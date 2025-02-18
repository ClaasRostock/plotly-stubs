from typing import Any

from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType

class Marker(_BaseTraceHierarchyType):
    _parent_path_str = ...
    _path_str = ...
    _valid_props = ...
    @property
    def color(self) -> str | None: ...
    @color.setter
    def color(self, val: str | None) -> None: ...
    @property
    def opacity(self) -> int | float | None: ...
    @opacity.setter
    def opacity(self, val: int | float | None) -> None: ...
    @property
    def size(self) -> int | float | None: ...
    @size.setter
    def size(self, val: int | float | None) -> None: ...
    def __init__(
        self,
        arg: dict[str, str | int | float] | Marker = ...,
        color: str = ...,
        opacity: int | float = ...,
        size: int | float = ...,
        **kwargs: Any,
    ) -> None: ...
