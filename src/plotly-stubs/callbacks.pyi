from typing import Any

__all__ = [
    "BoxSelector",
    "InputDeviceState",
    "LassoSelector",
    "Points",
]

class InputDeviceState:
    def __init__(
        self,
        ctrl: bool = ...,
        alt: bool = ...,
        shift: bool = ...,
        meta: bool = ...,
        button: int = ...,
        buttons: int = ...,
        **_: Any,
    ) -> None: ...
    @property
    def alt(self) -> bool: ...
    @property
    def ctrl(self) -> bool: ...
    @property
    def shift(self) -> bool: ...
    @property
    def meta(self) -> bool: ...
    @property
    def button(self) -> int: ...
    @property
    def buttons(self) -> int: ...

class Points:
    def __init__(
        self,
        point_inds: list[int] = ...,
        xs: list[float] = ...,
        ys: list[float] = ...,
        trace_name: str = ...,
        trace_index: int = ...,
    ) -> None: ...
    @property
    def point_inds(self) -> list[int]: ...
    @property
    def xs(self) -> list[float]: ...
    @property
    def ys(self) -> list[float]: ...
    @property
    def trace_name(self) -> str: ...
    @property
    def trace_index(self) -> int: ...

class BoxSelector:
    def __init__(
        self,
        xrange: tuple[float, float] = ...,
        yrange: tuple[float, float] = ...,
        **_: Any,
    ) -> None: ...
    @property
    def type(self) -> str: ...
    @property
    def xrange(self) -> tuple[float, float]: ...
    @property
    def yrange(self) -> tuple[float, float]: ...

class LassoSelector:
    def __init__(
        self,
        xs: list[float] = ...,
        ys: list[float] = ...,
        **_: Any,
    ) -> None: ...
    @property
    def type(self) -> str: ...
    @property
    def xs(self) -> list[float]: ...
    @property
    def ys(self) -> list[float]: ...
