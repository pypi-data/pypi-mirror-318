import numpy as np
import pandas as pd

from finter.backtest.v0.config import SimulatorConfig
from finter.backtest.v0.simulators.vars import InputVars, SimulationVariables


class BaseBacktestor:
    def __init__(self, config: SimulatorConfig, input_vars: InputVars):
        self.frame = config.frame
        self.execution = config.execution
        self.optional = config.optional
        self.cost = config.cost

        self.vars = SimulationVariables(input_vars, self.frame.shape)
        self.vars.initialize(self.execution.initial_cash)

        self._results = BacktestResult(self)

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
            self.vars.result.valuation,
            self.frame.common_index,
            self.frame.common_columns,
        )

    @property
    def cost(self) -> pd.DataFrame:
        cost = np.nansum(
            (
                self.vars.buy.actual_buy_volume
                * self.vars.input.buy_price
                * self.simulator.cost.buy_fee_tax
            )
            + (
                self.vars.sell.actual_sell_volume
                * self.vars.input.sell_price
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
                * self.vars.input.buy_price
                * (self.simulator.cost.slippage / (1 + self.simulator.cost.slippage))
            )
            + (
                self.vars.sell.actual_sell_volume
                * self.vars.input.sell_price
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
                self.valuation.sum(axis=1),
                self.cost,
                self.slippage,
                pnl,
            ],
            axis=1,
        )
        return result
