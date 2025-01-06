import warnings
from dataclasses import dataclass, field
from typing import Literal, Optional

import numpy as np
import pandas as pd

from finter.backtest.v0.config import (
    CacheConfig,
    CostConfig,
    DataConfig,
    DateConfig,
    ExecutionConfig,
    FrameConfig,
    OptionalConfig,
    SimulatorConfig,
)
from finter.backtest.v0.simulators.base import BaseBacktestor
from finter.backtest.v0.simulators.basic import BasicBacktestor
from finter.backtest.v0.simulators.idn_fof import IDNFOFBacktestor
from finter.backtest.v0.simulators.vars import InputVars
from finter.data.data_handler.main import DataHandler

POSITION_SCALAR = 1e8
BASIS_POINT_SCALAR = 10000


@dataclass
class SimulatorBuilder:
    data: DataConfig = field(default_factory=DataConfig)

    date: DateConfig = field(default_factory=DateConfig)
    cost: CostConfig = field(default_factory=CostConfig)
    execution: ExecutionConfig = field(default_factory=ExecutionConfig)
    optional: OptionalConfig = field(default_factory=OptionalConfig)
    cache: CacheConfig = field(default_factory=CacheConfig)
    frame: FrameConfig = field(default_factory=FrameConfig)

    def build(self) -> BaseBacktestor:
        if self.data.position is None or self.data.price is None:
            raise ValueError("Both position and price data are required")

        if not (self.date.start < self.date.end):
            raise ValueError("Start date must be earlier than end date")

        self.frame = self.__build_frame()
        config = self.__build_config()
        input_vars = self.__build_input_vars(config)

        if self.execution.market_type == "basic":
            return BasicBacktestor(config, input_vars)
        elif self.execution.market_type == "idn_fof":
            return IDNFOFBacktestor(config, input_vars)
        else:
            raise ValueError(f"Unknown market type: {self.execution.market_type}")

    def __build_input_vars(self, config: SimulatorConfig) -> InputVars:
        weight, price, rebalancing_mask = DataProcessor.preprocess_position(
            config, self.data
        )
        volume_capacity = DataProcessor.preprocess_volume_capacity(config, self.data)

        buy_price = price * (1 + self.cost.slippage)
        sell_price = price * (1 - self.cost.slippage)

        return InputVars(
            weight=weight,
            price=price,
            buy_price=buy_price,
            sell_price=sell_price,
            volume_capacity=volume_capacity,
            rebalancing_mask=rebalancing_mask,
        )

    def __build_frame(self) -> FrameConfig:
        return FrameConfig(
            shape=self.data.price.shape,
            common_columns=self.data.position.columns.intersection(
                self.data.price.columns
            ).tolist(),
            common_index=self.data.price.index.tolist(),
        )

    def __build_config(self) -> SimulatorConfig:
        return SimulatorConfig(
            date=self.date,
            cost=self.cost,
            execution=self.execution,
            optional=self.optional,
            cache=self.cache,
            frame=self.frame,
        )

    def update_data(
        self,
        position: Optional[pd.DataFrame] = None,
        price: Optional[pd.DataFrame] = None,
        volume: Optional[pd.DataFrame] = None,
    ) -> "SimulatorBuilder":
        def _filter_nonzero_and_common_columns(
            position: pd.DataFrame, price: pd.DataFrame
        ) -> tuple[pd.DataFrame, pd.DataFrame]:
            non_zero_columns = position.columns[position.sum() != 0]
            position = position[non_zero_columns]
            price = price[non_zero_columns]

            common_columns = position.columns.intersection(price.columns)
            if len(common_columns) == 0:
                raise ValueError("No overlapping columns between position and price")

            position = position[common_columns]
            price = price[common_columns]

            return position, price

        def _align_index_with_price(
            position: pd.DataFrame, price: pd.DataFrame
        ) -> tuple[pd.DataFrame, pd.DataFrame, pd.Timestamp]:
            position_start_date = position.index.min()
            price_before_position = price.loc[price.index < position_start_date]

            if price_before_position.empty:
                warnings.warn(
                    "No price data before position start date. "
                    "Position data will be trimmed to match available price data.",
                    UserWarning,
                )
                price_start_date = price.index[0]
                position = position.loc[position.index >= price_start_date]
            else:
                price_start_date = price_before_position.index[-1]

            price = price.loc[price_start_date:]
            position = position.reindex(price.index).loc[: position.index[-1]]
            price = price.loc[: position.index[-1]]

            return position, price, price_start_date

        position = position if position is not None else self.data.position
        price = price if price is not None else self.data.price
        volume = volume if volume is not None else self.data.volume

        if position is not None and price is not None:
            position, price = _filter_nonzero_and_common_columns(position, price)
            position, price, price_start_date = _align_index_with_price(position, price)

            if volume is not None:
                volume = volume.loc[price_start_date:, position.columns]
                volume = volume.reindex(position.index).loc[: position.index[-1]]

        self.data = DataConfig(position=position, price=price, volume=volume)

        return self

    def update_date(
        self, start: Optional[int] = None, end: Optional[int] = None
    ) -> "SimulatorBuilder":
        self.date = DateConfig(
            start=start if start is not None else self.date.start,
            end=end if end is not None else self.date.end,
        )
        return self

    def update_cost(
        self,
        buy_fee_tax: np.float64 = None,
        sell_fee_tax: np.float64 = None,
        slippage: np.float64 = None,
    ) -> "SimulatorBuilder":
        buy_fee_tax = (
            buy_fee_tax / BASIS_POINT_SCALAR
            if buy_fee_tax is not None
            else self.cost.buy_fee_tax
        )
        sell_fee_tax = (
            sell_fee_tax / BASIS_POINT_SCALAR
            if sell_fee_tax is not None
            else self.cost.sell_fee_tax
        )
        slippage = (
            slippage / BASIS_POINT_SCALAR
            if slippage is not None
            else self.cost.slippage
        )

        self.cost = CostConfig(
            buy_fee_tax=buy_fee_tax,
            sell_fee_tax=sell_fee_tax,
            slippage=slippage,
        )
        return self

    def update_execution(
        self,
        initial_cash: np.float64 = None,
        auto_rebalance: bool = None,
        resample_period: Literal[None, "W", "M", "Q"] = None,
        volume_capacity_ratio: np.float64 = None,
        market_type: Literal["basic", "idn_fof"] = None,
    ) -> "SimulatorBuilder":
        self.execution = ExecutionConfig(
            initial_cash=initial_cash
            if initial_cash is not None
            else self.execution.initial_cash,
            auto_rebalance=auto_rebalance
            if auto_rebalance is not None
            else self.execution.auto_rebalance,
            resample_period=resample_period
            if resample_period is not None
            else self.execution.resample_period,
            volume_capacity_ratio=volume_capacity_ratio
            if volume_capacity_ratio is not None
            else self.execution.volume_capacity_ratio,
            market_type=market_type
            if market_type is not None
            else self.execution.market_type,
        )
        return self

    def update_optional(self, debug: bool = None) -> "SimulatorBuilder":
        self.optional = OptionalConfig(
            debug=debug if debug is not None else self.optional.debug,
        )
        return self

    def update_cache(
        self, data_handler: DataHandler = None, timeout: int = None, maxsize: int = None
    ) -> "SimulatorBuilder":
        self.cache = CacheConfig(
            data_handler=data_handler
            if data_handler is not None
            else self.cache.data_handler,
            timeout=timeout if timeout is not None else self.cache.timeout,
            maxsize=maxsize if maxsize is not None else self.cache.maxsize,
        )
        return self


