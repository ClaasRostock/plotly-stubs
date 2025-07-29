from collections.abc import Sequence
from typing import Any, Literal, Protocol, TypeAlias, TypedDict

import pandas as pd
import polars as pl
from numpy.typing import NDArray

class MapCenter(TypedDict):
    lat: int | float
    lon: int | float

class DataFrameCompatible(Protocol):
    # More details at https://data-apis.org/dataframe-protocol/latest/index.html
    def __dataframe__(self, nan_as_null: bool = ..., allow_copy: bool = ...) -> Any: ...

DataArray: TypeAlias = Sequence[Any] | pd.Series | pl.Series | NDArray[Any]
FrameOrDict: TypeAlias = DataFrameCompatible | dict[str, DataArray] | Sequence[dict[str, Any]]
ColumnData: TypeAlias = str | int | DataArray
MultiColumnData: TypeAlias = ColumnData | list[ColumnData]
HoverData: TypeAlias = ColumnData | list[str] | dict[str, bool | str | DataArray]

TrendLineOptions: TypeAlias = dict[
    str, Any
]  # Specified to better spot remaining "any" types, and facilitating eventual future improvements.
MapIdentity: TypeAlias = (
    dict[str | int, str] | Literal["identity"]
)  # Would rather use dict[str, str] | dict[int, str], but is currently technically correct for pandas.

RenderMode: TypeAlias = Literal["auto", "webgl", "svg"]
TrendLineScope: TypeAlias = Literal["trace", "overall"]
TrendlineFunc: TypeAlias = Literal["ols", "lowess", "rolling", "expanding", "ewm"]
BarMode: TypeAlias = Literal["relative", "group", "overlay"]
ValNorm: TypeAlias = Literal["fraction", "percent"]
EcdfMode: TypeAlias = Literal["reversed", "complementary", "standard"]
Direction: TypeAlias = Literal["clockwise", "counterclockwise"]
HistNorm: TypeAlias = Literal["percent", "probability", "density", "probability density"]
HistFunc: TypeAlias = Literal["count", "sum", "avg", "min", "max"]
Marginal: TypeAlias = Literal["rug", "box", "violin", "histogram"]
Points: TypeAlias = Literal["all", "outliers", "suspectedoutliers"]
LineShape: TypeAlias = Literal["linear", "spline", "hv", "vh", "hvh", "vhv"]
Orientation: TypeAlias = Literal["v", "h"]
DisplayMode: TypeAlias = Literal["group", "overlay"]
LocationMode: TypeAlias = Literal["ISO-3", "USA-states", "country names"]
Templates: TypeAlias = Literal[
    "ggplot2",
    "seaborn",
    "simple_white",
    "plotly",
    "plotly_white",
    "plotly_dark",
    "presentation",
    "xgridoff",
    "ygridoff",
    "gridon",
    "none",
]
