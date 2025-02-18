# pyright: reportPropertyTypeMismatch=false
from collections.abc import Hashable, Sequence
from typing import Any

import numpy as np
import pandas as pd
from plotly.basedatatypes import BaseTraceType as _BaseTraceType
from plotly.graph_objs.surface import (
    ColorBar,
    Contours,
    Hoverlabel,
    Legendgrouptitle,
    Lighting,
    Lightposition,
    Stream,
)

class Surface(_BaseTraceType):
    _parent_path_str = ...
    _path_str = ...
    _valid_props = ...
    @property
    def autocolorscale(self) -> bool | None: ...
    @autocolorscale.setter
    def autocolorscale(self, val: bool | None) -> None: ...
    @property
    def cauto(self) -> bool | None: ...
    @cauto.setter
    def cauto(self, val: bool | None) -> None: ...
    @property
    def cmax(self) -> int | float | None: ...
    @cmax.setter
    def cmax(self, val: int | float | None) -> None: ...
    @property
    def cmid(self) -> int | float | None: ...
    @cmid.setter
    def cmid(self, val: int | float | None) -> None: ...
    @property
    def cmin(self) -> int | float | None: ...
    @cmin.setter
    def cmin(self, val: int | float | None) -> None: ...
    @property
    def coloraxis(self) -> str | None: ...
    @coloraxis.setter
    def coloraxis(self, val: str | None) -> None: ...
    @property
    def colorbar(self) -> ColorBar: ...
    @colorbar.setter
    def colorbar(self, val: ColorBar | dict[str, Any]) -> None: ...
    @property
    def colorscale(self) -> str | list[str] | list[tuple[float, str]]: ...
    @colorscale.setter
    def colorscale(self, val: str | list[str] | list[tuple[float, str]]) -> None: ...
    @property
    def connectgaps(self) -> bool | None: ...
    @connectgaps.setter
    def connectgaps(self, val: bool | None) -> None: ...
    @property
    def contours(self) -> Contours: ...
    @contours.setter
    def contours(self, val: Contours | dict[str, Any]) -> None: ...
    @property
    def customdata(self) -> Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] | pd.Series[float]: ...
    @customdata.setter
    def customdata(
        self, val: Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] | pd.Series[float]
    ) -> None: ...
    @property
    def customdatasrc(self) -> str | None: ...
    @customdatasrc.setter
    def customdatasrc(self, val: str | None) -> None: ...
    @property
    def hidesurface(self) -> bool | None: ...
    @hidesurface.setter
    def hidesurface(self, val: bool | None) -> None: ...
    @property
    def hoverinfo(self) -> str | Sequence[str] | None: ...
    @hoverinfo.setter
    def hoverinfo(self, val: str | Sequence[str] | None) -> None: ...
    @property
    def hoverinfosrc(self) -> str | None: ...
    @hoverinfosrc.setter
    def hoverinfosrc(self, val: str | None) -> None: ...
    @property
    def hoverlabel(self) -> Hoverlabel: ...
    @hoverlabel.setter
    def hoverlabel(self, val: Hoverlabel | dict[str, Any]) -> None: ...
    @property
    def hovertemplate(
        self,
    ) -> str | float | Sequence[str] | Sequence[float]: ...
    @hovertemplate.setter
    def hovertemplate(
        self, val: str | float | Sequence[str] | Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]]
    ) -> None: ...
    @property
    def hovertemplatesrc(self) -> str | None: ...
    @hovertemplatesrc.setter
    def hovertemplatesrc(self, val: str | None) -> None: ...
    @property
    def hovertext(
        self,
    ) -> str | float | Sequence[str] | Sequence[float]: ...
    @hovertext.setter
    def hovertext(
        self, val: str | float | Sequence[str] | Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]]
    ) -> None: ...
    @property
    def hovertextsrc(self) -> str | None: ...
    @hovertextsrc.setter
    def hovertextsrc(self, val: str | None) -> None: ...
    @property
    def ids(self) -> Sequence[str]: ...
    @ids.setter
    def ids(self, val: Sequence[str] | np.ndarray[tuple[int, ...], np.dtype[np.str_]] | pd.Series[str]) -> None: ...
    @property
    def idssrc(self) -> str | None: ...
    @idssrc.setter
    def idssrc(self, val: str | None) -> None: ...
    @property
    def legend(self) -> str | None: ...
    @legend.setter
    def legend(self, val: str | None) -> None: ...
    @property
    def legendgroup(self) -> str | int | None: ...
    @legendgroup.setter
    def legendgroup(self, val: str | int | None) -> None: ...
    @property
    def legendgrouptitle(self) -> Legendgrouptitle: ...
    @legendgrouptitle.setter
    def legendgrouptitle(self, val: Legendgrouptitle | dict[str, Any]) -> None: ...
    @property
    def legendrank(self) -> int | float | None: ...
    @legendrank.setter
    def legendrank(self, val: int | float | None) -> None: ...
    @property
    def legendwidth(self) -> int | float | None: ...
    @legendwidth.setter
    def legendwidth(self, val: int | float | None) -> None: ...
    @property
    def lighting(self) -> Lighting: ...
    @lighting.setter
    def lighting(self, val: Lighting | dict[str, Any]) -> None: ...
    @property
    def lightposition(self) -> Lightposition: ...
    @lightposition.setter
    def lightposition(
        self,
        val: Lightposition
        | dict[str, Sequence[int] | Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]]],
    ) -> None: ...
    @property
    def meta(self) -> Sequence[Any] | dict[str, Any] | np.ndarray[tuple[int, ...], Any]: ...
    @meta.setter
    def meta(self, val: Sequence[Any] | dict[str, Any] | np.ndarray[tuple[int, ...], Any]) -> None: ...
    @property
    def metasrc(self) -> str | None: ...
    @metasrc.setter
    def metasrc(self, val: str | None) -> None: ...
    @property
    def name(self) -> str | int | None: ...
    @name.setter
    def name(self, val: str | int | None) -> None: ...
    @property
    def opacity(self) -> int | float | None: ...
    @opacity.setter
    def opacity(self, val: int | float | None) -> None: ...
    @property
    def opacityscale(self) -> str | list[tuple[float, float]] | None: ...
    @opacityscale.setter
    def opacityscale(self, val: str | list[tuple[float, float]] | None) -> None: ...
    @property
    def reversescale(self) -> bool | None: ...
    @reversescale.setter
    def reversescale(self, val: bool | None) -> None: ...
    @property
    def scene(self) -> str | None: ...
    @scene.setter
    def scene(self, val: str | None) -> None: ...
    @property
    def showlegend(self) -> bool | None: ...
    @showlegend.setter
    def showlegend(self, val: bool | None) -> None: ...
    @property
    def showscale(self) -> bool | None: ...
    @showscale.setter
    def showscale(self, val: bool | None) -> None: ...
    @property
    def stream(self) -> Stream: ...
    @stream.setter
    def stream(self, val: Stream | dict[str, int | str]) -> None: ...
    @property
    def surfacecolor(self) -> Sequence[str]: ...
    @surfacecolor.setter
    def surfacecolor(
        self, val: Sequence[str] | np.ndarray[tuple[int, ...], np.dtype[np.str_]] | pd.Series[str]
    ) -> None: ...
    @property
    def surfacecolorsrc(self) -> str | None: ...
    @surfacecolorsrc.setter
    def surfacecolorsrc(self, val: str | None) -> None: ...
    @property
    def text(self) -> str | Sequence[str] | None: ...
    @text.setter
    def text(
        self, val: str | float | Sequence[str] | Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]]
    ) -> None: ...
    @property
    def textsrc(self) -> str | None: ...
    @textsrc.setter
    def textsrc(self, val: str | None) -> None: ...
    @property
    def uid(self) -> str | int | None: ...
    @uid.setter
    def uid(self, val: str | int | None) -> None: ...
    @property
    def uirevision(self) -> Hashable | None: ...
    @uirevision.setter
    def uirevision(self, val: Hashable | None) -> None: ...
    @property
    def visible(self) -> bool | str | None: ...
    @visible.setter
    def visible(self, val: bool | str | None) -> None: ...
    @property
    def x(
        self,
    ) -> Sequence[int] | Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] | pd.Series[float]: ...
    @x.setter
    def x(
        self,
        val: Sequence[int] | Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] | pd.Series[float],
    ) -> None: ...
    @property
    def xcalendar(self) -> str | None: ...
    @xcalendar.setter
    def xcalendar(self, val: str | None) -> None: ...
    @property
    def xhoverformat(self) -> str | None: ...
    @xhoverformat.setter
    def xhoverformat(self, val: str | None) -> None: ...
    @property
    def xsrc(self) -> str | None: ...
    @xsrc.setter
    def xsrc(self, val: str | None) -> None: ...
    @property
    def y(
        self,
    ) -> Sequence[int] | Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] | pd.Series[float]: ...
    @y.setter
    def y(
        self,
        val: Sequence[int] | Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] | pd.Series[float],
    ) -> None: ...
    @property
    def ycalendar(self) -> str | None: ...
    @ycalendar.setter
    def ycalendar(self, val: str | None) -> None: ...
    @property
    def yhoverformat(self) -> str | None: ...
    @yhoverformat.setter
    def yhoverformat(self, val: str | None) -> None: ...
    @property
    def ysrc(self) -> str | None: ...
    @ysrc.setter
    def ysrc(self, val: str | None) -> None: ...
    @property
    def z(
        self,
    ) -> Sequence[int] | Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] | pd.Series[float]: ...
    @z.setter
    def z(
        self,
        val: Sequence[int] | Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] | pd.Series[float],
    ) -> None: ...
    @property
    def zcalendar(self) -> str | None: ...
    @zcalendar.setter
    def zcalendar(self, val: str | None) -> None: ...
    @property
    def zhoverformat(self) -> str | None: ...
    @zhoverformat.setter
    def zhoverformat(self, val: str | None) -> None: ...
    @property
    def zsrc(self) -> str | None: ...
    @zsrc.setter
    def zsrc(self, val: str | None) -> None: ...
    @property
    def type(self) -> str | None: ...
    def __init__(
        self,
        arg: Surface | dict[str, Any] | None = ...,
        autocolorscale: bool | None = ...,
        cauto: bool | None = ...,
        cmax: int | float | None = ...,
        cmid: int | float | None = ...,
        cmin: int | float | None = ...,
        coloraxis: str | None = ...,
        colorbar: ColorBar | dict[str, Any] | None = ...,
        colorscale: str | list[str] | list[tuple[float, str]] | None = ...,
        connectgaps: bool | None = ...,
        contours: Contours | dict[str, Any] | None = ...,
        customdata: Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] | pd.Series[float] | None = ...,
        customdatasrc: str | None = ...,
        hidesurface: bool | None = ...,
        hoverinfo: str | Sequence[str] | None = ...,
        hoverinfosrc: str | None = ...,
        hoverlabel: Hoverlabel | dict[str, Any] | None = ...,
        hovertemplate: str
        | float
        | Sequence[str]
        | Sequence[float]
        | np.ndarray[tuple[int, ...], np.dtype[np.float64]]
        | None = ...,
        hovertemplatesrc: str | None = ...,
        hovertext: str
        | float
        | Sequence[str]
        | Sequence[float]
        | np.ndarray[tuple[int, ...], np.dtype[np.float64]]
        | None = ...,
        hovertextsrc: str | None = ...,
        ids: Sequence[str] | np.ndarray[tuple[int, ...], np.dtype[np.str_]] | pd.Series[str] | None = ...,
        idssrc: str | None = ...,
        legend: str | None = ...,
        legendgroup: str | int | None = ...,
        legendgrouptitle: Legendgrouptitle | dict[str, Any] | None = ...,
        legendrank: int | float | None = ...,
        legendwidth: int | float | None = ...,
        lighting: Lighting | dict[str, Any] | None = ...,
        lightposition: Lightposition
        | dict[str, Sequence[int] | Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]]]
        | None = ...,
        meta: Sequence[Any] | dict[str, Any] | np.ndarray[tuple[int, ...], Any] | None = ...,
        metasrc: str | None = ...,
        name: str | int | None = ...,
        opacity: int | float | None = ...,
        opacityscale: str | list[tuple[float, float]] | None = ...,
        reversescale: bool | None = ...,
        scene: str | None = ...,
        showlegend: bool | None = ...,
        showscale: bool | None = ...,
        stream: Stream | dict[str, int | str] | None = ...,
        surfacecolor: Sequence[str] | np.ndarray[tuple[int, ...], np.dtype[np.str_]] | pd.Series[str] | None = ...,
        surfacecolorsrc: str | None = ...,
        text: str
        | float
        | Sequence[str]
        | Sequence[float]
        | np.ndarray[tuple[int, ...], np.dtype[np.float64]]
        | None = ...,
        textsrc: str | None = ...,
        uid: str | int | None = ...,
        uirevision: Hashable | None = ...,
        visible: bool | str | None = ...,
        x: Sequence[int]
        | Sequence[float]
        | np.ndarray[tuple[int, ...], np.dtype[np.float64]]
        | pd.Series[float]
        | None = ...,
        xcalendar: str | None = ...,
        xhoverformat: str | None = ...,
        xsrc: str | None = ...,
        y: Sequence[int]
        | Sequence[float]
        | np.ndarray[tuple[int, ...], np.dtype[np.float64]]
        | pd.Series[float]
        | None = ...,
        ycalendar: str | None = ...,
        yhoverformat: str | None = ...,
        ysrc: str | None = ...,
        z: Sequence[int]
        | Sequence[float]
        | np.ndarray[tuple[int, ...], np.dtype[np.float64]]
        | pd.Series[float]
        | None = ...,
        zcalendar: str | None = ...,
        zhoverformat: str | None = ...,
        zsrc: str | None = ...,
        **kwargs: Any,
    ) -> None: ...
