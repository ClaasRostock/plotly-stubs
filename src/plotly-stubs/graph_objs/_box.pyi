# pyright: reportPropertyTypeMismatch=false
from collections.abc import Hashable, Sequence
from typing import Any

import numpy as np
import pandas as pd
import plotly.graph_objs.box.selected as _selected
import plotly.graph_objs.box.unselected as _unselected
from plotly.basedatatypes import BaseTraceType as _BaseTraceType
from plotly.graph_objs.box import (
    Hoverlabel,
    Legendgrouptitle,
    Line,
    Marker,
    Selected,
    Stream,
    Unselected,
)

class Box(_BaseTraceType):
    _parent_path_str = ...
    _path_str = ...
    _valid_props = ...
    @property
    def alignmentgroup(self) -> str | int | None: ...
    @alignmentgroup.setter
    def alignmentgroup(self, val: str | int | None) -> None: ...
    @property
    def boxmean(self) -> bool | str | None: ...
    @boxmean.setter
    def boxmean(self, val: bool | str | None) -> None: ...
    @property
    def boxpoints(self) -> bool | str | None: ...
    @boxpoints.setter
    def boxpoints(self, val: bool | str | None) -> None: ...
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
    def fillcolor(self) -> str | None: ...
    @fillcolor.setter
    def fillcolor(self, val: str | None) -> None: ...
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
    def hovertemplate(self) -> str | float | Sequence[str] | Sequence[float]: ...
    @hovertemplate.setter
    def hovertemplate(
        self, val: str | float | Sequence[str] | Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]]
    ) -> None: ...
    @property
    def hovertemplatesrc(self) -> str | None: ...
    @hovertemplatesrc.setter
    def hovertemplatesrc(self, val: str | None) -> None: ...
    @property
    def hovertext(self) -> str | Sequence[str]: ...
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
    def jitter(self) -> int | float | None: ...
    @jitter.setter
    def jitter(self, val: int | float | None) -> None: ...
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
    def lowerfence(self) -> Sequence[int] | Sequence[float]: ...
    @lowerfence.setter
    def lowerfence(
        self,
        val: Sequence[int] | Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] | pd.Series[float],
    ) -> None: ...
    @property
    def lowerfencesrc(self) -> str | None: ...
    @lowerfencesrc.setter
    def lowerfencesrc(self, val: str | None) -> None: ...
    @property
    def marker(self) -> Marker: ...
    @marker.setter
    def marker(self, val: Marker | dict[str, Any]) -> None: ...
    @property
    def mean(self) -> Sequence[float]: ...
    @mean.setter
    def mean(
        self, val: Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] | pd.Series[float]
    ) -> None: ...
    @property
    def meansrc(self) -> str | None: ...
    @meansrc.setter
    def meansrc(self, val: str | None) -> None: ...
    @property
    def median(self) -> Sequence[float]: ...
    @median.setter
    def median(
        self, val: Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] | pd.Series[float]
    ) -> None: ...
    @property
    def mediansrc(self) -> str | None: ...
    @mediansrc.setter
    def mediansrc(self, val: str | None) -> None: ...
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
    def notched(self) -> bool | None: ...
    @notched.setter
    def notched(self, val: bool | None) -> None: ...
    @property
    def notchspan(self) -> Sequence[float]: ...
    @notchspan.setter
    def notchspan(
        self, val: Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] | pd.Series[float]
    ) -> None: ...
    @property
    def notchspansrc(self) -> str | None: ...
    @notchspansrc.setter
    def notchspansrc(self, val: str | None) -> None: ...
    @property
    def notchwidth(self) -> int | float | None: ...
    @notchwidth.setter
    def notchwidth(self, val: int | float | None) -> None: ...
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
    def pointpos(self) -> int | float | None: ...
    @pointpos.setter
    def pointpos(self, val: int | float | None) -> None: ...
    @property
    def q1(self) -> Sequence[float]: ...
    @q1.setter
    def q1(
        self, val: Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] | pd.Series[float]
    ) -> None: ...
    @property
    def q1src(self) -> str | None: ...
    @q1src.setter
    def q1src(self, val: str | None) -> None: ...
    @property
    def q3(self) -> Sequence[float]: ...
    @q3.setter
    def q3(
        self, val: Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] | pd.Series[float]
    ) -> None: ...
    @property
    def q3src(self) -> str | None: ...
    @q3src.setter
    def q3src(self, val: str | None) -> None: ...
    @property
    def quartilemethod(self) -> str | None: ...
    @quartilemethod.setter
    def quartilemethod(self, val: str | None) -> None: ...
    @property
    def sd(self) -> Sequence[float]: ...
    @sd.setter
    def sd(
        self, val: Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] | pd.Series[float]
    ) -> None: ...
    @property
    def sdmultiple(self) -> int | float | None: ...
    @sdmultiple.setter
    def sdmultiple(self, val: int | float | None) -> None: ...
    @property
    def sdsrc(self) -> str | None: ...
    @sdsrc.setter
    def sdsrc(self, val: str | None) -> None: ...
    @property
    def selected(self) -> Selected: ...
    @selected.setter
    def selected(self, val: Selected | dict[str, _selected.Marker | dict[str, Any]]) -> None: ...
    @property
    def selectedpoints(self) -> Sequence[int]: ...
    @selectedpoints.setter
    def selectedpoints(self, val: Sequence[int]) -> None: ...
    @property
    def showlegend(self) -> bool | None: ...
    @showlegend.setter
    def showlegend(self, val: bool | None) -> None: ...
    @property
    def showwhiskers(self) -> bool | None: ...
    @showwhiskers.setter
    def showwhiskers(self, val: bool | None) -> None: ...
    @property
    def sizemode(self) -> str | None: ...
    @sizemode.setter
    def sizemode(self, val: str | None) -> None: ...
    @property
    def stream(self) -> Stream: ...
    @stream.setter
    def stream(self, val: Stream | dict[str, int | str]) -> None: ...
    @property
    def text(self) -> str | Sequence[str]: ...
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
    def unselected(self) -> Unselected: ...
    @unselected.setter
    def unselected(self, val: Unselected | dict[str, _unselected.Marker | dict[str, Any]]) -> None: ...
    @property
    def upperfence(self) -> Sequence[int] | Sequence[float]: ...
    @upperfence.setter
    def upperfence(
        self,
        val: Sequence[int] | Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] | pd.Series[float],
    ) -> None: ...
    @property
    def upperfencesrc(self) -> str | None: ...
    @upperfencesrc.setter
    def upperfencesrc(self, val: str | None) -> None: ...
    @property
    def visible(self) -> bool | str | None: ...
    @visible.setter
    def visible(self, val: bool | str | None) -> None: ...
    @property
    def whiskerwidth(self) -> int | float | None: ...
    @whiskerwidth.setter
    def whiskerwidth(self, val: int | float | None) -> None: ...
    @property
    def width(self) -> int | float | None: ...
    @width.setter
    def width(self, val: int | float | None) -> None: ...
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
    def type(self) -> str: ...
    def __init__(
        self,
        arg: Box | dict[str, Any] | None = ...,
        alignmentgroup: str | None = ...,
        boxmean: bool | str | None = ...,
        boxpoints: bool | str | None = ...,
        customdata: Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] | pd.Series[float] | None = ...,
        customdatasrc: str | None = ...,
        dx: int | float | None = ...,
        dy: int | float | None = ...,
        fillcolor: str | None = ...,
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
        jitter: int | float | None = ...,
        legend: str | None = ...,
        legendgroup: str | int | None = ...,
        legendgrouptitle: Legendgrouptitle | dict[str, Any] | None = ...,
        legendrank: int | float | None = ...,
        legendwidth: int | float | None = ...,
        line: Line | dict[str, str | int | float] | None = ...,
        lowerfence: Sequence[int]
        | Sequence[float]
        | np.ndarray[tuple[int, ...], np.dtype[np.float64]]
        | pd.Series[float]
        | None = ...,
        lowerfencesrc: str | None = ...,
        marker: Marker | dict[str, Any] | None = ...,
        mean: Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] | pd.Series[float] | None = ...,
        meansrc: str | None = ...,
        median: Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] | pd.Series[float] | None = ...,
        mediansrc: str | None = ...,
        meta: Sequence[Any] | dict[str, Any] | np.ndarray[tuple[int, ...], Any] | None = ...,
        metasrc: str | None = ...,
        name: str | int | None = ...,
        notched: bool | None = ...,
        notchspan: Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] | pd.Series[float] | None = ...,
        notchspansrc: str | None = ...,
        notchwidth: int | float | None = ...,
        offsetgroup: str | int | None = ...,
        opacity: int | float | None = ...,
        orientation: str | None = ...,
        pointpos: int | float | None = ...,
        q1: Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] | pd.Series[float] | None = ...,
        q1src: str | None = ...,
        q3: Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] | pd.Series[float] | None = ...,
        q3src: str | None = ...,
        quartilemethod: str | None = ...,
        sd: Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] | pd.Series[float] | None = ...,
        sdmultiple: int | float | None = ...,
        sdsrc: str | None = ...,
        selected: Selected | dict[str, _selected.Marker | dict[str, Any]] | None = ...,
        selectedpoints: Sequence[int] | None = ...,
        showlegend: bool | None = ...,
        showwhiskers: bool | None = ...,
        sizemode: str | None = ...,
        stream: Stream | dict[str, int | str] | None = ...,
        text: str
        | float
        | Sequence[str]
        | Sequence[float]
        | np.ndarray[tuple[int, ...], np.dtype[np.float64]]
        | None = ...,
        textsrc: str | None = ...,
        uid: str | int | None = ...,
        uirevision: Hashable | None = ...,
        unselected: Unselected | dict[str, _unselected.Marker | dict[str, Any]] | None = ...,
        upperfence: Sequence[int]
        | Sequence[float]
        | np.ndarray[tuple[int, ...], np.dtype[np.float64]]
        | pd.Series[float]
        | None = ...,
        upperfencesrc: str | None = ...,
        visible: bool | str | None = ...,
        whiskerwidth: int | float | None = ...,
        width: int | float | None = ...,
        x: Sequence[int]
        | Sequence[float]
        | np.ndarray[tuple[int, ...], np.dtype[np.float64]]
        | pd.Series[float]
        | None = ...,
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
