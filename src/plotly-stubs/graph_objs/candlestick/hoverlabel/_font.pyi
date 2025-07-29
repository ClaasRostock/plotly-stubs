from collections.abc import Sequence
from typing import Any

import numpy as np
from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType

class Font(_BaseTraceHierarchyType):
    _parent_path_str = ...
    _path_str = ...
    _valid_props = ...
    @property
    def color(self) -> str | Sequence[str] | np.ndarray[tuple[int, ...], np.dtype[np.str_]]: ...
    @color.setter
    def color(self, val: str | Sequence[str] | np.ndarray[tuple[int, ...], np.dtype[np.str_]]) -> None: ...
    @property
    def colorsrc(self) -> str | None: ...
    @colorsrc.setter
    def colorsrc(self, val: str | None) -> None: ...
    @property
    def family(self) -> str | Sequence[str] | np.ndarray[tuple[int], np.dtype[np.str_]]: ...
    @family.setter
    def family(self, val: str | Sequence[str] | np.ndarray[tuple[int], np.dtype[np.str_]]) -> None: ...
    @property
    def familysrc(self) -> str | None: ...
    @familysrc.setter
    def familysrc(self, val: str | None) -> None: ...
    @property
    def lineposition(self) -> str | Sequence[str] | np.ndarray[tuple[int, ...], np.dtype[np.str_]] | None: ...
    @lineposition.setter
    def lineposition(
        self, val: str | Sequence[str] | np.ndarray[tuple[int, ...], np.dtype[np.str_]] | None
    ) -> None: ...
    @property
    def linepositionsrc(self) -> str | None: ...
    @linepositionsrc.setter
    def linepositionsrc(self, val: str | None) -> None: ...
    @property
    def shadow(
        self,
    ) -> (
        str
        | int
        | float
        | Sequence[str]
        | Sequence[int]
        | Sequence[float]
        | np.ndarray[tuple[int], np.dtype[np.str_]]
        | np.ndarray[tuple[int], np.dtype[np.int_]]
        | np.ndarray[tuple[int], np.dtype[np.float64]]
    ): ...
    @shadow.setter
    def shadow(
        self,
        val: str
        | int
        | float
        | Sequence[str]
        | Sequence[int]
        | Sequence[float]
        | np.ndarray[tuple[int], np.dtype[np.str_]]
        | np.ndarray[tuple[int], np.dtype[np.int_]]
        | np.ndarray[tuple[int], np.dtype[np.float64]],
    ) -> None: ...
    @property
    def shadowsrc(self) -> str | None: ...
    @shadowsrc.setter
    def shadowsrc(self, val: str | None) -> None: ...
    @property
    def size(
        self,
    ) -> (
        int
        | float
        | Sequence[int]
        | Sequence[float]
        | np.ndarray[tuple[int], np.dtype[np.int_]]
        | np.ndarray[tuple[int], np.dtype[np.float64]]
    ): ...
    @size.setter
    def size(
        self,
        val: int
        | float
        | Sequence[int]
        | Sequence[float]
        | np.ndarray[tuple[int], np.dtype[np.int_]]
        | np.ndarray[tuple[int], np.dtype[np.float64]],
    ) -> None: ...
    @property
    def sizesrc(self) -> str | None: ...
    @sizesrc.setter
    def sizesrc(self, val: str | None) -> None: ...
    @property
    def style(self) -> str | Sequence[str] | np.ndarray[tuple[int], np.dtype[np.str_]] | None: ...
    @style.setter
    def style(self, val: str | Sequence[str] | np.ndarray[tuple[int], np.dtype[np.str_]] | None) -> None: ...
    @property
    def stylesrc(self) -> str | None: ...
    @stylesrc.setter
    def stylesrc(self, val: str | None) -> None: ...
    @property
    def textcase(self) -> str | Sequence[str] | np.ndarray[tuple[int], np.dtype[np.str_]] | None: ...
    @textcase.setter
    def textcase(self, val: str | Sequence[str] | np.ndarray[tuple[int], np.dtype[np.str_]] | None) -> None: ...
    @property
    def textcasesrc(self) -> str | None: ...
    @textcasesrc.setter
    def textcasesrc(self, val: str | None) -> None: ...
    @property
    def variant(self) -> str | Sequence[str] | np.ndarray[tuple[int], np.dtype[np.str_]] | None: ...
    @variant.setter
    def variant(self, val: str | Sequence[str] | np.ndarray[tuple[int], np.dtype[np.str_]] | None) -> None: ...
    @property
    def variantsrc(self) -> str | None: ...
    @variantsrc.setter
    def variantsrc(self, val: str | None) -> None: ...
    @property
    def weight(
        self,
    ) -> (
        int
        | float
        | str
        | Sequence[int]
        | Sequence[float]
        | Sequence[str]
        | np.ndarray[tuple[int], np.dtype[np.int_]]
        | np.ndarray[tuple[int], np.dtype[np.float64]]
        | np.ndarray[tuple[int], np.dtype[np.str_]]
        | None
    ): ...
    @weight.setter
    def weight(
        self,
        val: (
            int
            | float
            | str
            | Sequence[int]
            | Sequence[float]
            | Sequence[str]
            | np.ndarray[tuple[int], np.dtype[np.int_]]
            | np.ndarray[tuple[int], np.dtype[np.float64]]
            | np.ndarray[tuple[int], np.dtype[np.str_]]
            | None
        ),
    ) -> None: ...
    @property
    def weightsrc(self) -> str | None: ...
    @weightsrc.setter
    def weightsrc(self, val: str | None) -> None: ...
    def __init__(
        self,
        arg: Font | dict[str, Any] | None = ...,
        color: str | Sequence[str] | np.ndarray[tuple[int, ...], np.dtype[np.str_]] | None = ...,
        colorsrc: str | None = ...,
        family: str | Sequence[str] | np.ndarray[tuple[int], np.dtype[np.str_]] | None = ...,
        familysrc: str | None = ...,
        lineposition: str | Sequence[str] | np.ndarray[tuple[int, ...], np.dtype[np.str_]] | None = ...,
        linepositionsrc: str | None = ...,
        shadow: str
        | int
        | float
        | Sequence[str]
        | Sequence[int]
        | Sequence[float]
        | np.ndarray[tuple[int], np.dtype[np.str_]]
        | np.ndarray[tuple[int], np.dtype[np.int_]]
        | np.ndarray[tuple[int], np.dtype[np.float64]] = ...,
        shadowsrc: str | None = ...,
        size: int
        | float
        | Sequence[int]
        | Sequence[float]
        | np.ndarray[tuple[int], np.dtype[np.int_]]
        | np.ndarray[tuple[int], np.dtype[np.float64]]
        | None = ...,
        sizesrc: str | None = ...,
        style: str | Sequence[str] | np.ndarray[tuple[int], np.dtype[np.str_]] | None = ...,
        stylesrc: str | None = ...,
        textcase: str | Sequence[str] | np.ndarray[tuple[int], np.dtype[np.str_]] | None = ...,
        textcasesrc: str | None = ...,
        variant: str | Sequence[str] | np.ndarray[tuple[int], np.dtype[np.str_]] | None = ...,
        variantsrc: str | None = ...,
        weight: int
        | float
        | str
        | Sequence[int]
        | Sequence[float]
        | Sequence[str]
        | np.ndarray[tuple[int], np.dtype[np.int_]]
        | np.ndarray[tuple[int], np.dtype[np.float64]]
        | np.ndarray[tuple[int], np.dtype[np.str_]]
        | None = ...,
        weightsrc: str | None = ...,
        **kwargs: Any,
    ) -> None: ...
