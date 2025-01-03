from dataclasses import dataclass

import numpy as np


@dataclass(slots=True)
class PositionVars:
    actual_holding_volume: np.ndarray
    target_volume: np.ndarray


@dataclass(slots=True)
class BuyVars:
    target_buy_volume: np.ndarray
    available_buy_volume: np.ndarray
    actual_buy_volume: np.ndarray
    actual_buy_amount: np.ndarray
    available_buy_amount: np.ndarray
    target_buy_amount: np.ndarray
    target_buy_amount_sum: np.ndarray


@dataclass(slots=True)
class SellVars:
    target_sell_volume: np.ndarray
    actual_sell_volume: np.ndarray
    actual_sell_amount: np.ndarray


@dataclass(slots=True)
class ResultVars:
    valuation: np.ndarray
    cash: np.ndarray
    nav: np.ndarray


@dataclass(slots=True)
class SimulationVariables:
    shape: tuple[int, int]
    shape_1d: tuple[int, int] = None
    position: PositionVars = None
    buy: BuyVars = None
    sell: SellVars = None
    result: ResultVars = None

    def __post_init__(self):
        self.shape_1d = (self.shape[0], 1)

        # Initialize sub-dataclasses
        self.position = PositionVars(
            actual_holding_volume=np.full(self.shape, np.nan, dtype=np.float64),
            target_volume=np.full(self.shape, np.nan, dtype=np.float64),
        )

        self.buy = BuyVars(
            target_buy_volume=np.full(self.shape, np.nan, dtype=np.float64),
            available_buy_volume=np.full(self.shape, np.nan, dtype=np.float64),
            available_buy_amount=np.full(self.shape_1d, np.nan, dtype=np.float64),
            actual_buy_volume=np.full(self.shape, np.nan, dtype=np.float64),
            actual_buy_amount=np.full(self.shape, np.nan, dtype=np.float64),
            target_buy_amount=np.full(self.shape, np.nan, dtype=np.float64),
            target_buy_amount_sum=np.full(self.shape_1d, np.nan, dtype=np.float64),
        )

        self.sell = SellVars(
            target_sell_volume=np.full(self.shape, np.nan, dtype=np.float64),
            actual_sell_volume=np.full(self.shape, np.nan, dtype=np.float64),
            actual_sell_amount=np.full(self.shape, np.nan, dtype=np.float64),
        )

        self.result = ResultVars(
            valuation=np.full(self.shape, np.nan, dtype=np.float64),
            cash=np.full(self.shape_1d, np.nan, dtype=np.float64),
            nav=np.full(self.shape_1d, np.nan, dtype=np.float64),
        )

    def initialize(self, initial_cash: np.float64):
        self.position.actual_holding_volume[0] = 0

        self.result.cash[0] = initial_cash
        self.result.nav[0] = initial_cash
        self.result.valuation[0] = 0
