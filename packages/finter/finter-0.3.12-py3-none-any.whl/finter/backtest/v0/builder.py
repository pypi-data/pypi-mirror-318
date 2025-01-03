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
    FrameVars,
    OptionalConfig,
    SimulatorConfig,
)
from finter.backtest.v0.simulators.base import BaseBacktestor
from finter.backtest.v0.simulators.basic import BasicBacktestor
from finter.backtest.v0.simulators.idn_fof import IDNFOFBacktestor
from finter.data.data_handler.main import DataHandler


@dataclass
class SimulatorBuilder:
    data: DataConfig = field(default_factory=DataConfig)
    date: DateConfig = field(default_factory=DateConfig)
    cost: CostConfig = field(default_factory=CostConfig)
    execution: ExecutionConfig = field(default_factory=ExecutionConfig)
    optional: OptionalConfig = field(default_factory=OptionalConfig)
    cache: CacheConfig = field(default_factory=CacheConfig)
    frame: FrameVars = field(default_factory=FrameVars)
    market_type: Literal["basic", "idn_fof"] = "basic"

    def build(self) -> BaseBacktestor:
        # 기본적인 설정 검증
        if self.data.position is None or self.data.price is None:
            raise ValueError("Both position and price data are required")

        # 날짜 데이터 유효성 검증
        if not (self.date.start < self.date.end):
            raise ValueError("Start date must be earlier than end date")

        self.frame = FrameVars(
            shape=self.data.price.shape,
            common_columns=self.data.position.columns.intersection(
                self.data.price.columns
            ).tolist(),
            common_index=self.data.price.index.tolist(),
        )

        config = SimulatorConfig(
            data=self.data,
            date=self.date,
            cost=self.cost,
            execution=self.execution,
            optional=self.optional,
            cache=self.cache,
            frame=self.frame,
        )

        if self.market_type == "basic":
            return BasicBacktestor(config)
        elif self.market_type == "idn_fof":
            return IDNFOFBacktestor(config)
        else:
            raise ValueError(f"Unknown market type: {self.market_type}")

    def update_data(
        self,
        position: Optional[pd.DataFrame] = None,
        price: Optional[pd.DataFrame] = None,
        volume: Optional[pd.DataFrame] = None,
    ) -> "SimulatorBuilder":
        position = position if position is not None else self.data.position
        price = price if price is not None else self.data.price
        volume = volume if volume is not None else self.data.volume

        if position is not None and price is not None:
            non_zero_columns = position.columns[position.sum() != 0]
            position = position[non_zero_columns]
            price = price[non_zero_columns]

            common_columns = position.columns.intersection(price.columns)
            if len(common_columns) == 0:
                raise ValueError("No overlapping columns between position and price")

            position_start_date = position.index.min()
            price_before_position = price.loc[price.index < position_start_date]

            if len(price_before_position) == 0:
                import warnings

                warnings.warn(
                    "No price data before position start date. "
                    "Position data will be trimmed to match available price data.",
                    UserWarning,
                )
                position = position.loc[position.index > price.index[0]]
                price_start_date = price.index[0]
            else:
                price_start_date = price_before_position.index[-1]

            position = position[common_columns]
            price = price.loc[price_start_date:, common_columns]

            if volume is not None:
                volume = volume.loc[price_start_date:, common_columns]

        self.data = DataConfig(
            position=position,
            price=price,
            volume=volume,
        )
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
            buy_fee_tax / 10000 if buy_fee_tax is not None else self.cost.buy_fee_tax
        )
        sell_fee_tax = (
            sell_fee_tax / 10000 if sell_fee_tax is not None else self.cost.sell_fee_tax
        )
        slippage = slippage / 10000 if slippage is not None else self.cost.slippage

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

    def update_market_type(
        self, market_type: Literal["basic", "idn_fof"]
    ) -> "SimulatorBuilder":
        self.market_type = market_type
        return self


if __name__ == "__main__":
    from finter.data import ContentFactory, ModelData

    start, end = 20200101, 20240101
    position = ModelData.load("alpha.krx.krx.stock.ldh0127.div_new_1")
    price = ContentFactory("kr_stock", start, end).get_df("price_close", fill_nan=False)

    builder = SimulatorBuilder()

    (
        builder.update_data(position=position, price=price)
        .update_date(start=start, end=end)
        .update_cost(buy_fee_tax=0.001, sell_fee_tax=0.001, slippage=0.001)
        .update_execution(initial_cash=1e4)
    )

    res = []
    for market_type in ["basic", "idn_fof"]:
        builder.update_market_type(market_type)
        simulator = builder.build()
        res.append(simulator.run())

    res
