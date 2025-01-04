import numpy as np
import pandas as pd

from finter.backtest.v0.config import DataConfig, SimulatorConfig
from finter.backtest.v0.simulators.vars import SimulationVariables
from finter.modeling.utils import daily2period


class BaseBacktestor:
    def __init__(self, config: SimulatorConfig):
        self.frame = config.frame
        self.execution = config.execution
        self.optional = config.optional
        self.cost = config.cost

        self.weight, self.price = self.preprocess_position(config.data)
        self.volume_capacity = self.preprocess_volume_capacity(config.data)
        self.buy_price = self.price * (1 + self.cost.slippage)
        self.sell_price = self.price * (1 - self.cost.slippage)

        self.initialize_variables()

        self._results = BacktestResult(self)

    def preprocess_position(self, data: DataConfig):
        if self.execution.resample_period:
            position = daily2period(
                data.position, self.execution.resample_period, keep_index=True
            )
        else:
            position = data.position

        return (position / 1e8).to_numpy(), data.price.to_numpy()

    def preprocess_volume_capacity(self, data: DataConfig):
        if self.execution.volume_capacity_ratio == 0:
            volume = pd.DataFrame(
                np.inf, index=self.frame.common_index, columns=self.frame.common_columns
            )
            return volume.to_numpy()
        else:
            volume = data.volume.reindex(
                self.frame.common_index, columns=self.frame.common_columns
            )
            return volume.fillna(0).to_numpy() * self.execution.volume_capacity_ratio

    def initialize_variables(self) -> None:
        self.vars = SimulationVariables(self.frame.shape)
        self.vars.initialize(self.execution.initial_cash)

    def _clear_all_variables(self):
        for attr in list(self.__dict__.keys()):
            if attr not in ["summary"]:
                delattr(self, attr)

    def run(self):
        raise NotImplementedError

    @property
    def _summary(self):
        return self._results.summary

    def plot_single(self, single_asset):
        return self._results.plot_single(single_asset)


class BacktestResult:
    def __init__(self, simulator: BaseBacktestor) -> None:
        self.simulator = simulator
        self.vars = simulator.vars
        self.frame = simulator.frame

    def _create_df(
        self, data: np.ndarray, index: list[str], columns: list[str]
    ) -> pd.DataFrame:
        return pd.DataFrame(data, index=index, columns=columns)

    @property
    def nav(self) -> pd.DataFrame:
        return self._create_df(self.vars.result.nav, self.frame.common_index, ["nav"])

    @property
    def cash(self) -> pd.DataFrame:
        return self._create_df(self.vars.result.cash, self.frame.common_index, ["cash"])

    @property
    def valuation(self) -> pd.DataFrame:
        return self._create_df(
            self.vars.result.valuation.sum(axis=1),
            self.frame.common_index,
            ["valuation"],
        )

    @property
    def cost(self) -> pd.DataFrame:
        cost = np.nansum(
            (
                self.vars.buy.actual_buy_volume
                * self.simulator.buy_price
                * self.simulator.cost.buy_fee_tax
            )
            + (
                self.vars.sell.actual_sell_volume
                * self.simulator.sell_price
                * self.simulator.cost.sell_fee_tax
            ),
            axis=1,
        )
        return pd.DataFrame(
            cost,
            index=self.frame.common_index,
            columns=["cost"],
        )

    @property
    def slippage(self) -> pd.DataFrame:
        slippage = np.nansum(
            (
                self.vars.buy.actual_buy_volume
                * self.simulator.buy_price
                * (self.simulator.cost.slippage / (1 + self.simulator.cost.slippage))
            )
            + (
                self.vars.sell.actual_sell_volume
                * self.simulator.sell_price
                * (self.simulator.cost.slippage / (1 - self.simulator.cost.slippage))
            ),
            axis=1,
        )
        return pd.DataFrame(
            slippage,
            index=self.frame.common_index,
            columns=["slippage"],
        )

    @property
    def summary(self) -> pd.DataFrame:
        pnl = self.nav.diff().fillna(0) - self.cost.values
        pnl.columns = ("pnl",)

        result = pd.concat(
            [
                self.nav,
                self.cash,
                self.valuation,
                self.cost,
                self.slippage,
                pnl,
            ],
            axis=1,
        )
        return result
