from dataclasses import dataclass
from datetime import datetime
from typing import Literal

import numpy as np
import pandas as pd

from finter.data.data_handler.main import DataHandler


@dataclass(slots=True)
class DataConfig:
    position: pd.DataFrame = None
    price: pd.DataFrame = None
    volume: pd.DataFrame = None


@dataclass(slots=True)
class DateConfig:
    start: int = 20150101  # e.g. 20200101
    end: int = int(datetime.now().strftime("%Y%m%d"))  # e.g. 20201231


@dataclass(slots=True)
class CostConfig:
    # unit: basis point
    buy_fee_tax: np.float64 = 0.0
    sell_fee_tax: np.float64 = 0.0
    slippage: np.float64 = 0.0


@dataclass(slots=True)
class ExecutionConfig:
    initial_cash: np.float64 = 1e8
    auto_rebalance: bool = True
    resample_period: Literal[None, "W", "M", "Q"] = None
    volume_capacity_ratio: np.float64 = 0.0


@dataclass(slots=True)
class OptionalConfig:
    # todo: currency, seperate dividend
    # adj_dividend: bool = False
    debug: bool = False


@dataclass(slots=True)
class CacheConfig:
    data_handler: DataHandler = None
    timeout: int = 300
    maxsize: int = 5


@dataclass(slots=True)
class FrameVars:
    shape: tuple[int, int] = None
    common_columns: list[str] = None
    common_index: list[str] = None


@dataclass(slots=True)
class SimulatorConfig:
    data: DataConfig
    date: DateConfig
    cost: CostConfig
    execution: ExecutionConfig
    optional: OptionalConfig
    cache: CacheConfig
    frame: FrameVars
