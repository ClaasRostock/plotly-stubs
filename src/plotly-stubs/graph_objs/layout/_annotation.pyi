# pyright: reportPropertyTypeMismatch=false
from typing import Any

from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
from plotly.graph_objs.layout.annotation import (
    Font,
    Hoverlabel,
)

class Annotation(_BaseLayoutHierarchyType):
    _parent_path_str = ...
    _path_str = ...
    _valid_props = ...
    @property
    def align(self) -> str | None: ...
    @align.setter
    def align(self, val: str | None) -> None: ...
    @property
    def arrowcolor(self) -> str | None: ...
    @arrowcolor.setter
    def arrowcolor(self, val: str | None) -> None: ...
    @property
    def arrowhead(self) -> int | None: ...
    @arrowhead.setter
    def arrowhead(self, val: int | None) -> None: ...
    @property
    def arrowside(self) -> str | None: ...
    @arrowside.setter
    def arrowside(self, val: str | None) -> None: ...
    @property
    def arrowsize(self) -> int | float | None: ...
    @arrowsize.setter
    def arrowsize(self, val: int | float | None) -> None: ...
    @property
    def arrowwidth(self) -> int | float | None: ...
    @arrowwidth.setter
    def arrowwidth(self, val: int | float | None) -> None: ...
    @property
    def ax(self) -> int | float | None: ...
    @ax.setter
    def ax(self, val: int | float | None) -> None: ...
    @property
    def axref(self) -> str | None: ...
    @axref.setter
    def axref(self, val: str | None) -> None: ...
    @property
    def ay(self) -> int | float | None: ...
    @ay.setter
    def ay(self, val: int | float | None) -> None: ...
    @property
    def ayref(self) -> str | None: ...
    @ayref.setter
    def ayref(self, val: str | None) -> None: ...
    @property
    def bgcolor(self) -> str | None: ...
    @bgcolor.setter
    def bgcolor(self, val: str | None) -> None: ...
    @property
    def bordercolor(self) -> str | None: ...
    @bordercolor.setter
    def bordercolor(self, val: str | None) -> None: ...
    @property
    def borderpad(self) -> int | float | None: ...
    @borderpad.setter
    def borderpad(self, val: int | float | None) -> None: ...
    @property
    def borderwidth(self) -> int | float | None: ...
    @borderwidth.setter
    def borderwidth(self, val: int | float | None) -> None: ...
    @property
    def captureevents(self) -> bool | None: ...
    @captureevents.setter
    def captureevents(self, val: bool | None) -> None: ...
    @property
    def clicktoshow(self) -> bool | str | None: ...
    @clicktoshow.setter
    def clicktoshow(self, val: bool | str | None) -> None: ...
    @property
    def font(self) -> Font: ...
    @font.setter
    def font(self, val: Font | dict[str, Any]) -> None: ...
    @property
    def height(self) -> int | float | None: ...
    @height.setter
    def height(self, val: int | float | None) -> None: ...
    @property
    def hoverlabel(self) -> Hoverlabel: ...
    @hoverlabel.setter
    def hoverlabel(self, val: Hoverlabel | dict[str, Any]) -> None: ...
    @property
    def hovertext(self) -> str | None: ...
    @hovertext.setter
    def hovertext(self, val: str | None) -> None: ...
    @property
    def name(self) -> str | int | None: ...
    @name.setter
    def name(self, val: str | int | None) -> None: ...
    @property
    def opacity(self) -> int | float | None: ...
    @opacity.setter
    def opacity(self, val: int | float | None) -> None: ...
    @property
    def showarrow(self) -> bool | None: ...
    @showarrow.setter
    def showarrow(self, val: bool | None) -> None: ...
    @property
    def standoff(self) -> int | float | None: ...
    @standoff.setter
    def standoff(self, val: int | float | None) -> None: ...
    @property
    def startarrowhead(self) -> int | None: ...
    @startarrowhead.setter
    def startarrowhead(self, val: int | None) -> None: ...
    @property
    def startarrowsize(self) -> int | float | None: ...
    @startarrowsize.setter
    def startarrowsize(self, val: int | float | None) -> None: ...
    @property
    def startstandoff(self) -> int | float | None: ...
    @startstandoff.setter
    def startstandoff(self, val: int | float | None) -> None: ...
    @property
    def templateitemname(self) -> str | int | None: ...
    @templateitemname.setter
    def templateitemname(self, val: str | int | None) -> None: ...
    @property
    def text(self) -> str | None: ...
    @text.setter
    def text(self, val: str | None) -> None: ...
    @property
    def textangle(self) -> int | float | None: ...
    @textangle.setter
    def textangle(self, val: int | float | None) -> None: ...
    @property
    def valign(self) -> str | None: ...
    @valign.setter
    def valign(self, val: str | None) -> None: ...
    @property
    def visible(self) -> bool | None: ...
    @visible.setter
    def visible(self, val: bool | None) -> None: ...
    @property
    def width(self) -> int | float | None: ...
    @width.setter
    def width(self, val: int | float | None) -> None: ...
    @property
    def x(self) -> Any | None: ...
    @x.setter
    def x(self, val: Any | None) -> None: ...
    @property
    def xanchor(self) -> str | None: ...
    @xanchor.setter
    def xanchor(self, val: str | None) -> None: ...
    @property
    def xclick(self) -> Any | None: ...
    @xclick.setter
    def xclick(self, val: Any | None) -> None: ...
    @property
    def xref(self) -> str | None: ...
    @xref.setter
    def xref(self, val: str | None) -> None: ...
    @property
    def xshift(self) -> int | float | None: ...
    @xshift.setter
    def xshift(self, val: int | float | None) -> None: ...
    @property
    def y(self) -> Any | None: ...
    @y.setter
    def y(self, val: Any | None) -> None: ...
    @property
    def yanchor(self) -> str | None: ...
    @yanchor.setter
    def yanchor(self, val: str | None) -> None: ...
    @property
    def yclick(self) -> Any | None: ...
    @yclick.setter
    def yclick(self, val: Any | None) -> None: ...
    @property
    def yref(self) -> str | None: ...
    @yref.setter
    def yref(self, val: str | None) -> None: ...
    @property
    def yshift(self) -> int | float | None: ...
    @yshift.setter
    def yshift(self, val: int | float | None) -> None: ...
    def __init__(
        self,
        arg: Annotation | dict[str, Any] | None = ...,
        align: str | None = ...,
        arrowcolor: str | None = ...,
        arrowhead: int | None = ...,
        arrowside: str | None = ...,
        arrowsize: int | float | None = ...,
        arrowwidth: int | float | None = ...,
        ax: int | float | None = ...,
        axref: str | None = ...,
        ay: int | float | None = ...,
        ayref: str | None = ...,
        bgcolor: str | None = ...,
        bordercolor: str | None = ...,
        borderpad: int | float | None = ...,
        borderwidth: int | float | None = ...,
        captureevents: bool | None = ...,
        clicktoshow: bool | str | None = ...,
        font: Font | dict[str, Any] | None = ...,
        height: int | float | None = ...,
        hoverlabel: Hoverlabel | dict[str, Any] | None = ...,
        hovertext: str | None = ...,
        name: str | int | None = ...,
        opacity: int | float | None = ...,
        showarrow: bool | None = ...,
        standoff: int | float | None = ...,
        startarrowhead: int | None = ...,
        startarrowsize: int | float | None = ...,
        startstandoff: int | float | None = ...,
        templateitemname: str | int | None = ...,
        text: str | None = ...,
        textangle: int | float | None = ...,
        valign: str | None = ...,
        visible: bool | None = ...,
        width: int | float | None = ...,
        x: Any | None = ...,
        xanchor: str | None = ...,
        xclick: Any | None = ...,
        xref: str | None = ...,
        xshift: int | float | None = ...,
        y: Any | None = ...,
        yanchor: str | None = ...,
        yclick: Any | None = ...,
        yref: str | None = ...,
        yshift: int | float | None = ...,
        **kwargs: Any,
    ) -> None: ...