class DataProcessor:
    def __init__(self):
        pass

    @staticmethod
    def preprocess_position(config: SimulatorConfig, data: DataConfig):
        from finter.modeling.utils import daily2period, get_rebalancing_mask

        if config.execution.resample_period:
            position = daily2period(
                data.position,
                config.execution.resample_period,
                keep_index=True,
            )
            rebalancing_mask = np.array(
                [
                    d
                    in get_rebalancing_mask(
                        data.position, config.execution.resample_period
                    )
                    for d in config.frame.common_index
                ],
                dtype=int,
            )
        else:
            position = data.position
            rebalancing_mask = np.ones(len(config.frame.common_index), dtype=int)

        return (
            (position / POSITION_SCALAR).to_numpy(),
            data.price.to_numpy(),
            rebalancing_mask,
        )

    @staticmethod
    def preprocess_volume_capacity(config: SimulatorConfig, data: DataConfig):
        if config.execution.volume_capacity_ratio == 0:
            volume = pd.DataFrame(
                np.inf,
                index=config.frame.common_index,
                columns=config.frame.common_columns,
            )
            return volume.to_numpy()
        else:
            volume = data.volume.reindex(
                config.frame.common_index,
                columns=config.frame.common_columns,
            )
        return volume.fillna(0).to_numpy() * config.execution.volume_capacity_ratio


if __name__ == "__main__":
    from finter.data import ContentFactory, ModelData

    start, end = 20220101, 20240101
    position = ModelData.load("alpha.krx.krx.stock.ldh0127.div_new_1").loc["2022"]
    price = ContentFactory("kr_stock", start, end).get_df("price_close", fill_nan=False)

    builder = SimulatorBuilder()

    (
        builder.update_data(position=position, price=price)
        .update_date(start=start, end=end)
        .update_cost(buy_fee_tax=10, sell_fee_tax=10, slippage=10)
        .update_execution(initial_cash=1e4)
        .update_optional(debug=True)
    )

    res = []
    for resample_period in [None, "M", "Q", "W"]:
        builder.update_execution(resample_period=resample_period)
        simulator = builder.build()
        res.append(simulator.run())
