from collections.abc import Sequence
from typing import Any

import numpy as np
import pandas as pd
from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
from plotly.graph_objs.candlestick.hoverlabel import Font

class Hoverlabel(_BaseTraceHierarchyType):
    _parent_path_str = ...
    _path_str = ...
    _valid_props = ...
    @property
    def align(self) -> str | Sequence[str] | np.ndarray[tuple[int], np.dtype[np.str_]]: ...
    @align.setter
    def align(self, val: str | Sequence[str] | np.ndarray[tuple[int], np.dtype[np.str_]]) -> None: ...
    @property
    def alignsrc(self) -> str | None: ...
    @alignsrc.setter
    def alignsrc(self, val: str | None) -> None: ...
    @property
    def bgcolor(self) -> str | Sequence[str] | np.ndarray[tuple[int, ...], np.dtype[np.str_]] | pd.Series[str]: ...
    @bgcolor.setter
    def bgcolor(
        self, val: str | Sequence[str] | np.ndarray[tuple[int, ...], np.dtype[np.str_]] | pd.Series[str]
    ) -> None: ...
    @property
    def bgcolorsrc(self) -> str | None: ...
    @bgcolorsrc.setter
    def bgcolorsrc(self, val: str | None) -> None: ...
    @property
    def bordercolor(self) -> str | Sequence[str] | np.ndarray[tuple[int, ...], np.dtype[np.str_]] | pd.Series[str]: ...
    @bordercolor.setter
    def bordercolor(
        self, val: str | Sequence[str] | np.ndarray[tuple[int, ...], np.dtype[np.str_]] | pd.Series[str]
    ) -> None: ...
    @property
    def bordercolorsrc(self) -> str | None: ...
    @bordercolorsrc.setter
    def bordercolorsrc(self, val: str | None) -> None: ...
    @property
    def font(self) -> Font | dict[str, Any] | None: ...
    @font.setter
    def font(self, val: Font | dict[str, Any] | None) -> None: ...
    @property
    def namelength(
        self,
    ) -> (
        int
        | float
        | Sequence[int]
        | Sequence[float]
        | np.ndarray[tuple[int, ...], np.dtype[np.int_]]
        | np.ndarray[tuple[int, ...], np.dtype[np.float64]]
        | pd.Series[str]
        | None
    ): ...
    @namelength.setter
    def namelength(
        self,
        val: (
            int
            | float
            | Sequence[int]
            | Sequence[float]
            | np.ndarray[tuple[int, ...], np.dtype[np.int_]]
            | np.ndarray[tuple[int, ...], np.dtype[np.float64]]
            | pd.Series[str]
            | None
        ),
    ) -> None: ...
    @property
    def namelengthsrc(self) -> str | None: ...
    @namelengthsrc.setter
    def namelengthsrc(self, val: str | None) -> None: ...
    @property
    def split(self) -> bool | None: ...
    @split.setter
    def split(self, val: bool | None) -> None: ...
    def __init__(
        self,
        arg: Hoverlabel | dict[str, Any] | None = ...,
        align: str | Sequence[str] | np.ndarray[tuple[int], np.dtype[np.str_]] | None = ...,
        alignsrc: str | None = ...,
        bgcolor: str | Sequence[str] | np.ndarray[tuple[int, ...], np.dtype[np.str_]] | pd.Series[str] | None = ...,
        bgcolorsrc: str | None = ...,
        bordercolor: str | Sequence[str] | np.ndarray[tuple[int, ...], np.dtype[np.str_]] | pd.Series[str] | None = ...,
        bordercolorsrc: str | None = ...,
        font: Font | dict[str, Any] | None = ...,
        namelength: int
        | float
        | Sequence[int]
        | Sequence[float]
        | np.ndarray[tuple[int, ...], np.dtype[np.int_]]
        | np.ndarray[tuple[int, ...], np.dtype[np.float64]]
        | pd.Series[str]
        | None = ...,
        namelengthsrc: str | None = ...,
        split: bool | None = ...,
        **kwargs: Any,
    ) -> None: ...
