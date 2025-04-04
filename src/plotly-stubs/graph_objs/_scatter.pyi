# pyright: reportPropertyTypeMismatch=false
from collections.abc import Hashable, Sequence
from typing import Any

import numpy as np
import pandas as pd
import plotly.graph_objs.scatter.selected as _selected
import plotly.graph_objs.scatter.unselected as _unselected
from plotly.basedatatypes import BaseTraceType as _BaseTraceType
from plotly.graph_objs.scatter import (
    ErrorX,
    ErrorY,
    Fillgradient,
    Fillpattern,
    Hoverlabel,
    Legendgrouptitle,
    Line,
    Marker,
    Selected,
    Stream,
    Textfont,
    Unselected,
)

class Scatter(_BaseTraceType):
    _parent_path_str = ...
    _path_str = ...
    _valid_props = ...
    @property
    def alignmentgroup(self) -> str | int | None: ...
    @alignmentgroup.setter
    def alignmentgroup(self, val: str | int | None) -> None: ...
    @property
    def cliponaxis(self) -> bool | None: ...
    @cliponaxis.setter
    def cliponaxis(self, val: bool | None) -> None: ...
    @property
    def connectgaps(self) -> bool | None: ...
    @connectgaps.setter
    def connectgaps(self, val: bool | None) -> None: ...
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
    def dx(self) -> int | float | None: ...
    @dx.setter
    def dx(self, val: int | float | None) -> None: ...
    @property
    def dy(self) -> int | float | None: ...
    @dy.setter
    def dy(self, val: int | float | None) -> None: ...
    @property
    def error_x(self) -> ErrorX: ...
    @error_x.setter
    def error_x(self, val: ErrorX | dict[str, Any]) -> None: ...
    @property
    def error_y(self) -> ErrorY: ...
    @error_y.setter
    def error_y(self, val: ErrorY | dict[str, Any]) -> None: ...
    @property
    def fill(self) -> str | None: ...
    @fill.setter
    def fill(self, val: str | None) -> None: ...
    @property
    def fillcolor(self) -> str | None: ...
    @fillcolor.setter
    def fillcolor(self, val: str | None) -> None: ...
    @property
    def fillgradient(self) -> Fillgradient | None: ...
    @fillgradient.setter
    def fillgradient(self, val: Fillgradient | dict[str, Any] | None) -> None: ...
    @property
    def fillpattern(self) -> Fillpattern: ...
    @fillpattern.setter
    def fillpattern(self, val: Fillpattern | dict[str, Any]) -> None: ...
    @property
    def groupnorm(self) -> str | None: ...
    @groupnorm.setter
    def groupnorm(self, val: str | None) -> None: ...
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
    def hoveron(self) -> str | None: ...
    @hoveron.setter
    def hoveron(self, val: str | None) -> None: ...
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
    def hovertext(self) -> str | Sequence[str] | None: ...
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
    def line(self) -> Line: ...
    @line.setter
    def line(self, val: Line | dict[str, str | int | float]) -> None: ...
    @property
    def marker(self) -> Marker: ...
    @marker.setter
    def marker(self, val: Marker | dict[str, Any]) -> None: ...
    @property
    def meta(self) -> Sequence[Any] | dict[str, Any] | np.ndarray[tuple[int, ...], Any]: ...
    @meta.setter
    def meta(self, val: Sequence[Any] | dict[str, Any] | np.ndarray[tuple[int, ...], Any]) -> None: ...
    @property
    def metasrc(self) -> str | None: ...
    @metasrc.setter
    def metasrc(self, val: str | None) -> None: ...
    @property
    def mode(self) -> str | None: ...
    @mode.setter
    def mode(self, val: str | None) -> None: ...
    @property
    def name(self) -> str | int | None: ...
    @name.setter
    def name(self, val: str | int | None) -> None: ...
    @property
    def offsetgroup(self) -> str | int | None: ...
    @offsetgroup.setter
    def offsetgroup(self, val: str | int | None) -> None: ...
    @property
    def opacity(self) -> int | float | None: ...
    @opacity.setter
    def opacity(self, val: int | float | None) -> None: ...
    @property
    def orientation(self) -> str | None: ...
    @orientation.setter
    def orientation(self, val: str | None) -> None: ...
    @property
    def selected(self) -> Selected: ...
    @selected.setter
    def selected(self, val: Selected | dict[str, _selected.Marker | _selected.Textfont | dict[str, Any]]) -> None: ...
    @property
    def selectedpoints(self) -> Sequence[int]: ...
    @selectedpoints.setter
    def selectedpoints(self, val: Sequence[int]) -> None: ...
    @property
    def showlegend(self) -> bool | None: ...
    @showlegend.setter
    def showlegend(self, val: bool | None) -> None: ...
    @property
    def stackgaps(self) -> str | None: ...
    @stackgaps.setter
    def stackgaps(self, val: str | None) -> None: ...
    @property
    def stackgroup(self) -> str | int | None: ...
    @stackgroup.setter
    def stackgroup(self, val: str | int | None) -> None: ...
    @property
    def stream(self) -> Stream: ...
    @stream.setter
    def stream(self, val: Stream | dict[str, int | str]) -> None: ...
    @property
    def text(self) -> str | Sequence[str] | None: ...
    @text.setter
    def text(
        self, val: str | float | Sequence[str] | Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]]
    ) -> None: ...
    @property
    def textfont(self) -> Textfont: ...
    @textfont.setter
    def textfont(self, val: Textfont | dict[str, Any]) -> None: ...
    @property
    def textposition(self) -> str | Sequence[str] | None: ...
    @textposition.setter
    def textposition(self, val: str | Sequence[str] | np.ndarray[tuple[int, ...], np.dtype[np.str_]]) -> None: ...
    @property
    def textpositionsrc(self) -> str | None: ...
    @textpositionsrc.setter
    def textpositionsrc(self, val: str | None) -> None: ...
    @property
    def textsrc(self) -> str | None: ...
    @textsrc.setter
    def textsrc(self, val: str | None) -> None: ...
    @property
    def texttemplate(self) -> str | float | Sequence[str] | Sequence[float]: ...
    @texttemplate.setter
    def texttemplate(
        self, val: str | float | Sequence[str] | Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]]
    ) -> None: ...
    @property
    def texttemplatesrc(self) -> str | None: ...
    @texttemplatesrc.setter
    def texttemplatesrc(self, val: str | None) -> None: ...
    @property
    def uid(self) -> str | int | None: ...
    @uid.setter
    def uid(self, val: str | int | None) -> None: ...
    @property
    def uirevision(self) -> Hashable | None: ...
    @uirevision.setter
    def uirevision(self, val: Hashable | None) -> None: ...
    @property
    def unselected(self) -> Unselected: ...
    @unselected.setter
    def unselected(
        self, val: Unselected | dict[str, _unselected.Marker | _unselected.Textfont | dict[str, Any]]
    ) -> None: ...
    @property
    def visible(self) -> bool | str | None: ...
    @visible.setter
    def visible(self, val: bool | str | None) -> None: ...
    @property
    def x(
        self,
    ) -> Sequence[Any] | np.ndarray[tuple[int, ...], np.dtype[Any]] | pd.Series[Any]: ...
    @x.setter
    def x(
        self,
        val: Sequence[Any] | np.ndarray[tuple[int, ...], np.dtype[Any]] | pd.Series[Any],
    ) -> None: ...
    @property
    def x0(self) -> int | float | None: ...
    @x0.setter
    def x0(self, val: int | float | None) -> None: ...
    @property
    def xaxis(self) -> str | None: ...
    @xaxis.setter
    def xaxis(self, val: str | None) -> None: ...
    @property
    def xcalendar(self) -> str | None: ...
    @xcalendar.setter
    def xcalendar(self, val: str | None) -> None: ...
    @property
    def xhoverformat(self) -> str | None: ...
    @xhoverformat.setter
    def xhoverformat(self, val: str | None) -> None: ...
    @property
    def xperiod(self) -> int | float | str | None: ...
    @xperiod.setter
    def xperiod(self, val: int | float | str | None) -> None: ...
    @property
    def xperiod0(self) -> int | float | str | None: ...
    @xperiod0.setter
    def xperiod0(self, val: int | float | str | None) -> None: ...
    @property
    def xperiodalignment(self) -> str | None: ...
    @xperiodalignment.setter
    def xperiodalignment(self, val: str | None) -> None: ...
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
    def y0(self) -> int | float | None: ...
    @y0.setter
    def y0(self, val: int | float | None) -> None: ...
    @property
    def yaxis(self) -> str | None: ...
    @yaxis.setter
    def yaxis(self, val: str | None) -> None: ...
    @property
    def ycalendar(self) -> str | None: ...
    @ycalendar.setter
    def ycalendar(self, val: str | None) -> None: ...
    @property
    def yhoverformat(self) -> str | None: ...
    @yhoverformat.setter
    def yhoverformat(self, val: str | None) -> None: ...
    @property
    def yperiod(self) -> int | float | str | None: ...
    @yperiod.setter
    def yperiod(self, val: int | float | str | None) -> None: ...
    @property
    def yperiod0(self) -> int | float | str | None: ...
    @yperiod0.setter
    def yperiod0(self, val: int | float | str | None) -> None: ...
    @property
    def yperiodalignment(self) -> str | None: ...
    @yperiodalignment.setter
    def yperiodalignment(self, val: str | None) -> None: ...
    @property
    def ysrc(self) -> str | None: ...
    @ysrc.setter
    def ysrc(self, val: str | None) -> None: ...
    @property
    def zorder(self) -> int | None: ...
    @zorder.setter
    def zorder(self, val: int | None) -> None: ...
    @property
    def type(self) -> str | None: ...
    def __init__(
        self,
        arg: Scatter | dict[str, Any] | None = ...,
        alignmentgroup: str | int | None = ...,
        cliponaxis: bool | None = ...,
        connectgaps: bool | None = ...,
        customdata: Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] | pd.Series[float] | None = ...,
        customdatasrc: str | None = ...,
        dx: int | float | None = ...,
        dy: int | float | None = ...,
        error_x: ErrorX | dict[str, Any] | None = ...,
        error_y: ErrorY | dict[str, Any] | None = ...,
        fill: str | None = ...,
        fillcolor: str | None = ...,
        fillgradient: Fillgradient | dict[str, Any] | None = ...,
        fillpattern: Fillpattern | dict[str, Any] | None = ...,
        groupnorm: str | None = ...,
        hoverinfo: str | Sequence[str] | None = ...,
        hoverinfosrc: str | None = ...,
        hoverlabel: Hoverlabel | dict[str, Any] | None = ...,
        hoveron: str | None = ...,
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
        line: Line | dict[str, str | int | float] | None = ...,
        marker: Marker | dict[str, Any] | None = ...,
        meta: Sequence[Any] | dict[str, Any] | np.ndarray[tuple[int, ...], Any] | None = ...,
        metasrc: str | None = ...,
        mode: str | None = ...,
        name: str | int | None = ...,
        offsetgroup: str | int | None = ...,
        opacity: int | float | None = ...,
        orientation: str | None = ...,
        selected: Selected | dict[str, _selected.Marker | _selected.Textfont | dict[str, Any]] | None = ...,
        selectedpoints: Sequence[int] | None = ...,
        showlegend: bool | None = ...,
        stackgaps: str | None = ...,
        stackgroup: str | int | None = ...,
        stream: Stream | dict[str, int | str] | None = ...,
        text: str | Sequence[str] | None = ...,
        textfont: Textfont | dict[str, Any] | None = ...,
        textposition: str | Sequence[str] | np.ndarray[tuple[int, ...], np.dtype[np.str_]] | None = ...,
        textpositionsrc: str | None = ...,
        textsrc: str | None = ...,
        texttemplate: str | None = ...,
        texttemplatesrc: str | None = ...,
        uid: str | int | None = ...,
        uirevision: Hashable | None = ...,
        unselected: Unselected | dict[str, _unselected.Marker | _unselected.Textfont | dict[str, Any]] | None = ...,
        visible: bool | str | None = ...,
        x: Sequence[Any] | np.ndarray[tuple[int, ...], np.dtype[Any]] | pd.Series[Any] | None = ...,
        x0: int | float | None = ...,
        xaxis: str | None = ...,
        xcalendar: str | None = ...,
        xhoverformat: str | None = ...,
        xperiod: int | float | str | None = ...,
        xperiod0: int | float | str | None = ...,
        xperiodalignment: str | None = ...,
        xsrc: str | None = ...,
        y: Sequence[int]
        | Sequence[float]
        | np.ndarray[tuple[int, ...], np.dtype[np.float64]]
        | pd.Series[float]
        | None = ...,
        y0: int | float | None = ...,
        yaxis: str | None = ...,
        ycalendar: str | None = ...,
        yhoverformat: str | None = ...,
        yperiod: int | float | str | None = ...,
        yperiod0: int | float | str | None = ...,
        yperiodalignment: str | None = ...,
        ysrc: str | None = ...,
        zorder: int | None = ...,
        **kwargs: Any,
    ) -> None: ...
