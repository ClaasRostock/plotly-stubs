from collections.abc import Callable, Generator, Hashable, Sequence
from typing import Any

import numpy as np
import pandas as pd
from plotly.basedatatypes import BaseFigure, BaseLayoutHierarchyType, BaseLayoutType, BaseTraceType
from plotly.graph_objs import (
    Frame,
    Layout,
    bar,
    barpolar,
    box,
    candlestick,
    carpet,
    choropleth,
    choroplethmap,
    choroplethmapbox,
    cone,
    contour,
    contourcarpet,
    densitymap,
    densitymapbox,
    funnel,
    funnelarea,
    heatmap,
    histogram,
    histogram2d,
    histogram2dcontour,
    icicle,
    image,
    indicator,
    isosurface,
    layout,
    mesh3d,
    ohlc,
    parcats,
    parcoords,
    pie,
    sankey,
    scatter,
    scatter3d,
    scattercarpet,
    scattergeo,
    scattergl,
    scattermap,
    scattermapbox,
    scatterpolar,
    scatterpolargl,
    scattersmith,
    scatterternary,
    splom,
    streamtube,
    sunburst,
    surface,
    table,
    treemap,
    violin,
    volume,
    waterfall,
)

class Figure(BaseFigure):
    def __init__(
        self,
        data: Sequence[BaseTraceType] | Sequence[dict[str, Any]] | BaseTraceType | BaseFigure | dict[str, Any] = ...,
        layout: Layout | dict[str, Any] = ...,
        frames: Sequence[Frame] | Sequence[dict[str, Any]] = ...,
        skip_invalid: bool = ...,
        **kwargs: Any,
    ) -> None: ...
    def update(
        self,
        dict1: dict[str, Any] = ...,
        overwrite: bool = ...,
        **kwargs: Any,
    ) -> Figure: ...
    def update_traces(
        self,
        patch: dict[str, Any] | None = ...,
        selector: dict[str, Any] | Callable[[BaseTraceType], bool] | int | str | None = ...,
        row: int | None = ...,
        col: int | None = ...,
        secondary_y: bool | None = ...,
        overwrite: bool = ...,
        **kwargs: Any,
    ) -> Figure: ...
    def update_layout(
        self,
        dict1: dict[str, Any] = ...,
        overwrite: bool = ...,
        **kwargs: Any,
    ) -> Figure: ...
    def for_each_trace(
        self,
        fn: Callable[[BaseTraceType], Any],
        selector: dict[str, Any] | Callable[[BaseTraceType], bool] | int | str | None = ...,
        row: int | None = ...,
        col: int | None = ...,
        secondary_y: bool | None = ...,
    ) -> Figure: ...
    def add_trace(
        self,
        trace: BaseTraceType | dict[str, Any],
        row: int | str | None = ...,
        col: int | str | None = ...,
        secondary_y: bool | None = ...,
        exclude_empty_subplots: bool = ...,
    ) -> Figure: ...
    def add_traces(
        self,
        data: Sequence[BaseTraceType | dict[str, Any]],
        rows: Sequence[int] | int | None = ...,
        cols: Sequence[int] | int | None = ...,
        secondary_ys: Sequence[bool] | None = ...,
        exclude_empty_subplots: bool = ...,
    ) -> Figure: ...
    def add_vline(
        self,
        x: int | float,
        row: int | str | None = ...,
        col: int | str | None = ...,
        exclude_empty_subplots: bool = ...,
        annotation: layout.Annotation | dict[str, Any] = ...,
        annotation_position: str | None = ...,
        **kwargs: Any,
    ) -> Figure: ...
    def add_hline(
        self,
        y: int | float,
        row: int | str | None = ...,
        col: int | str | None = ...,
        exclude_empty_subplots: bool = ...,
        annotation: layout.Annotation | dict[str, Any] = ...,
        annotation_position: str | None = ...,
        **kwargs: Any,
    ) -> Figure: ...
    def add_vrect(
        self,
        x0: int | float,
        x1: int | float,
        row: int | str | None = ...,
        col: int | str | None = ...,
        exclude_empty_subplots: bool = ...,
        annotation: layout.Annotation | dict[str, Any] = ...,
        annotation_position: str | None = ...,
        **kwargs: Any,
    ) -> Figure: ...
    def add_hrect(
        self,
        y0: int | float,
        y1: int | float,
        row: int | str | None = ...,
        col: int | str | None = ...,
        exclude_empty_subplots: bool = ...,
        annotation: layout.Annotation | dict[str, Any] = ...,
        annotation_position: str | None = ...,
        **kwargs: Any,
    ) -> Figure: ...
    def set_subplots(
        self,
        rows: int = ...,
        cols: int = ...,
        shared_xaxes: bool | str = ...,
        shared_yaxes: bool | str = ...,
        start_cell: str = ...,
        print_grid: bool = ...,
        horizontal_spacing: float = ...,
        vertical_spacing: float = ...,
        subplot_titles: list[str] | None = ...,
        column_widths: list[float] | None = ...,
        row_heights: list[float] | None = ...,
        specs: list[list[dict[str, str | bool | int | float] | None]] | None = ...,
        insets: list[dict[str, tuple[int, int] | str | float]] | None = ...,
        column_titles: list[str] | None = ...,
        row_titles: list[str] | None = ...,
        x_title: str | None = ...,
        y_title: str | None = ...,
        figure: BaseFigure | None = ...,
        **kwargs: Any,
    ) -> Figure: ...
    def add_bar(
        self,
        alignmentgroup: str | int = ...,
        base: Any = ...,
        basesrc: str = ...,
        cliponaxis: bool = ...,
        constraintext: str = ...,
        customdata: Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] | pd.Series[float] = ...,
        customdatasrc: str = ...,
        dx: int | float = ...,
        dy: int | float = ...,
        error_x: bar.ErrorX | dict[str, Any] = ...,
        error_y: bar.ErrorY | dict[str, Any] = ...,
        hoverinfo: str | Sequence[str] = ...,
        hoverinfosrc: str = ...,
        hoverlabel: bar.Hoverlabel | dict[str, Any] = ...,
        hovertemplate: str
        | float
        | Sequence[str]
        | Sequence[float]
        | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        hovertemplatesrc: str = ...,
        hovertext: str
        | float
        | Sequence[str]
        | Sequence[float]
        | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        hovertextsrc: str = ...,
        ids: Sequence[str] | np.ndarray[tuple[int, ...], np.dtype[np.str_]] | pd.Series[str] = ...,
        idssrc: str = ...,
        insidetextanchor: str = ...,
        insidetextfont: bar.Insidetextfont | dict[str, Any] = ...,
        legend: str = ...,
        legendgroup: str | int = ...,
        legendgrouptitle: bar.Legendgrouptitle | dict[str, Any] = ...,
        legendrank: int | float = ...,
        legendwidth: int | float = ...,
        marker: bar.Marker | dict[str, Any] = ...,
        meta: Sequence[Any] | dict[str, Any] | np.ndarray[tuple[int, ...], Any] = ...,
        metasrc: str = ...,
        name: str | int = ...,
        offset: int | float | Sequence[int] | Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        offsetgroup: str | int = ...,
        offsetsrc: str = ...,
        opacity: int | float = ...,
        orientation: str = ...,
        outsidetextfont: bar.Outsidetextfont | dict[str, Any] = ...,
        selected: bar.Selected | dict[str, bar.selected.Marker | bar.selected.Textfont | dict[str, Any]] = ...,
        selectedpoints: Sequence[int] = ...,
        showlegend: bool = ...,
        stream: bar.Stream | dict[str, int | str] = ...,
        text: str | float | Sequence[str] | Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        textangle: int | float = ...,
        textfont: bar.Textfont | dict[str, Any] = ...,
        textposition: str | Sequence[str] | np.ndarray[tuple[int, ...], np.dtype[np.str_]] = ...,
        textpositionsrc: str = ...,
        textsrc: str = ...,
        texttemplate: str
        | float
        | Sequence[str]
        | Sequence[float]
        | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        texttemplatesrc: str = ...,
        uid: str | int = ...,
        uirevision: Hashable = ...,
        unselected: bar.Unselected | dict[str, bar.unselected.Marker | bar.unselected.Textfont | dict[str, Any]] = ...,
        visible: bool | str = ...,
        width: int | float | Sequence[int] | Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        widthsrc: str = ...,
        x: Sequence[Any] | np.ndarray[tuple[int, ...], np.dtype[Any]] | pd.Series[Any] | None = ...,
        x0: int | float = ...,
        xaxis: str = ...,
        xcalendar: str = ...,
        xhoverformat: str = ...,
        xperiod: int | float | str = ...,
        xperiod0: int | float | str = ...,
        xperiodalignment: str = ...,
        xsrc: str = ...,
        y: Sequence[int] | Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] | pd.Series[float] = ...,
        y0: int | float = ...,
        yaxis: str = ...,
        ycalendar: str = ...,
        yhoverformat: str = ...,
        yperiod: int | float | str = ...,
        yperiod0: int | float | str = ...,
        yperiodalignment: str = ...,
        ysrc: str = ...,
        zorder: int = ...,
        row: int | str | None = ...,
        col: int | str | None = ...,
        secondary_y: bool | None = ...,
        **kwargs: Any,
    ) -> Figure: ...
    def add_barpolar(
        self,
        base=...,  # pyright: ignore[reportMissingParameterType]
        basesrc: str = ...,
        customdata: Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] | pd.Series[float] = ...,
        customdatasrc: str = ...,
        dr=...,  # pyright: ignore[reportMissingParameterType]
        dtheta=...,  # pyright: ignore[reportMissingParameterType]
        hoverinfo: str | Sequence[str] = ...,
        hoverinfosrc: str = ...,
        hoverlabel: barpolar.Hoverlabel | dict[str, Any] = ...,
        hovertemplate: str
        | float
        | Sequence[str]
        | Sequence[float]
        | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        hovertemplatesrc: str = ...,
        hovertext: str
        | float
        | Sequence[str]
        | Sequence[float]
        | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        hovertextsrc: str = ...,
        ids: Sequence[str] | np.ndarray[tuple[int, ...], np.dtype[np.str_]] | pd.Series[str] = ...,
        idssrc: str = ...,
        legend: str = ...,
        legendgroup: str | int = ...,
        legendgrouptitle: barpolar.Legendgrouptitle | dict[str, Any] = ...,
        legendrank: int | float = ...,
        legendwidth: int | float = ...,
        marker: barpolar.Marker | dict[str, Any] = ...,
        meta: Sequence[Any] | dict[str, Any] | np.ndarray[tuple[int, ...], Any] = ...,
        metasrc: str = ...,
        name: str | int = ...,
        offset=...,  # pyright: ignore[reportMissingParameterType]
        offsetsrc: str = ...,
        opacity: int | float = ...,
        r=...,  # pyright: ignore[reportMissingParameterType]
        r0=...,  # pyright: ignore[reportMissingParameterType]
        rsrc: str = ...,
        selected: barpolar.Selected
        | dict[str, barpolar.selected.Marker | barpolar.selected.Textfont | dict[str, Any]] = ...,
        selectedpoints: Sequence[int] = ...,
        showlegend: bool = ...,
        stream: barpolar.Stream | dict[str, int | str] = ...,
        subplot=...,  # pyright: ignore[reportMissingParameterType]
        text: str | float | Sequence[str] | Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        textsrc: str = ...,
        theta=...,  # pyright: ignore[reportMissingParameterType]
        theta0=...,  # pyright: ignore[reportMissingParameterType]
        thetasrc: str = ...,
        thetaunit=...,  # pyright: ignore[reportMissingParameterType]
        uid: str | int = ...,
        uirevision: Hashable = ...,
        unselected: barpolar.Unselected
        | dict[str, barpolar.unselected.Marker | barpolar.unselected.Textfont | dict[str, Any]] = ...,
        visible: bool | str = ...,
        width=...,  # pyright: ignore[reportMissingParameterType]
        widthsrc: str = ...,
        row=...,  # pyright: ignore[reportMissingParameterType]
        col=...,  # pyright: ignore[reportMissingParameterType]
        **kwargs: Any,
    ) -> Figure: ...
    def add_box(
        self,
        alignmentgroup: str = ...,
        boxmean: bool | str = ...,
        boxpoints: bool | str = ...,
        customdata: Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] | pd.Series[float] = ...,
        customdatasrc: str = ...,
        dx: int | float = ...,
        dy: int | float = ...,
        fillcolor: str = ...,
        hoverinfo: str | Sequence[str] = ...,
        hoverinfosrc: str = ...,
        hoverlabel: box.Hoverlabel | dict[str, Any] = ...,
        hoveron: str = ...,
        hovertemplate: str
        | float
        | Sequence[str]
        | Sequence[float]
        | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        hovertemplatesrc: str = ...,
        hovertext: str
        | float
        | Sequence[str]
        | Sequence[float]
        | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        hovertextsrc: str = ...,
        ids: Sequence[str] | np.ndarray[tuple[int, ...], np.dtype[np.str_]] | pd.Series[str] = ...,
        idssrc: str = ...,
        jitter: int | float = ...,
        legend: str = ...,
        legendgroup: str | int = ...,
        legendgrouptitle: box.Legendgrouptitle | dict[str, Any] = ...,
        legendrank: int | float = ...,
        legendwidth: int | float = ...,
        line: box.Line | dict[str, str | int | float] = ...,
        lowerfence: Sequence[int]
        | Sequence[float]
        | np.ndarray[tuple[int, ...], np.dtype[np.float64]]
        | pd.Series[float] = ...,
        lowerfencesrc: str = ...,
        marker: box.Marker | dict[str, Any] = ...,
        mean: Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] | pd.Series[float] = ...,
        meansrc: str = ...,
        median: Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] | pd.Series[float] = ...,
        mediansrc: str = ...,
        meta: Sequence[Any] | dict[str, Any] | np.ndarray[tuple[int, ...], Any] = ...,
        metasrc: str = ...,
        name: str | int = ...,
        notched: bool = ...,
        notchspan: Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] | pd.Series[float] = ...,
        notchspansrc: str = ...,
        notchwidth: int | float = ...,
        offsetgroup: str | int = ...,
        opacity: int | float = ...,
        orientation: str = ...,
        pointpos: int | float = ...,
        q1: Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] | pd.Series[float] = ...,
        q1src: str = ...,
        q3: Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] | pd.Series[float] = ...,
        q3src: str = ...,
        quartilemethod: str = ...,
        sd: Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] | pd.Series[float] = ...,
        sdmultiple: int | float = ...,
        sdsrc: str = ...,
        selected: box.Selected | dict[str, box.selected.Marker | dict[str, Any]] = ...,
        selectedpoints: Sequence[int] = ...,
        showlegend: bool = ...,
        showwhiskers: bool = ...,
        sizemode: str = ...,
        stream: box.Stream | dict[str, int | str] = ...,
        text: str | float | Sequence[str] | Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        textsrc: str = ...,
        uid: str | int = ...,
        uirevision: Hashable = ...,
        unselected: box.Unselected | dict[str, box.unselected.Marker | dict[str, Any]] = ...,
        upperfence: Sequence[int]
        | Sequence[float]
        | np.ndarray[tuple[int, ...], np.dtype[np.float64]]
        | pd.Series[float] = ...,
        upperfencesrc: str = ...,
        visible: bool | str = ...,
        whiskerwidth: int | float = ...,
        width: int | float = ...,
        x: Sequence[int] | Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] | pd.Series[float] = ...,
        x0: int | float = ...,
        xaxis: str = ...,
        xcalendar: str = ...,
        xhoverformat: str = ...,
        xperiod: int | float | str = ...,
        xperiod0: int | float | str = ...,
        xperiodalignment: str = ...,
        xsrc: str = ...,
        y: Sequence[int] | Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] | pd.Series[float] = ...,
        y0: int | float = ...,
        yaxis: str = ...,
        ycalendar: str = ...,
        yhoverformat: str = ...,
        yperiod: int | float | str = ...,
        yperiod0: int | float | str = ...,
        yperiodalignment: str = ...,
        ysrc: str = ...,
        zorder: int = ...,
        row: int | str | None = ...,
        col: int | str | None = ...,
        secondary_y: bool | None = ...,
        **kwargs: Any,
    ) -> Figure: ...
    def add_candlestick(
        self,
        close=...,  # pyright: ignore[reportMissingParameterType]
        closesrc: str = ...,
        customdata: Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] | pd.Series[float] = ...,
        customdatasrc: str = ...,
        decreasing=...,  # pyright: ignore[reportMissingParameterType]
        high=...,  # pyright: ignore[reportMissingParameterType]
        highsrc: str = ...,
        hoverinfo: str | Sequence[str] = ...,
        hoverinfosrc: str = ...,
        hoverlabel: candlestick.Hoverlabel | dict[str, Any] = ...,
        hovertext: str
        | float
        | Sequence[str]
        | Sequence[float]
        | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        hovertextsrc: str = ...,
        ids: Sequence[str] | np.ndarray[tuple[int, ...], np.dtype[np.str_]] | pd.Series[str] = ...,
        idssrc: str = ...,
        increasing=...,  # pyright: ignore[reportMissingParameterType]
        legend: str = ...,
        legendgroup: str | int = ...,
        legendgrouptitle: candlestick.Legendgrouptitle | dict[str, Any] = ...,
        legendrank: int | float = ...,
        legendwidth: int | float = ...,
        line: candlestick.Line | dict[str, str | int | float] = ...,
        low=...,  # pyright: ignore[reportMissingParameterType]
        lowsrc: str = ...,
        meta: Sequence[Any] | dict[str, Any] | np.ndarray[tuple[int, ...], Any] = ...,
        metasrc: str = ...,
        name: str | int = ...,
        opacity: int | float = ...,
        open=...,  # pyright: ignore[reportMissingParameterType]
        opensrc: str = ...,
        selectedpoints: Sequence[int] = ...,
        showlegend: bool = ...,
        stream: candlestick.Stream | dict[str, int | str] = ...,
        text: str | float | Sequence[str] | Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        textsrc: str = ...,
        uid: str | int = ...,
        uirevision: Hashable = ...,
        visible: bool | str = ...,
        whiskerwidth=...,  # pyright: ignore[reportMissingParameterType]
        x=...,  # pyright: ignore[reportMissingParameterType]
        xaxis: str = ...,
        xcalendar: str = ...,
        xhoverformat: str = ...,
        xperiod: int | float | str = ...,
        xperiod0: int | float | str = ...,
        xperiodalignment: str = ...,
        xsrc: str = ...,
        yaxis: str = ...,
        yhoverformat: str = ...,
        zorder: int = ...,
        row=...,  # pyright: ignore[reportMissingParameterType]
        col=...,  # pyright: ignore[reportMissingParameterType]
        secondary_y: bool | None = ...,
        **kwargs: Any,
    ) -> Figure: ...
    def add_carpet(
        self,
        a=...,  # pyright: ignore[reportMissingParameterType]
        a0=...,  # pyright: ignore[reportMissingParameterType]
        aaxis=...,  # pyright: ignore[reportMissingParameterType]
        asrc: str = ...,
        b=...,  # pyright: ignore[reportMissingParameterType]
        b0=...,  # pyright: ignore[reportMissingParameterType]
        baxis=...,  # pyright: ignore[reportMissingParameterType]
        bsrc: str = ...,
        carpet=...,  # pyright: ignore[reportMissingParameterType]
        cheaterslope=...,  # pyright: ignore[reportMissingParameterType]
        color=...,  # pyright: ignore[reportMissingParameterType]
        customdata: Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] | pd.Series[float] = ...,
        customdatasrc: str = ...,
        da=...,  # pyright: ignore[reportMissingParameterType]
        db=...,  # pyright: ignore[reportMissingParameterType]
        font=...,  # pyright: ignore[reportMissingParameterType]
        ids: Sequence[str] | np.ndarray[tuple[int, ...], np.dtype[np.str_]] | pd.Series[str] = ...,
        idssrc: str = ...,
        legend: str = ...,
        legendgrouptitle: carpet.Legendgrouptitle | dict[str, Any] = ...,
        legendrank: int | float = ...,
        legendwidth: int | float = ...,
        meta: Sequence[Any] | dict[str, Any] | np.ndarray[tuple[int, ...], Any] = ...,
        metasrc: str = ...,
        name: str | int = ...,
        opacity: int | float = ...,
        stream: carpet.Stream | dict[str, int | str] = ...,
        uid: str | int = ...,
        uirevision: Hashable = ...,
        visible: bool | str = ...,
        x=...,  # pyright: ignore[reportMissingParameterType]
        xaxis: str = ...,
        xsrc: str = ...,
        y=...,  # pyright: ignore[reportMissingParameterType]
        yaxis: str = ...,
        ysrc: str = ...,
        zorder: int = ...,
        row=...,  # pyright: ignore[reportMissingParameterType]
        col=...,  # pyright: ignore[reportMissingParameterType]
        secondary_y: bool | None = ...,
        **kwargs: Any,
    ) -> Figure: ...
    def add_choropleth(
        self,
        autocolorscale: bool = ...,
        coloraxis: str = ...,
        colorbar: choropleth.ColorBar | dict[str, Any] = ...,
        colorscale: str | list[str] | list[tuple[float, str]] = ...,
        customdata: Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] | pd.Series[float] = ...,
        customdatasrc: str = ...,
        featureidkey=...,  # pyright: ignore[reportMissingParameterType]
        geo=...,  # pyright: ignore[reportMissingParameterType]
        geojson=...,  # pyright: ignore[reportMissingParameterType]
        hoverinfo: str | Sequence[str] = ...,
        hoverinfosrc: str = ...,
        hoverlabel: choropleth.Hoverlabel | dict[str, Any] = ...,
        hovertemplate: str
        | float
        | Sequence[str]
        | Sequence[float]
        | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        hovertemplatesrc: str = ...,
        hovertext: str
        | float
        | Sequence[str]
        | Sequence[float]
        | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        hovertextsrc: str = ...,
        ids: Sequence[str] | np.ndarray[tuple[int, ...], np.dtype[np.str_]] | pd.Series[str] = ...,
        idssrc: str = ...,
        legend: str = ...,
        legendgroup: str | int = ...,
        legendgrouptitle: choropleth.Legendgrouptitle | dict[str, Any] = ...,
        legendrank: int | float = ...,
        legendwidth: int | float = ...,
        locationmode=...,  # pyright: ignore[reportMissingParameterType]
        locations=...,  # pyright: ignore[reportMissingParameterType]
        locationssrc: str = ...,
        marker: choropleth.Marker | dict[str, Any] = ...,
        meta: Sequence[Any] | dict[str, Any] | np.ndarray[tuple[int, ...], Any] = ...,
        metasrc: str = ...,
        name: str | int = ...,
        reversescale: bool = ...,
        selected: choropleth.Selected | dict[str, choropleth.selected.Marker | dict[str, Any]] = ...,
        selectedpoints: Sequence[int] = ...,
        showlegend: bool = ...,
        showscale: bool = ...,
        stream: choropleth.Stream | dict[str, int | str] = ...,
        text: str | float | Sequence[str] | Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        textsrc: str = ...,
        uid: str | int = ...,
        uirevision: Hashable = ...,
        unselected: choropleth.Unselected | dict[str, choropleth.unselected.Marker | dict[str, Any]] = ...,
        visible: bool | str = ...,
        z=...,  # pyright: ignore[reportMissingParameterType]
        zauto: bool = ...,
        zmax: int | float = ...,
        zmid: int | float = ...,
        zmin: int | float = ...,
        zsrc: str = ...,
        row=...,  # pyright: ignore[reportMissingParameterType]
        col=...,  # pyright: ignore[reportMissingParameterType]
        **kwargs: Any,
    ) -> Figure: ...
    def add_choroplethmap(
        self,
        autocolorscale: bool = ...,
        below=...,  # pyright: ignore[reportMissingParameterType]
        coloraxis: str = ...,
        colorbar: choroplethmap.ColorBar | dict[str, Any] = ...,
        colorscale: str | list[str] | list[tuple[float, str]] = ...,
        customdata: Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] | pd.Series[float] = ...,
        customdatasrc: str = ...,
        featureidkey=...,  # pyright: ignore[reportMissingParameterType]
        geojson=...,  # pyright: ignore[reportMissingParameterType]
        hoverinfo: str | Sequence[str] = ...,
        hoverinfosrc: str = ...,
        hoverlabel: choroplethmap.Hoverlabel | dict[str, Any] = ...,
        hovertemplate: str
        | float
        | Sequence[str]
        | Sequence[float]
        | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        hovertemplatesrc: str = ...,
        hovertext: str
        | float
        | Sequence[str]
        | Sequence[float]
        | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        hovertextsrc: str = ...,
        ids: Sequence[str] | np.ndarray[tuple[int, ...], np.dtype[np.str_]] | pd.Series[str] = ...,
        idssrc: str = ...,
        legend: str = ...,
        legendgroup: str | int = ...,
        legendgrouptitle: choroplethmap.Legendgrouptitle | dict[str, Any] = ...,
        legendrank: int | float = ...,
        legendwidth: int | float = ...,
        locations=...,  # pyright: ignore[reportMissingParameterType]
        locationssrc: str = ...,
        marker: choroplethmap.Marker | dict[str, Any] = ...,
        meta: Sequence[Any] | dict[str, Any] | np.ndarray[tuple[int, ...], Any] = ...,
        metasrc: str = ...,
        name: str | int = ...,
        reversescale: bool = ...,
        selected: choroplethmap.Selected | dict[str, choroplethmap.selected.Marker | dict[str, Any]] = ...,
        selectedpoints: Sequence[int] = ...,
        showlegend: bool = ...,
        showscale: bool = ...,
        stream: choroplethmap.Stream | dict[str, int | str] = ...,
        subplot=...,  # pyright: ignore[reportMissingParameterType]
        text: str | float | Sequence[str] | Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        textsrc: str = ...,
        uid: str | int = ...,
        uirevision: Hashable = ...,
        unselected: choroplethmap.Unselected | dict[str, choroplethmap.unselected.Marker | dict[str, Any]] = ...,
        visible: bool | str = ...,
        z=...,  # pyright: ignore[reportMissingParameterType]
        zauto: bool = ...,
        zmax: int | float = ...,
        zmid: int | float = ...,
        zmin: int | float = ...,
        zsrc: str = ...,
        row=...,  # pyright: ignore[reportMissingParameterType]
        col=...,  # pyright: ignore[reportMissingParameterType]
        **kwargs: Any,
    ) -> Figure: ...
    def add_choroplethmapbox(
        self,
        autocolorscale: bool = ...,
        below=...,  # pyright: ignore[reportMissingParameterType]
        coloraxis: str = ...,
        colorbar: choroplethmapbox.ColorBar | dict[str, Any] = ...,
        colorscale: str | list[str] | list[tuple[float, str]] = ...,
        customdata: Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] | pd.Series[float] = ...,
        customdatasrc: str = ...,
        featureidkey=...,  # pyright: ignore[reportMissingParameterType]
        geojson=...,  # pyright: ignore[reportMissingParameterType]
        hoverinfo: str | Sequence[str] = ...,
        hoverinfosrc: str = ...,
        hoverlabel: choroplethmapbox.Hoverlabel | dict[str, Any] = ...,
        hovertemplate: str
        | float
        | Sequence[str]
        | Sequence[float]
        | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        hovertemplatesrc: str = ...,
        hovertext: str
        | float
        | Sequence[str]
        | Sequence[float]
        | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        hovertextsrc: str = ...,
        ids: Sequence[str] | np.ndarray[tuple[int, ...], np.dtype[np.str_]] | pd.Series[str] = ...,
        idssrc: str = ...,
        legend: str = ...,
        legendgroup: str | int = ...,
        legendgrouptitle: choroplethmapbox.Legendgrouptitle | dict[str, Any] = ...,
        legendrank: int | float = ...,
        legendwidth: int | float = ...,
        locations=...,  # pyright: ignore[reportMissingParameterType]
        locationssrc: str = ...,
        marker: choroplethmapbox.Marker | dict[str, Any] = ...,
        meta: Sequence[Any] | dict[str, Any] | np.ndarray[tuple[int, ...], Any] = ...,
        metasrc: str = ...,
        name: str | int = ...,
        reversescale: bool = ...,
        selected: choroplethmapbox.Selected | dict[str, choroplethmapbox.selected.Marker | dict[str, Any]] = ...,
        selectedpoints: Sequence[int] = ...,
        showlegend: bool = ...,
        showscale: bool = ...,
        stream: choroplethmapbox.Stream | dict[str, int | str] = ...,
        subplot=...,  # pyright: ignore[reportMissingParameterType]
        text: str | float | Sequence[str] | Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        textsrc: str = ...,
        uid: str | int = ...,
        uirevision: Hashable = ...,
        unselected: choroplethmapbox.Unselected | dict[str, choroplethmapbox.unselected.Marker | dict[str, Any]] = ...,
        visible: bool | str = ...,
        z=...,  # pyright: ignore[reportMissingParameterType]
        zauto: bool = ...,
        zmax: int | float = ...,
        zmid: int | float = ...,
        zmin: int | float = ...,
        zsrc: str = ...,
        row=...,  # pyright: ignore[reportMissingParameterType]
        col=...,  # pyright: ignore[reportMissingParameterType]
        **kwargs: Any,
    ) -> Figure: ...
    def add_cone(
        self,
        anchor=...,  # pyright: ignore[reportMissingParameterType]
        autocolorscale: bool = ...,
        cauto: bool = ...,
        cmax: int | float = ...,
        cmid: int | float = ...,
        cmin: int | float = ...,
        coloraxis: str = ...,
        colorbar: cone.ColorBar | dict[str, Any] = ...,
        colorscale: str | list[str] | list[tuple[float, str]] = ...,
        customdata: Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] | pd.Series[float] = ...,
        customdatasrc: str = ...,
        hoverinfo: str | Sequence[str] = ...,
        hoverinfosrc: str = ...,
        hoverlabel: cone.Hoverlabel | dict[str, Any] = ...,
        hovertemplate: str
        | float
        | Sequence[str]
        | Sequence[float]
        | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        hovertemplatesrc: str = ...,
        hovertext: str
        | float
        | Sequence[str]
        | Sequence[float]
        | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        hovertextsrc: str = ...,
        ids: Sequence[str] | np.ndarray[tuple[int, ...], np.dtype[np.str_]] | pd.Series[str] = ...,
        idssrc: str = ...,
        legend: str = ...,
        legendgroup: str | int = ...,
        legendgrouptitle: cone.Legendgrouptitle | dict[str, Any] = ...,
        legendrank: int | float = ...,
        legendwidth: int | float = ...,
        lighting: cone.Lighting | dict[str, Any] = ...,
        lightposition: cone.Lightposition
        | dict[str, Sequence[int] | Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]]] = ...,
        meta: Sequence[Any] | dict[str, Any] | np.ndarray[tuple[int, ...], Any] = ...,
        metasrc: str = ...,
        name: str | int = ...,
        opacity: int | float = ...,
        reversescale: bool = ...,
        scene: str = ...,
        showlegend: bool = ...,
        showscale: bool = ...,
        sizemode: str = ...,
        sizeref=...,  # pyright: ignore[reportMissingParameterType]
        stream: cone.Stream | dict[str, int | str] = ...,
        text: str | float | Sequence[str] | Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        textsrc: str = ...,
        u=...,  # pyright: ignore[reportMissingParameterType]
        uhoverformat: str = ...,
        uid: str | int = ...,
        uirevision: Hashable = ...,
        usrc: str = ...,
        v=...,  # pyright: ignore[reportMissingParameterType]
        vhoverformat: str = ...,
        visible: bool | str = ...,
        vsrc: str = ...,
        w=...,  # pyright: ignore[reportMissingParameterType]
        whoverformat: str = ...,
        wsrc: str = ...,
        x=...,  # pyright: ignore[reportMissingParameterType]
        xhoverformat: str = ...,
        xsrc: str = ...,
        y=...,  # pyright: ignore[reportMissingParameterType]
        yhoverformat: str = ...,
        ysrc: str = ...,
        z=...,  # pyright: ignore[reportMissingParameterType]
        zhoverformat: str = ...,
        zsrc: str = ...,
        row=...,  # pyright: ignore[reportMissingParameterType]
        col=...,  # pyright: ignore[reportMissingParameterType]
        **kwargs: Any,
    ) -> Figure: ...
    def add_contour(
        self,
        autocolorscale: bool = ...,
        autocontour: bool = ...,
        coloraxis: str = ...,
        colorbar: contour.ColorBar | dict[str, Any] = ...,
        colorscale: str | list[str] | list[tuple[float, str]] = ...,
        connectgaps: bool = ...,
        contours: contour.Contours | dict[str, Any] = ...,
        customdata: Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] | pd.Series[float] = ...,
        customdatasrc: str = ...,
        dx: int | float = ...,
        dy: int | float = ...,
        fillcolor: str = ...,
        hoverinfo: str | Sequence[str] = ...,
        hoverinfosrc: str = ...,
        hoverlabel: contour.Hoverlabel | dict[str, Any] = ...,
        hoverongaps: bool = ...,
        hovertemplate: str
        | float
        | Sequence[str]
        | Sequence[float]
        | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        hovertemplatesrc: str = ...,
        hovertext: str
        | float
        | Sequence[str]
        | Sequence[float]
        | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        hovertextsrc: str = ...,
        ids: Sequence[str] | np.ndarray[tuple[int, ...], np.dtype[np.str_]] | pd.Series[str] = ...,
        idssrc: str = ...,
        legend: str = ...,
        legendgroup: str | int = ...,
        legendgrouptitle: contour.Legendgrouptitle | dict[str, Any] = ...,
        legendrank: int | float = ...,
        legendwidth: int | float = ...,
        line: contour.Line | dict[str, str | int | float] = ...,
        meta: Sequence[Any] | dict[str, Any] | np.ndarray[tuple[int, ...], Any] = ...,
        metasrc: str = ...,
        name: str | int = ...,
        ncontours: int = ...,
        opacity: int | float = ...,
        reversescale: bool = ...,
        showlegend: bool = ...,
        showscale: bool = ...,
        stream: contour.Stream | dict[str, int | str] = ...,
        text: str | float | Sequence[str] | Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        textfont: contour.Textfont | dict[str, Any] = ...,
        textsrc: str = ...,
        texttemplate: str = ...,
        transpose: bool = ...,
        uid: str | int = ...,
        uirevision: Hashable = ...,
        visible: bool | str = ...,
        x: Sequence[int] | Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] | pd.Series[float] = ...,
        x0: int | float = ...,
        xaxis: str = ...,
        xcalendar: str = ...,
        xhoverformat: str = ...,
        xperiod: int | float | str = ...,
        xperiod0: int | float | str = ...,
        xperiodalignment: str = ...,
        xsrc: str = ...,
        xtype: str = ...,
        y: Sequence[int] | Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] | pd.Series[float] = ...,
        y0: int | float = ...,
        yaxis: str = ...,
        ycalendar: str = ...,
        yhoverformat: str = ...,
        yperiod: int | float | str = ...,
        yperiod0: int | float | str = ...,
        yperiodalignment: str = ...,
        ysrc: str = ...,
        ytype: str = ...,
        z: Sequence[int] | Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] | pd.Series[float] = ...,
        zauto: bool = ...,
        zhoverformat: str = ...,
        zmax: int | float = ...,
        zmid: int | float = ...,
        zmin: int | float = ...,
        zorder: int = ...,
        zsrc: str = ...,
        row: int | str | None = ...,
        col: int | str | None = ...,
        secondary_y: bool | None = ...,
        **kwargs: Any,
    ) -> Figure: ...
    def add_contourcarpet(
        self,
        a=...,  # pyright: ignore[reportMissingParameterType]
        a0=...,  # pyright: ignore[reportMissingParameterType]
        asrc: str = ...,
        atype=...,  # pyright: ignore[reportMissingParameterType]
        autocolorscale: bool = ...,
        autocontour: bool = ...,
        b=...,  # pyright: ignore[reportMissingParameterType]
        b0=...,  # pyright: ignore[reportMissingParameterType]
        bsrc: str = ...,
        btype=...,  # pyright: ignore[reportMissingParameterType]
        carpet=...,  # pyright: ignore[reportMissingParameterType]
        coloraxis: str = ...,
        colorbar: contourcarpet.ColorBar | dict[str, Any] = ...,
        colorscale: str | list[str] | list[tuple[float, str]] = ...,
        contours: contourcarpet.Contours | dict[str, Any] = ...,
        customdata: Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] | pd.Series[float] = ...,
        customdatasrc: str = ...,
        da=...,  # pyright: ignore[reportMissingParameterType]
        db=...,  # pyright: ignore[reportMissingParameterType]
        fillcolor: str = ...,
        hovertext: str
        | float
        | Sequence[str]
        | Sequence[float]
        | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        hovertextsrc: str = ...,
        ids: Sequence[str] | np.ndarray[tuple[int, ...], np.dtype[np.str_]] | pd.Series[str] = ...,
        idssrc: str = ...,
        legend: str = ...,
        legendgroup: str | int = ...,
        legendgrouptitle: contourcarpet.Legendgrouptitle | dict[str, Any] = ...,
        legendrank: int | float = ...,
        legendwidth: int | float = ...,
        line: contourcarpet.Line | dict[str, str | int | float] = ...,
        meta: Sequence[Any] | dict[str, Any] | np.ndarray[tuple[int, ...], Any] = ...,
        metasrc: str = ...,
        name: str | int = ...,
        ncontours: int = ...,
        opacity: int | float = ...,
        reversescale: bool = ...,
        showlegend: bool = ...,
        showscale: bool = ...,
        stream: contourcarpet.Stream | dict[str, int | str] = ...,
        text: str | float | Sequence[str] | Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        textsrc: str = ...,
        transpose: bool = ...,
        uid: str | int = ...,
        uirevision: Hashable = ...,
        visible: bool | str = ...,
        xaxis: str = ...,
        yaxis: str = ...,
        z=...,  # pyright: ignore[reportMissingParameterType]
        zauto: bool = ...,
        zmax: int | float = ...,
        zmid: int | float = ...,
        zmin: int | float = ...,
        zorder: int = ...,
        zsrc: str = ...,
        row=...,  # pyright: ignore[reportMissingParameterType]
        col=...,  # pyright: ignore[reportMissingParameterType]
        secondary_y: bool | None = ...,
        **kwargs: Any,
    ) -> Figure: ...
    def add_densitymap(
        self,
        autocolorscale: bool = ...,
        below=...,  # pyright: ignore[reportMissingParameterType]
        coloraxis: str = ...,
        colorbar: densitymap.ColorBar | dict[str, Any] = ...,
        colorscale: str | list[str] | list[tuple[float, str]] = ...,
        customdata: Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] | pd.Series[float] = ...,
        customdatasrc: str = ...,
        hoverinfo: str | Sequence[str] = ...,
        hoverinfosrc: str = ...,
        hoverlabel: densitymap.Hoverlabel | dict[str, Any] = ...,
        hovertemplate: str
        | float
        | Sequence[str]
        | Sequence[float]
        | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        hovertemplatesrc: str = ...,
        hovertext: str
        | float
        | Sequence[str]
        | Sequence[float]
        | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        hovertextsrc: str = ...,
        ids: Sequence[str] | np.ndarray[tuple[int, ...], np.dtype[np.str_]] | pd.Series[str] = ...,
        idssrc: str = ...,
        lat=...,  # pyright: ignore[reportMissingParameterType]
        latsrc: str = ...,
        legend: str = ...,
        legendgroup: str | int = ...,
        legendgrouptitle: densitymap.Legendgrouptitle | dict[str, Any] = ...,
        legendrank: int | float = ...,
        legendwidth: int | float = ...,
        lon=...,  # pyright: ignore[reportMissingParameterType]
        lonsrc: str = ...,
        meta: Sequence[Any] | dict[str, Any] | np.ndarray[tuple[int, ...], Any] = ...,
        metasrc: str = ...,
        name: str | int = ...,
        opacity: int | float = ...,
        radius=...,  # pyright: ignore[reportMissingParameterType]
        radiussrc: str = ...,
        reversescale: bool = ...,
        showlegend: bool = ...,
        showscale: bool = ...,
        stream: densitymap.Stream | dict[str, int | str] = ...,
        subplot=...,  # pyright: ignore[reportMissingParameterType]
        text: str | float | Sequence[str] | Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        textsrc: str = ...,
        uid: str | int = ...,
        uirevision: Hashable = ...,
        visible: bool | str = ...,
        z=...,  # pyright: ignore[reportMissingParameterType]
        zauto: bool = ...,
        zmax: int | float = ...,
        zmid: int | float = ...,
        zmin: int | float = ...,
        zsrc: str = ...,
        row=...,  # pyright: ignore[reportMissingParameterType]
        col=...,  # pyright: ignore[reportMissingParameterType]
        **kwargs: Any,
    ) -> Figure: ...
    def add_densitymapbox(
        self,
        autocolorscale: bool = ...,
        below=...,  # pyright: ignore[reportMissingParameterType]
        coloraxis: str = ...,
        colorbar: densitymapbox.ColorBar | dict[str, Any] = ...,
        colorscale: str | list[str] | list[tuple[float, str]] = ...,
        customdata: Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] | pd.Series[float] = ...,
        customdatasrc: str = ...,
        hoverinfo: str | Sequence[str] = ...,
        hoverinfosrc: str = ...,
        hoverlabel: densitymapbox.Hoverlabel | dict[str, Any] = ...,
        hovertemplate: str
        | float
        | Sequence[str]
        | Sequence[float]
        | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        hovertemplatesrc: str = ...,
        hovertext: str
        | float
        | Sequence[str]
        | Sequence[float]
        | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        hovertextsrc: str = ...,
        ids: Sequence[str] | np.ndarray[tuple[int, ...], np.dtype[np.str_]] | pd.Series[str] = ...,
        idssrc: str = ...,
        lat=...,  # pyright: ignore[reportMissingParameterType]
        latsrc: str = ...,
        legend: str = ...,
        legendgroup: str | int = ...,
        legendgrouptitle: densitymapbox.Legendgrouptitle | dict[str, Any] = ...,
        legendrank: int | float = ...,
        legendwidth: int | float = ...,
        lon=...,  # pyright: ignore[reportMissingParameterType]
        lonsrc: str = ...,
        meta: Sequence[Any] | dict[str, Any] | np.ndarray[tuple[int, ...], Any] = ...,
        metasrc: str = ...,
        name: str | int = ...,
        opacity: int | float = ...,
        radius=...,  # pyright: ignore[reportMissingParameterType]
        radiussrc: str = ...,
        reversescale: bool = ...,
        showlegend: bool = ...,
        showscale: bool = ...,
        stream: densitymapbox.Stream | dict[str, int | str] = ...,
        subplot=...,  # pyright: ignore[reportMissingParameterType]
        text: str | float | Sequence[str] | Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        textsrc: str = ...,
        uid: str | int = ...,
        uirevision: Hashable = ...,
        visible: bool | str = ...,
        z=...,  # pyright: ignore[reportMissingParameterType]
        zauto: bool = ...,
        zmax: int | float = ...,
        zmid: int | float = ...,
        zmin: int | float = ...,
        zsrc: str = ...,
        row=...,  # pyright: ignore[reportMissingParameterType]
        col=...,  # pyright: ignore[reportMissingParameterType]
        **kwargs: Any,
    ) -> Figure: ...
    def add_funnel(
        self,
        alignmentgroup: str | int = ...,
        cliponaxis: bool = ...,
        connector=...,  # pyright: ignore[reportMissingParameterType]
        constraintext=...,  # pyright: ignore[reportMissingParameterType]
        customdata: Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] | pd.Series[float] = ...,
        customdatasrc: str = ...,
        dx: int | float = ...,
        dy: int | float = ...,
        hoverinfo: str | Sequence[str] = ...,
        hoverinfosrc: str = ...,
        hoverlabel: funnel.Hoverlabel | dict[str, Any] = ...,
        hovertemplate: str
        | float
        | Sequence[str]
        | Sequence[float]
        | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        hovertemplatesrc: str = ...,
        hovertext: str
        | float
        | Sequence[str]
        | Sequence[float]
        | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        hovertextsrc: str = ...,
        ids: Sequence[str] | np.ndarray[tuple[int, ...], np.dtype[np.str_]] | pd.Series[str] = ...,
        idssrc: str = ...,
        insidetextanchor=...,  # pyright: ignore[reportMissingParameterType]
        insidetextfont=...,  # pyright: ignore[reportMissingParameterType]
        legend: str = ...,
        legendgroup: str | int = ...,
        legendgrouptitle: funnel.Legendgrouptitle | dict[str, Any] = ...,
        legendrank: int | float = ...,
        legendwidth: int | float = ...,
        marker: funnel.Marker | dict[str, Any] = ...,
        meta: Sequence[Any] | dict[str, Any] | np.ndarray[tuple[int, ...], Any] = ...,
        metasrc: str = ...,
        name: str | int = ...,
        offset=...,  # pyright: ignore[reportMissingParameterType]
        offsetgroup: str | int = ...,
        opacity: int | float = ...,
        orientation: str = ...,
        outsidetextfont=...,  # pyright: ignore[reportMissingParameterType]
        selectedpoints: Sequence[int] = ...,
        showlegend: bool = ...,
        stream: funnel.Stream | dict[str, int | str] = ...,
        text: str | float | Sequence[str] | Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        textangle: int | float = ...,
        textfont: funnel.Textfont | dict[str, Any] = ...,
        textinfo=...,  # pyright: ignore[reportMissingParameterType]
        textposition: str | Sequence[str] | np.ndarray[tuple[int, ...], np.dtype[np.str_]] = ...,
        textpositionsrc: str = ...,
        textsrc: str = ...,
        texttemplate: str = ...,
        texttemplatesrc: str = ...,
        uid: str | int = ...,
        uirevision: Hashable = ...,
        visible: bool | str = ...,
        width=...,  # pyright: ignore[reportMissingParameterType]
        x=...,  # pyright: ignore[reportMissingParameterType]
        x0: int | float = ...,
        xaxis: str = ...,
        xhoverformat: str = ...,
        xperiod: int | float | str = ...,
        xperiod0: int | float | str = ...,
        xperiodalignment: str = ...,
        xsrc: str = ...,
        y=...,  # pyright: ignore[reportMissingParameterType]
        y0: int | float = ...,
        yaxis: str = ...,
        yhoverformat: str = ...,
        yperiod: int | float | str = ...,
        yperiod0: int | float | str = ...,
        yperiodalignment: str = ...,
        ysrc: str = ...,
        zorder: int = ...,
        row=...,  # pyright: ignore[reportMissingParameterType]
        col=...,  # pyright: ignore[reportMissingParameterType]
        secondary_y: bool | None = ...,
        **kwargs: Any,
    ) -> Figure: ...
    def add_funnelarea(
        self,
        aspectratio=...,  # pyright: ignore[reportMissingParameterType]
        baseratio=...,  # pyright: ignore[reportMissingParameterType]
        customdata: Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] | pd.Series[float] = ...,
        customdatasrc: str = ...,
        dlabel=...,  # pyright: ignore[reportMissingParameterType]
        domain=...,  # pyright: ignore[reportMissingParameterType]
        hoverinfo: str | Sequence[str] = ...,
        hoverinfosrc: str = ...,
        hoverlabel: funnelarea.Hoverlabel | dict[str, Any] = ...,
        hovertemplate: str
        | float
        | Sequence[str]
        | Sequence[float]
        | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        hovertemplatesrc: str = ...,
        hovertext: str
        | float
        | Sequence[str]
        | Sequence[float]
        | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        hovertextsrc: str = ...,
        ids: Sequence[str] | np.ndarray[tuple[int, ...], np.dtype[np.str_]] | pd.Series[str] = ...,
        idssrc: str = ...,
        insidetextfont=...,  # pyright: ignore[reportMissingParameterType]
        label0=...,  # pyright: ignore[reportMissingParameterType]
        labels=...,  # pyright: ignore[reportMissingParameterType]
        labelssrc: str = ...,
        legend: str = ...,
        legendgroup: str | int = ...,
        legendgrouptitle: funnelarea.Legendgrouptitle | dict[str, Any] = ...,
        legendrank: int | float = ...,
        legendwidth: int | float = ...,
        marker: funnelarea.Marker | dict[str, Any] = ...,
        meta: Sequence[Any] | dict[str, Any] | np.ndarray[tuple[int, ...], Any] = ...,
        metasrc: str = ...,
        name: str | int = ...,
        opacity: int | float = ...,
        scalegroup=...,  # pyright: ignore[reportMissingParameterType]
        showlegend: bool = ...,
        stream: funnelarea.Stream | dict[str, int | str] = ...,
        text: str | float | Sequence[str] | Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        textfont: funnelarea.Textfont | dict[str, Any] = ...,
        textinfo=...,  # pyright: ignore[reportMissingParameterType]
        textposition: str | Sequence[str] | np.ndarray[tuple[int, ...], np.dtype[np.str_]] = ...,
        textpositionsrc: str = ...,
        textsrc: str = ...,
        texttemplate: str = ...,
        texttemplatesrc: str = ...,
        title=...,  # pyright: ignore[reportMissingParameterType]
        uid: str | int = ...,
        uirevision: Hashable = ...,
        values=...,  # pyright: ignore[reportMissingParameterType]
        valuessrc: str = ...,
        visible: bool | str = ...,
        row=...,  # pyright: ignore[reportMissingParameterType]
        col=...,  # pyright: ignore[reportMissingParameterType]
        **kwargs: Any,
    ) -> Figure: ...
    def add_heatmap(
        self,
        autocolorscale: bool = ...,
        coloraxis: str = ...,
        colorbar: heatmap.ColorBar | dict[str, Any] = ...,
        colorscale: str | list[str] | list[tuple[float, str]] = ...,
        connectgaps: bool = ...,
        customdata: Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] | pd.Series[float] = ...,
        customdatasrc: str = ...,
        dx: int | float = ...,
        dy: int | float = ...,
        hoverinfo: str | Sequence[str] = ...,
        hoverinfosrc: str = ...,
        hoverlabel: heatmap.Hoverlabel | dict[str, Any] = ...,
        hoverongaps: bool = ...,
        hovertemplate: str
        | float
        | Sequence[str]
        | Sequence[float]
        | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        hovertemplatesrc: str = ...,
        hovertext: str
        | float
        | Sequence[str]
        | Sequence[float]
        | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        hovertextsrc: str = ...,
        ids: Sequence[str] | np.ndarray[tuple[int, ...], np.dtype[np.str_]] | pd.Series[str] = ...,
        idssrc: str = ...,
        legend: str = ...,
        legendgroup: str | int = ...,
        legendgrouptitle: heatmap.Legendgrouptitle | dict[str, Any] = ...,
        legendrank: int | float = ...,
        legendwidth: int | float = ...,
        meta: Sequence[Any] | dict[str, Any] | np.ndarray[tuple[int, ...], Any] = ...,
        metasrc: str = ...,
        name: str | int = ...,
        opacity: int | float = ...,
        reversescale: bool = ...,
        showlegend: bool = ...,
        showscale: bool = ...,
        stream: heatmap.Stream | dict[str, int | str] = ...,
        text: str | float | Sequence[str] | Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        textfont: heatmap.Textfont | dict[str, Any] = ...,
        textsrc: str = ...,
        texttemplate: str = ...,
        transpose: bool = ...,
        uid: str | int = ...,
        uirevision: Hashable = ...,
        visible: bool | str = ...,
        x: Sequence[int] | Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] | pd.Series[float] = ...,
        x0: int | float = ...,
        xaxis: str = ...,
        xcalendar: str = ...,
        xgap: int | float = ...,
        xhoverformat: str = ...,
        xperiod: int | float | str = ...,
        xperiod0: int | float | str = ...,
        xperiodalignment: str = ...,
        xsrc: str = ...,
        xtype: str = ...,
        y: Sequence[int] | Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] | pd.Series[float] = ...,
        y0: int | float = ...,
        yaxis: str = ...,
        ycalendar: str = ...,
        ygap: int | float = ...,
        yhoverformat: str = ...,
        yperiod: int | float | str = ...,
        yperiod0: int | float | str = ...,
        yperiodalignment: str = ...,
        ysrc: str = ...,
        ytype: str = ...,
        z: Sequence[int] | Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] | pd.Series[float] = ...,
        zauto: bool = ...,
        zhoverformat: str = ...,
        zmax: int | float = ...,
        zmid: int | float = ...,
        zmin: int | float = ...,
        zorder: int = ...,
        zsmooth: str | bool = ...,
        zsrc: str = ...,
        row: int | str | None = ...,
        col: int | str | None = ...,
        secondary_y: bool | None = ...,
        **kwargs: Any,
    ) -> Figure: ...
    def add_histogram(
        self,
        alignmentgroup: str | int = ...,
        autobinx=...,  # pyright: ignore[reportMissingParameterType]
        autobiny=...,  # pyright: ignore[reportMissingParameterType]
        bingroup=...,  # pyright: ignore[reportMissingParameterType]
        cliponaxis: bool = ...,
        constraintext=...,  # pyright: ignore[reportMissingParameterType]
        cumulative=...,  # pyright: ignore[reportMissingParameterType]
        customdata: Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] | pd.Series[float] = ...,
        customdatasrc: str = ...,
        error_x: histogram.ErrorX | dict[str, Any] = ...,
        error_y: histogram.ErrorY | dict[str, Any] = ...,
        histfunc=...,  # pyright: ignore[reportMissingParameterType]
        histnorm=...,  # pyright: ignore[reportMissingParameterType]
        hoverinfo: str | Sequence[str] = ...,
        hoverinfosrc: str = ...,
        hoverlabel: histogram.Hoverlabel | dict[str, Any] = ...,
        hovertemplate: str
        | float
        | Sequence[str]
        | Sequence[float]
        | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        hovertemplatesrc: str = ...,
        hovertext: str
        | float
        | Sequence[str]
        | Sequence[float]
        | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        hovertextsrc: str = ...,
        ids: Sequence[str] | np.ndarray[tuple[int, ...], np.dtype[np.str_]] | pd.Series[str] = ...,
        idssrc: str = ...,
        insidetextanchor=...,  # pyright: ignore[reportMissingParameterType]
        insidetextfont=...,  # pyright: ignore[reportMissingParameterType]
        legend: str = ...,
        legendgroup: str | int = ...,
        legendgrouptitle: histogram.Legendgrouptitle | dict[str, Any] = ...,
        legendrank: int | float = ...,
        legendwidth: int | float = ...,
        marker: histogram.Marker | dict[str, Any] = ...,
        meta: Sequence[Any] | dict[str, Any] | np.ndarray[tuple[int, ...], Any] = ...,
        metasrc: str = ...,
        name: str | int = ...,
        nbinsx=...,  # pyright: ignore[reportMissingParameterType]
        nbinsy=...,  # pyright: ignore[reportMissingParameterType]
        offsetgroup: str | int = ...,
        opacity: int | float = ...,
        orientation: str = ...,
        outsidetextfont=...,  # pyright: ignore[reportMissingParameterType]
        selected: histogram.Selected
        | dict[str, histogram.selected.Marker | histogram.selected.Textfont | dict[str, Any]] = ...,
        selectedpoints: Sequence[int] = ...,
        showlegend: bool = ...,
        stream: histogram.Stream | dict[str, int | str] = ...,
        text: str | float | Sequence[str] | Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        textangle: int | float = ...,
        textfont: histogram.Textfont | dict[str, Any] = ...,
        textposition: str | Sequence[str] | np.ndarray[tuple[int, ...], np.dtype[np.str_]] = ...,
        textsrc: str = ...,
        texttemplate: str = ...,
        uid: str | int = ...,
        uirevision: Hashable = ...,
        unselected: histogram.Unselected
        | dict[str, histogram.unselected.Marker | histogram.unselected.Textfont | dict[str, Any]] = ...,
        visible: bool | str = ...,
        x=...,  # pyright: ignore[reportMissingParameterType]
        xaxis: str = ...,
        xbins=...,  # pyright: ignore[reportMissingParameterType]
        xcalendar: str = ...,
        xhoverformat: str = ...,
        xsrc: str = ...,
        y=...,  # pyright: ignore[reportMissingParameterType]
        yaxis: str = ...,
        ybins=...,  # pyright: ignore[reportMissingParameterType]
        ycalendar: str = ...,
        yhoverformat: str = ...,
        ysrc: str = ...,
        zorder: int = ...,
        row=...,  # pyright: ignore[reportMissingParameterType]
        col=...,  # pyright: ignore[reportMissingParameterType]
        secondary_y: bool | None = ...,
        **kwargs: Any,
    ) -> Figure: ...
    def add_histogram2d(
        self,
        autobinx=...,  # pyright: ignore[reportMissingParameterType]
        autobiny=...,  # pyright: ignore[reportMissingParameterType]
        autocolorscale: bool = ...,
        bingroup=...,  # pyright: ignore[reportMissingParameterType]
        coloraxis: str = ...,
        colorbar: histogram2d.ColorBar | dict[str, Any] = ...,
        colorscale: str | list[str] | list[tuple[float, str]] = ...,
        customdata: Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] | pd.Series[float] = ...,
        customdatasrc: str = ...,
        histfunc=...,  # pyright: ignore[reportMissingParameterType]
        histnorm=...,  # pyright: ignore[reportMissingParameterType]
        hoverinfo: str | Sequence[str] = ...,
        hoverinfosrc: str = ...,
        hoverlabel: histogram2d.Hoverlabel | dict[str, Any] = ...,
        hovertemplate: str
        | float
        | Sequence[str]
        | Sequence[float]
        | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        hovertemplatesrc: str = ...,
        ids: Sequence[str] | np.ndarray[tuple[int, ...], np.dtype[np.str_]] | pd.Series[str] = ...,
        idssrc: str = ...,
        legend: str = ...,
        legendgroup: str | int = ...,
        legendgrouptitle: histogram2d.Legendgrouptitle | dict[str, Any] = ...,
        legendrank: int | float = ...,
        legendwidth: int | float = ...,
        marker: histogram2d.Marker | dict[str, Any] = ...,
        meta: Sequence[Any] | dict[str, Any] | np.ndarray[tuple[int, ...], Any] = ...,
        metasrc: str = ...,
        name: str | int = ...,
        nbinsx=...,  # pyright: ignore[reportMissingParameterType]
        nbinsy=...,  # pyright: ignore[reportMissingParameterType]
        opacity: int | float = ...,
        reversescale: bool = ...,
        showlegend: bool = ...,
        showscale: bool = ...,
        stream: histogram2d.Stream | dict[str, int | str] = ...,
        textfont: histogram2d.Textfont | dict[str, Any] = ...,
        texttemplate: str = ...,
        uid: str | int = ...,
        uirevision: Hashable = ...,
        visible: bool | str = ...,
        x=...,  # pyright: ignore[reportMissingParameterType]
        xaxis: str = ...,
        xbingroup=...,  # pyright: ignore[reportMissingParameterType]
        xbins=...,  # pyright: ignore[reportMissingParameterType]
        xcalendar: str = ...,
        xgap: int | float = ...,
        xhoverformat: str = ...,
        xsrc: str = ...,
        y=...,  # pyright: ignore[reportMissingParameterType]
        yaxis: str = ...,
        ybingroup=...,  # pyright: ignore[reportMissingParameterType]
        ybins=...,  # pyright: ignore[reportMissingParameterType]
        ycalendar: str = ...,
        ygap: int | float = ...,
        yhoverformat: str = ...,
        ysrc: str = ...,
        z=...,  # pyright: ignore[reportMissingParameterType]
        zauto: bool = ...,
        zhoverformat: str = ...,
        zmax: int | float = ...,
        zmid: int | float = ...,
        zmin: int | float = ...,
        zsmooth: str | bool = ...,
        zsrc: str = ...,
        row=...,  # pyright: ignore[reportMissingParameterType]
        col=...,  # pyright: ignore[reportMissingParameterType]
        secondary_y: bool | None = ...,
        **kwargs: Any,
    ) -> Figure: ...
    def add_histogram2dcontour(
        self,
        autobinx=...,  # pyright: ignore[reportMissingParameterType]
        autobiny=...,  # pyright: ignore[reportMissingParameterType]
        autocolorscale: bool = ...,
        autocontour: bool = ...,
        bingroup=...,  # pyright: ignore[reportMissingParameterType]
        coloraxis: str = ...,
        colorbar: histogram2dcontour.ColorBar | dict[str, Any] = ...,
        colorscale: str | list[str] | list[tuple[float, str]] = ...,
        contours: histogram2dcontour.Contours | dict[str, Any] = ...,
        customdata: Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] | pd.Series[float] = ...,
        customdatasrc: str = ...,
        histfunc=...,  # pyright: ignore[reportMissingParameterType]
        histnorm=...,  # pyright: ignore[reportMissingParameterType]
        hoverinfo: str | Sequence[str] = ...,
        hoverinfosrc: str = ...,
        hoverlabel: histogram2dcontour.Hoverlabel | dict[str, Any] = ...,
        hovertemplate: str
        | float
        | Sequence[str]
        | Sequence[float]
        | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        hovertemplatesrc: str = ...,
        ids: Sequence[str] | np.ndarray[tuple[int, ...], np.dtype[np.str_]] | pd.Series[str] = ...,
        idssrc: str = ...,
        legend: str = ...,
        legendgroup: str | int = ...,
        legendgrouptitle: histogram2dcontour.Legendgrouptitle | dict[str, Any] = ...,
        legendrank: int | float = ...,
        legendwidth: int | float = ...,
        line: histogram2dcontour.Line | dict[str, str | int | float] = ...,
        marker: histogram2dcontour.Marker | dict[str, Any] = ...,
        meta: Sequence[Any] | dict[str, Any] | np.ndarray[tuple[int, ...], Any] = ...,
        metasrc: str = ...,
        name: str | int = ...,
        nbinsx=...,  # pyright: ignore[reportMissingParameterType]
        nbinsy=...,  # pyright: ignore[reportMissingParameterType]
        ncontours: int = ...,
        opacity: int | float = ...,
        reversescale: bool = ...,
        showlegend: bool = ...,
        showscale: bool = ...,
        stream: histogram2dcontour.Stream | dict[str, int | str] = ...,
        textfont: histogram2dcontour.Textfont | dict[str, Any] = ...,
        texttemplate: str = ...,
        uid: str | int = ...,
        uirevision: Hashable = ...,
        visible: bool | str = ...,
        x=...,  # pyright: ignore[reportMissingParameterType]
        xaxis: str = ...,
        xbingroup=...,  # pyright: ignore[reportMissingParameterType]
        xbins=...,  # pyright: ignore[reportMissingParameterType]
        xcalendar: str = ...,
        xhoverformat: str = ...,
        xsrc: str = ...,
        y=...,  # pyright: ignore[reportMissingParameterType]
        yaxis: str = ...,
        ybingroup=...,  # pyright: ignore[reportMissingParameterType]
        ybins=...,  # pyright: ignore[reportMissingParameterType]
        ycalendar: str = ...,
        yhoverformat: str = ...,
        ysrc: str = ...,
        z=...,  # pyright: ignore[reportMissingParameterType]
        zauto: bool = ...,
        zhoverformat: str = ...,
        zmax: int | float = ...,
        zmid: int | float = ...,
        zmin: int | float = ...,
        zsrc: str = ...,
        row=...,  # pyright: ignore[reportMissingParameterType]
        col=...,  # pyright: ignore[reportMissingParameterType]
        secondary_y: bool | None = ...,
        **kwargs: Any,
    ) -> Figure: ...
    def add_icicle(
        self,
        branchvalues=...,  # pyright: ignore[reportMissingParameterType]
        count=...,  # pyright: ignore[reportMissingParameterType]
        customdata: Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] | pd.Series[float] = ...,
        customdatasrc: str = ...,
        domain=...,  # pyright: ignore[reportMissingParameterType]
        hoverinfo: str | Sequence[str] = ...,
        hoverinfosrc: str = ...,
        hoverlabel: icicle.Hoverlabel | dict[str, Any] = ...,
        hovertemplate: str
        | float
        | Sequence[str]
        | Sequence[float]
        | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        hovertemplatesrc: str = ...,
        hovertext: str
        | float
        | Sequence[str]
        | Sequence[float]
        | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        hovertextsrc: str = ...,
        ids: Sequence[str] | np.ndarray[tuple[int, ...], np.dtype[np.str_]] | pd.Series[str] = ...,
        idssrc: str = ...,
        insidetextfont=...,  # pyright: ignore[reportMissingParameterType]
        labels=...,  # pyright: ignore[reportMissingParameterType]
        labelssrc: str = ...,
        leaf=...,  # pyright: ignore[reportMissingParameterType]
        legend: str = ...,
        legendgrouptitle: icicle.Legendgrouptitle | dict[str, Any] = ...,
        legendrank: int | float = ...,
        legendwidth: int | float = ...,
        level=...,  # pyright: ignore[reportMissingParameterType]
        marker: icicle.Marker | dict[str, Any] = ...,
        maxdepth=...,  # pyright: ignore[reportMissingParameterType]
        meta: Sequence[Any] | dict[str, Any] | np.ndarray[tuple[int, ...], Any] = ...,
        metasrc: str = ...,
        name: str | int = ...,
        opacity: int | float = ...,
        outsidetextfont=...,  # pyright: ignore[reportMissingParameterType]
        parents=...,  # pyright: ignore[reportMissingParameterType]
        parentssrc: str = ...,
        pathbar=...,  # pyright: ignore[reportMissingParameterType]
        root=...,  # pyright: ignore[reportMissingParameterType]
        sort=...,  # pyright: ignore[reportMissingParameterType]
        stream: icicle.Stream | dict[str, int | str] = ...,
        text: str | float | Sequence[str] | Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        textfont: icicle.Textfont | dict[str, Any] = ...,
        textinfo=...,  # pyright: ignore[reportMissingParameterType]
        textposition: str | Sequence[str] | np.ndarray[tuple[int, ...], np.dtype[np.str_]] = ...,
        textsrc: str = ...,
        texttemplate: str = ...,
        texttemplatesrc: str = ...,
        tiling=...,  # pyright: ignore[reportMissingParameterType]
        uid: str | int = ...,
        uirevision: Hashable = ...,
        values=...,  # pyright: ignore[reportMissingParameterType]
        valuessrc: str = ...,
        visible: bool | str = ...,
        row=...,  # pyright: ignore[reportMissingParameterType]
        col=...,  # pyright: ignore[reportMissingParameterType]
        **kwargs: Any,
    ) -> Figure: ...
    def add_image(
        self,
        colormodel=...,  # pyright: ignore[reportMissingParameterType]
        customdata: Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] | pd.Series[float] = ...,
        customdatasrc: str = ...,
        dx: int | float = ...,
        dy: int | float = ...,
        hoverinfo: str | Sequence[str] = ...,
        hoverinfosrc: str = ...,
        hoverlabel: image.Hoverlabel | dict[str, Any] = ...,
        hovertemplate: str
        | float
        | Sequence[str]
        | Sequence[float]
        | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        hovertemplatesrc: str = ...,
        hovertext: str
        | float
        | Sequence[str]
        | Sequence[float]
        | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        hovertextsrc: str = ...,
        ids: Sequence[str] | np.ndarray[tuple[int, ...], np.dtype[np.str_]] | pd.Series[str] = ...,
        idssrc: str = ...,
        legend: str = ...,
        legendgrouptitle: image.Legendgrouptitle | dict[str, Any] = ...,
        legendrank: int | float = ...,
        legendwidth: int | float = ...,
        meta: Sequence[Any] | dict[str, Any] | np.ndarray[tuple[int, ...], Any] = ...,
        metasrc: str = ...,
        name: str | int = ...,
        opacity: int | float = ...,
        source=...,  # pyright: ignore[reportMissingParameterType]
        stream: image.Stream | dict[str, int | str] = ...,
        text: str | float | Sequence[str] | Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        textsrc: str = ...,
        uid: str | int = ...,
        uirevision: Hashable = ...,
        visible: bool | str = ...,
        x0: int | float = ...,
        xaxis: str = ...,
        y0: int | float = ...,
        yaxis: str = ...,
        z=...,  # pyright: ignore[reportMissingParameterType]
        zmax: int | float = ...,
        zmin: int | float = ...,
        zorder: int = ...,
        zsmooth: str | bool = ...,
        zsrc: str = ...,
        row=...,  # pyright: ignore[reportMissingParameterType]
        col=...,  # pyright: ignore[reportMissingParameterType]
        secondary_y: bool | None = ...,
        **kwargs: Any,
    ) -> Figure: ...
    def add_indicator(
        self,
        align=...,  # pyright: ignore[reportMissingParameterType]
        customdata: Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] | pd.Series[float] = ...,
        customdatasrc: str = ...,
        delta=...,  # pyright: ignore[reportMissingParameterType]
        domain=...,  # pyright: ignore[reportMissingParameterType]
        gauge=...,  # pyright: ignore[reportMissingParameterType]
        ids: Sequence[str] | np.ndarray[tuple[int, ...], np.dtype[np.str_]] | pd.Series[str] = ...,
        idssrc: str = ...,
        legend: str = ...,
        legendgrouptitle: indicator.Legendgrouptitle | dict[str, Any] = ...,
        legendrank: int | float = ...,
        legendwidth: int | float = ...,
        meta: Sequence[Any] | dict[str, Any] | np.ndarray[tuple[int, ...], Any] = ...,
        metasrc: str = ...,
        mode: str = ...,
        name: str | int = ...,
        number=...,  # pyright: ignore[reportMissingParameterType]
        stream: indicator.Stream | dict[str, int | str] = ...,
        title=...,  # pyright: ignore[reportMissingParameterType]
        uid: str | int = ...,
        uirevision: Hashable = ...,
        value=...,  # pyright: ignore[reportMissingParameterType]
        visible: bool | str = ...,
        row=...,  # pyright: ignore[reportMissingParameterType]
        col=...,  # pyright: ignore[reportMissingParameterType]
        **kwargs: Any,
    ) -> Figure: ...
    def add_isosurface(
        self,
        autocolorscale: bool = ...,
        caps=...,  # pyright: ignore[reportMissingParameterType]
        cauto: bool = ...,
        cmax: int | float = ...,
        cmid: int | float = ...,
        cmin: int | float = ...,
        coloraxis: str = ...,
        colorbar: isosurface.ColorBar | dict[str, Any] = ...,
        colorscale: str | list[str] | list[tuple[float, str]] = ...,
        contour=...,  # pyright: ignore[reportMissingParameterType]
        customdata: Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] | pd.Series[float] = ...,
        customdatasrc: str = ...,
        flatshading=...,  # pyright: ignore[reportMissingParameterType]
        hoverinfo: str | Sequence[str] = ...,
        hoverinfosrc: str = ...,
        hoverlabel: isosurface.Hoverlabel | dict[str, Any] = ...,
        hovertemplate: str
        | float
        | Sequence[str]
        | Sequence[float]
        | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        hovertemplatesrc: str = ...,
        hovertext: str
        | float
        | Sequence[str]
        | Sequence[float]
        | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        hovertextsrc: str = ...,
        ids: Sequence[str] | np.ndarray[tuple[int, ...], np.dtype[np.str_]] | pd.Series[str] = ...,
        idssrc: str = ...,
        isomax=...,  # pyright: ignore[reportMissingParameterType]
        isomin=...,  # pyright: ignore[reportMissingParameterType]
        legend: str = ...,
        legendgroup: str | int = ...,
        legendgrouptitle: isosurface.Legendgrouptitle | dict[str, Any] = ...,
        legendrank: int | float = ...,
        legendwidth: int | float = ...,
        lighting: isosurface.Lighting | dict[str, Any] = ...,
        lightposition: isosurface.Lightposition
        | dict[str, Sequence[int] | Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]]] = ...,
        meta: Sequence[Any] | dict[str, Any] | np.ndarray[tuple[int, ...], Any] = ...,
        metasrc: str = ...,
        name: str | int = ...,
        opacity: int | float = ...,
        reversescale: bool = ...,
        scene: str = ...,
        showlegend: bool = ...,
        showscale: bool = ...,
        slices=...,  # pyright: ignore[reportMissingParameterType]
        spaceframe=...,  # pyright: ignore[reportMissingParameterType]
        stream: isosurface.Stream | dict[str, int | str] = ...,
        surface=...,  # pyright: ignore[reportMissingParameterType]
        text: str | float | Sequence[str] | Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        textsrc: str = ...,
        uid: str | int = ...,
        uirevision: Hashable = ...,
        value=...,  # pyright: ignore[reportMissingParameterType]
        valuehoverformat: str = ...,
        valuesrc: str = ...,
        visible: bool | str = ...,
        x=...,  # pyright: ignore[reportMissingParameterType]
        xhoverformat: str = ...,
        xsrc: str = ...,
        y=...,  # pyright: ignore[reportMissingParameterType]
        yhoverformat: str = ...,
        ysrc: str = ...,
        z=...,  # pyright: ignore[reportMissingParameterType]
        zhoverformat: str = ...,
        zsrc: str = ...,
        row=...,  # pyright: ignore[reportMissingParameterType]
        col=...,  # pyright: ignore[reportMissingParameterType]
        **kwargs: Any,
    ) -> Figure: ...
    def add_mesh3d(
        self,
        alphahull=...,  # pyright: ignore[reportMissingParameterType]
        autocolorscale: bool = ...,
        cauto: bool = ...,
        cmax: int | float = ...,
        cmid: int | float = ...,
        cmin: int | float = ...,
        color=...,  # pyright: ignore[reportMissingParameterType]
        coloraxis: str = ...,
        colorbar: mesh3d.ColorBar | dict[str, Any] = ...,
        colorscale: str | list[str] | list[tuple[float, str]] = ...,
        contour=...,  # pyright: ignore[reportMissingParameterType]
        customdata: Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] | pd.Series[float] = ...,
        customdatasrc: str = ...,
        delaunayaxis=...,  # pyright: ignore[reportMissingParameterType]
        facecolor=...,  # pyright: ignore[reportMissingParameterType]
        facecolorsrc: str = ...,
        flatshading=...,  # pyright: ignore[reportMissingParameterType]
        hoverinfo: str | Sequence[str] = ...,
        hoverinfosrc: str = ...,
        hoverlabel: mesh3d.Hoverlabel | dict[str, Any] = ...,
        hovertemplate: str
        | float
        | Sequence[str]
        | Sequence[float]
        | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        hovertemplatesrc: str = ...,
        hovertext: str
        | float
        | Sequence[str]
        | Sequence[float]
        | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        hovertextsrc: str = ...,
        i=...,  # pyright: ignore[reportMissingParameterType]
        ids: Sequence[str] | np.ndarray[tuple[int, ...], np.dtype[np.str_]] | pd.Series[str] = ...,
        idssrc: str = ...,
        intensity=...,  # pyright: ignore[reportMissingParameterType]
        intensitymode=...,  # pyright: ignore[reportMissingParameterType]
        intensitysrc: str = ...,
        isrc: str = ...,
        j=...,  # pyright: ignore[reportMissingParameterType]
        jsrc: str = ...,
        k=...,  # pyright: ignore[reportMissingParameterType]
        ksrc: str = ...,
        legend: str = ...,
        legendgroup: str | int = ...,
        legendgrouptitle: mesh3d.Legendgrouptitle | dict[str, Any] = ...,
        legendrank: int | float = ...,
        legendwidth: int | float = ...,
        lighting: mesh3d.Lighting | dict[str, Any] = ...,
        lightposition: mesh3d.Lightposition
        | dict[str, Sequence[int] | Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]]] = ...,
        meta: Sequence[Any] | dict[str, Any] | np.ndarray[tuple[int, ...], Any] = ...,
        metasrc: str = ...,
        name: str | int = ...,
        opacity: int | float = ...,
        reversescale: bool = ...,
        scene: str = ...,
        showlegend: bool = ...,
        showscale: bool = ...,
        stream: mesh3d.Stream | dict[str, int | str] = ...,
        text: str | float | Sequence[str] | Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        textsrc: str = ...,
        uid: str | int = ...,
        uirevision: Hashable = ...,
        vertexcolor=...,  # pyright: ignore[reportMissingParameterType]
        vertexcolorsrc: str = ...,
        visible: bool | str = ...,
        x=...,  # pyright: ignore[reportMissingParameterType]
        xcalendar: str = ...,
        xhoverformat: str = ...,
        xsrc: str = ...,
        y=...,  # pyright: ignore[reportMissingParameterType]
        ycalendar: str = ...,
        yhoverformat: str = ...,
        ysrc: str = ...,
        z=...,  # pyright: ignore[reportMissingParameterType]
        zcalendar: str = ...,
        zhoverformat: str = ...,
        zsrc: str = ...,
        row=...,  # pyright: ignore[reportMissingParameterType]
        col=...,  # pyright: ignore[reportMissingParameterType]
        **kwargs: Any,
    ) -> Figure: ...
    def add_ohlc(
        self,
        close=...,  # pyright: ignore[reportMissingParameterType]
        closesrc: str = ...,
        customdata: Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] | pd.Series[float] = ...,
        customdatasrc: str = ...,
        decreasing=...,  # pyright: ignore[reportMissingParameterType]
        high=...,  # pyright: ignore[reportMissingParameterType]
        highsrc: str = ...,
        hoverinfo: str | Sequence[str] = ...,
        hoverinfosrc: str = ...,
        hoverlabel: ohlc.Hoverlabel | dict[str, Any] = ...,
        hovertext: str
        | float
        | Sequence[str]
        | Sequence[float]
        | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        hovertextsrc: str = ...,
        ids: Sequence[str] | np.ndarray[tuple[int, ...], np.dtype[np.str_]] | pd.Series[str] = ...,
        idssrc: str = ...,
        increasing=...,  # pyright: ignore[reportMissingParameterType]
        legend: str = ...,
        legendgroup: str | int = ...,
        legendgrouptitle: ohlc.Legendgrouptitle | dict[str, Any] = ...,
        legendrank: int | float = ...,
        legendwidth: int | float = ...,
        line: ohlc.Line | dict[str, str | int | float] = ...,
        low=...,  # pyright: ignore[reportMissingParameterType]
        lowsrc: str = ...,
        meta: Sequence[Any] | dict[str, Any] | np.ndarray[tuple[int, ...], Any] = ...,
        metasrc: str = ...,
        name: str | int = ...,
        opacity: int | float = ...,
        open=...,  # pyright: ignore[reportMissingParameterType]
        opensrc: str = ...,
        selectedpoints: Sequence[int] = ...,
        showlegend: bool = ...,
        stream: ohlc.Stream | dict[str, int | str] = ...,
        text: str | float | Sequence[str] | Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        textsrc: str = ...,
        tickwidth=...,  # pyright: ignore[reportMissingParameterType]
        uid: str | int = ...,
        uirevision: Hashable = ...,
        visible: bool | str = ...,
        x=...,  # pyright: ignore[reportMissingParameterType]
        xaxis: str = ...,
        xcalendar: str = ...,
        xhoverformat: str = ...,
        xperiod: int | float | str = ...,
        xperiod0: int | float | str = ...,
        xperiodalignment: str = ...,
        xsrc: str = ...,
        yaxis: str = ...,
        yhoverformat: str = ...,
        zorder: int = ...,
        row=...,  # pyright: ignore[reportMissingParameterType]
        col=...,  # pyright: ignore[reportMissingParameterType]
        secondary_y: bool | None = ...,
        **kwargs: Any,
    ) -> Figure: ...
    def add_parcats(
        self,
        arrangement=...,  # pyright: ignore[reportMissingParameterType]
        bundlecolors=...,  # pyright: ignore[reportMissingParameterType]
        counts=...,  # pyright: ignore[reportMissingParameterType]
        countssrc: str = ...,
        dimensions=...,  # pyright: ignore[reportMissingParameterType]
        dimensiondefaults=...,  # pyright: ignore[reportMissingParameterType]
        domain=...,  # pyright: ignore[reportMissingParameterType]
        hoverinfo: str | Sequence[str] = ...,
        hoveron: str = ...,
        hovertemplate: str
        | float
        | Sequence[str]
        | Sequence[float]
        | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        labelfont=...,  # pyright: ignore[reportMissingParameterType]
        legendgrouptitle: parcats.Legendgrouptitle | dict[str, Any] = ...,
        legendwidth: int | float = ...,
        line: parcats.Line | dict[str, str | int | float] = ...,
        meta: Sequence[Any] | dict[str, Any] | np.ndarray[tuple[int, ...], Any] = ...,
        metasrc: str = ...,
        name: str | int = ...,
        sortpaths=...,  # pyright: ignore[reportMissingParameterType]
        stream: parcats.Stream | dict[str, int | str] = ...,
        tickfont=...,  # pyright: ignore[reportMissingParameterType]
        uid: str | int = ...,
        uirevision: Hashable = ...,
        visible: bool | str = ...,
        row=...,  # pyright: ignore[reportMissingParameterType]
        col=...,  # pyright: ignore[reportMissingParameterType]
        **kwargs: Any,
    ) -> Figure: ...
    def add_parcoords(
        self,
        customdata: Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] | pd.Series[float] = ...,
        customdatasrc: str = ...,
        dimensions=...,  # pyright: ignore[reportMissingParameterType]
        dimensiondefaults=...,  # pyright: ignore[reportMissingParameterType]
        domain=...,  # pyright: ignore[reportMissingParameterType]
        ids: Sequence[str] | np.ndarray[tuple[int, ...], np.dtype[np.str_]] | pd.Series[str] = ...,
        idssrc: str = ...,
        labelangle=...,  # pyright: ignore[reportMissingParameterType]
        labelfont=...,  # pyright: ignore[reportMissingParameterType]
        labelside=...,  # pyright: ignore[reportMissingParameterType]
        legend: str = ...,
        legendgrouptitle: parcoords.Legendgrouptitle | dict[str, Any] = ...,
        legendrank: int | float = ...,
        legendwidth: int | float = ...,
        line: parcoords.Line | dict[str, str | int | float] = ...,
        meta: Sequence[Any] | dict[str, Any] | np.ndarray[tuple[int, ...], Any] = ...,
        metasrc: str = ...,
        name: str | int = ...,
        rangefont=...,  # pyright: ignore[reportMissingParameterType]
        stream: parcoords.Stream | dict[str, int | str] = ...,
        tickfont=...,  # pyright: ignore[reportMissingParameterType]
        uid: str | int = ...,
        uirevision: Hashable = ...,
        unselected: parcoords.Unselected | dict[str, parcoords.unselected.Line | dict[str, Any]] = ...,
        visible: bool | str = ...,
        row=...,  # pyright: ignore[reportMissingParameterType]
        col=...,  # pyright: ignore[reportMissingParameterType]
        **kwargs: Any,
    ) -> Figure: ...
    def add_pie(
        self,
        automargin=...,  # pyright: ignore[reportMissingParameterType]
        customdata: Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] | pd.Series[float] = ...,
        customdatasrc: str = ...,
        direction=...,  # pyright: ignore[reportMissingParameterType]
        dlabel=...,  # pyright: ignore[reportMissingParameterType]
        domain=...,  # pyright: ignore[reportMissingParameterType]
        hole=...,  # pyright: ignore[reportMissingParameterType]
        hoverinfo: str | Sequence[str] = ...,
        hoverinfosrc: str = ...,
        hoverlabel: pie.Hoverlabel | dict[str, Any] = ...,
        hovertemplate: str
        | float
        | Sequence[str]
        | Sequence[float]
        | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        hovertemplatesrc: str = ...,
        hovertext: str
        | float
        | Sequence[str]
        | Sequence[float]
        | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        hovertextsrc: str = ...,
        ids: Sequence[str] | np.ndarray[tuple[int, ...], np.dtype[np.str_]] | pd.Series[str] = ...,
        idssrc: str = ...,
        insidetextfont=...,  # pyright: ignore[reportMissingParameterType]
        insidetextorientation=...,  # pyright: ignore[reportMissingParameterType]
        label0=...,  # pyright: ignore[reportMissingParameterType]
        labels=...,  # pyright: ignore[reportMissingParameterType]
        labelssrc: str = ...,
        legend: str = ...,
        legendgroup: str | int = ...,
        legendgrouptitle: pie.Legendgrouptitle | dict[str, Any] = ...,
        legendrank: int | float = ...,
        legendwidth: int | float = ...,
        marker: pie.Marker | dict[str, Any] = ...,
        meta: Sequence[Any] | dict[str, Any] | np.ndarray[tuple[int, ...], Any] = ...,
        metasrc: str = ...,
        name: str | int = ...,
        opacity: int | float = ...,
        outsidetextfont=...,  # pyright: ignore[reportMissingParameterType]
        pull=...,  # pyright: ignore[reportMissingParameterType]
        pullsrc: str = ...,
        rotation=...,  # pyright: ignore[reportMissingParameterType]
        scalegroup=...,  # pyright: ignore[reportMissingParameterType]
        showlegend: bool = ...,
        sort=...,  # pyright: ignore[reportMissingParameterType]
        stream: pie.Stream | dict[str, int | str] = ...,
        text: str | float | Sequence[str] | Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        textfont: pie.Textfont | dict[str, Any] = ...,
        textinfo=...,  # pyright: ignore[reportMissingParameterType]
        textposition: str | Sequence[str] | np.ndarray[tuple[int, ...], np.dtype[np.str_]] = ...,
        textpositionsrc: str = ...,
        textsrc: str = ...,
        texttemplate: str = ...,
        texttemplatesrc: str = ...,
        title=...,  # pyright: ignore[reportMissingParameterType]
        uid: str | int = ...,
        uirevision: Hashable = ...,
        values=...,  # pyright: ignore[reportMissingParameterType]
        valuessrc: str = ...,
        visible: bool | str = ...,
        row=...,  # pyright: ignore[reportMissingParameterType]
        col=...,  # pyright: ignore[reportMissingParameterType]
        **kwargs: Any,
    ) -> Figure: ...
    def add_sankey(
        self,
        arrangement=...,  # pyright: ignore[reportMissingParameterType]
        customdata: Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] | pd.Series[float] = ...,
        customdatasrc: str = ...,
        domain=...,  # pyright: ignore[reportMissingParameterType]
        hoverinfo: str | Sequence[str] = ...,
        hoverlabel: sankey.Hoverlabel | dict[str, Any] = ...,
        ids: Sequence[str] | np.ndarray[tuple[int, ...], np.dtype[np.str_]] | pd.Series[str] = ...,
        idssrc: str = ...,
        legend: str = ...,
        legendgrouptitle: sankey.Legendgrouptitle | dict[str, Any] = ...,
        legendrank: int | float = ...,
        legendwidth: int | float = ...,
        link=...,  # pyright: ignore[reportMissingParameterType]
        meta: Sequence[Any] | dict[str, Any] | np.ndarray[tuple[int, ...], Any] = ...,
        metasrc: str = ...,
        name: str | int = ...,
        node=...,  # pyright: ignore[reportMissingParameterType]
        orientation: str = ...,
        selectedpoints: Sequence[int] = ...,
        stream: sankey.Stream | dict[str, int | str] = ...,
        textfont: sankey.Textfont | dict[str, Any] = ...,
        uid: str | int = ...,
        uirevision: Hashable = ...,
        valueformat=...,  # pyright: ignore[reportMissingParameterType]
        valuesuffix=...,  # pyright: ignore[reportMissingParameterType]
        visible: bool | str = ...,
        row=...,  # pyright: ignore[reportMissingParameterType]
        col=...,  # pyright: ignore[reportMissingParameterType]
        **kwargs: Any,
    ) -> Figure: ...
    def add_scatter(
        self,
        alignmentgroup: str | int = ...,
        cliponaxis: bool = ...,
        connectgaps: bool = ...,
        customdata: Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] | pd.Series[float] = ...,
        customdatasrc: str = ...,
        dx: int | float = ...,
        dy: int | float = ...,
        error_x: scatter.ErrorX | dict[str, Any] = ...,
        error_y: scatter.ErrorY | dict[str, Any] = ...,
        fill: str = ...,
        fillcolor: str = ...,
        fillgradient: scatter.Fillgradient | dict[str, Any] | None = ...,
        fillpattern: scatter.Fillpattern | dict[str, Any] = ...,
        groupnorm: str = ...,
        hoverinfo: str | Sequence[str] = ...,
        hoverinfosrc: str = ...,
        hoverlabel: scatter.Hoverlabel | dict[str, Any] = ...,
        hoveron: str = ...,
        hovertemplate: str
        | float
        | Sequence[str]
        | Sequence[float]
        | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        hovertemplatesrc: str = ...,
        hovertext: str
        | float
        | Sequence[str]
        | Sequence[float]
        | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        hovertextsrc: str = ...,
        ids: Sequence[str] | np.ndarray[tuple[int, ...], np.dtype[np.str_]] | pd.Series[str] = ...,
        idssrc: str = ...,
        legend: str = ...,
        legendgroup: str | int = ...,
        legendgrouptitle: scatter.Legendgrouptitle | dict[str, Any] = ...,
        legendrank: int | float = ...,
        legendwidth: int | float = ...,
        line: scatter.Line | dict[str, str | int | float] = ...,
        marker: scatter.Marker | dict[str, Any] = ...,
        meta: Sequence[Any] | dict[str, Any] | np.ndarray[tuple[int, ...], Any] = ...,
        metasrc: str = ...,
        mode: str = ...,
        name: str | int = ...,
        offsetgroup: str | int = ...,
        opacity: int | float = ...,
        orientation: str = ...,
        selected: scatter.Selected
        | dict[str, scatter.selected.Marker | scatter.selected.Textfont | dict[str, Any]] = ...,
        selectedpoints: Sequence[int] = ...,
        showlegend: bool = ...,
        stackgaps: str = ...,
        stackgroup: str | int = ...,
        stream: scatter.Stream | dict[str, int | str] = ...,
        text: str | float | Sequence[str] | Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        textfont: scatter.Textfont | dict[str, Any] = ...,
        textposition: str | Sequence[str] | np.ndarray[tuple[int, ...], np.dtype[np.str_]] = ...,
        textpositionsrc: str = ...,
        textsrc: str = ...,
        texttemplate: str = ...,
        texttemplatesrc: str = ...,
        uid: str | int = ...,
        uirevision: Hashable = ...,
        unselected: scatter.Unselected
        | dict[str, scatter.unselected.Marker | scatter.unselected.Textfont | dict[str, Any]] = ...,
        visible: bool | str = ...,
        x: Sequence[Any] | np.ndarray[tuple[int, ...], np.dtype[Any]] | pd.Series[Any] = ...,
        x0: int | float = ...,
        xaxis: str = ...,
        xcalendar: str = ...,
        xhoverformat: str = ...,
        xperiod: int | float | str = ...,
        xperiod0: int | float | str = ...,
        xperiodalignment: str = ...,
        xsrc: str = ...,
        y: Sequence[int] | Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] | pd.Series[float] = ...,
        y0: int | float = ...,
        yaxis: str = ...,
        ycalendar: str = ...,
        yhoverformat: str = ...,
        yperiod: int | float | str = ...,
        yperiod0: int | float | str = ...,
        yperiodalignment: str = ...,
        ysrc: str = ...,
        zorder: int = ...,
        row: int | str | None = ...,
        col: int | str | None = ...,
        secondary_y: bool | None = ...,
        **kwargs: Any,
    ) -> Figure: ...
    def add_scatter3d(
        self,
        connectgaps: bool = ...,
        customdata: Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] | pd.Series[float] = ...,
        customdatasrc: str = ...,
        error_x: scatter3d.ErrorX | dict[str, Any] = ...,
        error_y: scatter3d.ErrorY | dict[str, Any] = ...,
        error_z=...,  # pyright: ignore[reportMissingParameterType]
        hoverinfo: str | Sequence[str] = ...,
        hoverinfosrc: str = ...,
        hoverlabel: scatter3d.Hoverlabel | dict[str, Any] = ...,
        hovertemplate: str
        | float
        | Sequence[str]
        | Sequence[float]
        | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        hovertemplatesrc: str = ...,
        hovertext: str
        | float
        | Sequence[str]
        | Sequence[float]
        | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        hovertextsrc: str = ...,
        ids: Sequence[str] | np.ndarray[tuple[int, ...], np.dtype[np.str_]] | pd.Series[str] = ...,
        idssrc: str = ...,
        legend: str = ...,
        legendgroup: str | int = ...,
        legendgrouptitle: scatter3d.Legendgrouptitle | dict[str, Any] = ...,
        legendrank: int | float = ...,
        legendwidth: int | float = ...,
        line: scatter3d.Line | dict[str, str | int | float] = ...,
        marker: scatter3d.Marker | dict[str, Any] = ...,
        meta: Sequence[Any] | dict[str, Any] | np.ndarray[tuple[int, ...], Any] = ...,
        metasrc: str = ...,
        mode: str = ...,
        name: str | int = ...,
        opacity: int | float = ...,
        projection=...,  # pyright: ignore[reportMissingParameterType]
        scene: str = ...,
        showlegend: bool = ...,
        stream: scatter3d.Stream | dict[str, int | str] = ...,
        surfaceaxis=...,  # pyright: ignore[reportMissingParameterType]
        surfacecolor: Sequence[str] | np.ndarray[tuple[int, ...], np.dtype[np.str_]] | pd.Series[str] = ...,
        text: str | float | Sequence[str] | Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        textfont: scatter3d.Textfont | dict[str, Any] = ...,
        textposition: str | Sequence[str] | np.ndarray[tuple[int, ...], np.dtype[np.str_]] = ...,
        textpositionsrc: str = ...,
        textsrc: str = ...,
        texttemplate: str = ...,
        texttemplatesrc: str = ...,
        uid: str | int = ...,
        uirevision: Hashable = ...,
        visible: bool | str = ...,
        x=...,  # pyright: ignore[reportMissingParameterType]
        xcalendar: str = ...,
        xhoverformat: str = ...,
        xsrc: str = ...,
        y=...,  # pyright: ignore[reportMissingParameterType]
        ycalendar: str = ...,
        yhoverformat: str = ...,
        ysrc: str = ...,
        z=...,  # pyright: ignore[reportMissingParameterType]
        zcalendar: str = ...,
        zhoverformat: str = ...,
        zsrc: str = ...,
        row=...,  # pyright: ignore[reportMissingParameterType]
        col=...,  # pyright: ignore[reportMissingParameterType]
        **kwargs: Any,
    ) -> Figure: ...
    def add_scattercarpet(
        self,
        a=...,  # pyright: ignore[reportMissingParameterType]
        asrc: str = ...,
        b=...,  # pyright: ignore[reportMissingParameterType]
        bsrc: str = ...,
        carpet=...,  # pyright: ignore[reportMissingParameterType]
        connectgaps: bool = ...,
        customdata: Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] | pd.Series[float] = ...,
        customdatasrc: str = ...,
        fill: str = ...,
        fillcolor: str = ...,
        hoverinfo: str | Sequence[str] = ...,
        hoverinfosrc: str = ...,
        hoverlabel: scattercarpet.Hoverlabel | dict[str, Any] = ...,
        hoveron: str = ...,
        hovertemplate: str
        | float
        | Sequence[str]
        | Sequence[float]
        | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        hovertemplatesrc: str = ...,
        hovertext: str
        | float
        | Sequence[str]
        | Sequence[float]
        | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        hovertextsrc: str = ...,
        ids: Sequence[str] | np.ndarray[tuple[int, ...], np.dtype[np.str_]] | pd.Series[str] = ...,
        idssrc: str = ...,
        legend: str = ...,
        legendgroup: str | int = ...,
        legendgrouptitle: scattercarpet.Legendgrouptitle | dict[str, Any] = ...,
        legendrank: int | float = ...,
        legendwidth: int | float = ...,
        line: scattercarpet.Line | dict[str, str | int | float] = ...,
        marker: scattercarpet.Marker | dict[str, Any] = ...,
        meta: Sequence[Any] | dict[str, Any] | np.ndarray[tuple[int, ...], Any] = ...,
        metasrc: str = ...,
        mode: str = ...,
        name: str | int = ...,
        opacity: int | float = ...,
        selected: scattercarpet.Selected
        | dict[str, scattercarpet.selected.Marker | scattercarpet.selected.Textfont | dict[str, Any]] = ...,
        selectedpoints: Sequence[int] = ...,
        showlegend: bool = ...,
        stream: scattercarpet.Stream | dict[str, int | str] = ...,
        text: str | float | Sequence[str] | Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        textfont: scattercarpet.Textfont | dict[str, Any] = ...,
        textposition: str | Sequence[str] | np.ndarray[tuple[int, ...], np.dtype[np.str_]] = ...,
        textpositionsrc: str = ...,
        textsrc: str = ...,
        texttemplate: str = ...,
        texttemplatesrc: str = ...,
        uid: str | int = ...,
        uirevision: Hashable = ...,
        unselected: scattercarpet.Unselected
        | dict[str, scattercarpet.unselected.Marker | scattercarpet.unselected.Textfont | dict[str, Any]] = ...,
        visible: bool | str = ...,
        xaxis: str = ...,
        yaxis: str = ...,
        zorder: int = ...,
        row=...,  # pyright: ignore[reportMissingParameterType]
        col=...,  # pyright: ignore[reportMissingParameterType]
        secondary_y: bool | None = ...,
        **kwargs: Any,
    ) -> Figure: ...
    def add_scattergeo(
        self,
        connectgaps: bool = ...,
        customdata: Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] | pd.Series[float] = ...,
        customdatasrc: str = ...,
        featureidkey=...,  # pyright: ignore[reportMissingParameterType]
        fill: str = ...,
        fillcolor: str = ...,
        geo=...,  # pyright: ignore[reportMissingParameterType]
        geojson=...,  # pyright: ignore[reportMissingParameterType]
        hoverinfo: str | Sequence[str] = ...,
        hoverinfosrc: str = ...,
        hoverlabel: scattergeo.Hoverlabel | dict[str, Any] = ...,
        hovertemplate: str
        | float
        | Sequence[str]
        | Sequence[float]
        | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        hovertemplatesrc: str = ...,
        hovertext: str
        | float
        | Sequence[str]
        | Sequence[float]
        | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        hovertextsrc: str = ...,
        ids: Sequence[str] | np.ndarray[tuple[int, ...], np.dtype[np.str_]] | pd.Series[str] = ...,
        idssrc: str = ...,
        lat=...,  # pyright: ignore[reportMissingParameterType]
        latsrc: str = ...,
        legend: str = ...,
        legendgroup: str | int = ...,
        legendgrouptitle: scattergeo.Legendgrouptitle | dict[str, Any] = ...,
        legendrank: int | float = ...,
        legendwidth: int | float = ...,
        line: scattergeo.Line | dict[str, str | int | float] = ...,
        locationmode=...,  # pyright: ignore[reportMissingParameterType]
        locations=...,  # pyright: ignore[reportMissingParameterType]
        locationssrc: str = ...,
        lon=...,  # pyright: ignore[reportMissingParameterType]
        lonsrc: str = ...,
        marker: scattergeo.Marker | dict[str, Any] = ...,
        meta: Sequence[Any] | dict[str, Any] | np.ndarray[tuple[int, ...], Any] = ...,
        metasrc: str = ...,
        mode: str = ...,
        name: str | int = ...,
        opacity: int | float = ...,
        selected: scattergeo.Selected
        | dict[str, scattergeo.selected.Marker | scattergeo.selected.Textfont | dict[str, Any]] = ...,
        selectedpoints: Sequence[int] = ...,
        showlegend: bool = ...,
        stream: scattergeo.Stream | dict[str, int | str] = ...,
        text: str | float | Sequence[str] | Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        textfont: scattergeo.Textfont | dict[str, Any] = ...,
        textposition: str | Sequence[str] | np.ndarray[tuple[int, ...], np.dtype[np.str_]] = ...,
        textpositionsrc: str = ...,
        textsrc: str = ...,
        texttemplate: str = ...,
        texttemplatesrc: str = ...,
        uid: str | int = ...,
        uirevision: Hashable = ...,
        unselected: scattergeo.Unselected
        | dict[str, scattergeo.unselected.Marker | scattergeo.unselected.Textfont | dict[str, Any]] = ...,
        visible: bool | str = ...,
        row=...,  # pyright: ignore[reportMissingParameterType]
        col=...,  # pyright: ignore[reportMissingParameterType]
        **kwargs: Any,
    ) -> Figure: ...
    def add_scattergl(
        self,
        connectgaps: bool = ...,
        customdata: Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] | pd.Series[float] = ...,
        customdatasrc: str = ...,
        dx: int | float = ...,
        dy: int | float = ...,
        error_x: scattergl.ErrorX | dict[str, Any] = ...,
        error_y: scattergl.ErrorY | dict[str, Any] = ...,
        fill: str = ...,
        fillcolor: str = ...,
        hoverinfo: str | Sequence[str] = ...,
        hoverinfosrc: str = ...,
        hoverlabel: scattergl.Hoverlabel | dict[str, Any] = ...,
        hovertemplate: str
        | float
        | Sequence[str]
        | Sequence[float]
        | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        hovertemplatesrc: str = ...,
        hovertext: str
        | float
        | Sequence[str]
        | Sequence[float]
        | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        hovertextsrc: str = ...,
        ids: Sequence[str] | np.ndarray[tuple[int, ...], np.dtype[np.str_]] | pd.Series[str] = ...,
        idssrc: str = ...,
        legend: str = ...,
        legendgroup: str | int = ...,
        legendgrouptitle: scattergl.Legendgrouptitle | dict[str, Any] = ...,
        legendrank: int | float = ...,
        legendwidth: int | float = ...,
        line: scattergl.Line | dict[str, str | int | float] = ...,
        marker: scattergl.Marker | dict[str, Any] = ...,
        meta: Sequence[Any] | dict[str, Any] | np.ndarray[tuple[int, ...], Any] = ...,
        metasrc: str = ...,
        mode: str = ...,
        name: str | int = ...,
        opacity: int | float = ...,
        selected: scattergl.Selected
        | dict[str, scattergl.selected.Marker | scattergl.selected.Textfont | dict[str, Any]] = ...,
        selectedpoints: Sequence[int] = ...,
        showlegend: bool = ...,
        stream: scattergl.Stream | dict[str, int | str] = ...,
        text: str | float | Sequence[str] | Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        textfont: scattergl.Textfont | dict[str, Any] = ...,
        textposition: str | Sequence[str] | np.ndarray[tuple[int, ...], np.dtype[np.str_]] = ...,
        textpositionsrc: str = ...,
        textsrc: str = ...,
        texttemplate: str = ...,
        texttemplatesrc: str = ...,
        uid: str | int = ...,
        uirevision: Hashable = ...,
        unselected: scattergl.Unselected
        | dict[str, scattergl.unselected.Marker | scattergl.unselected.Textfont | dict[str, Any]] = ...,
        visible: bool | str = ...,
        x=...,  # pyright: ignore[reportMissingParameterType]
        x0: int | float = ...,
        xaxis: str = ...,
        xcalendar: str = ...,
        xhoverformat: str = ...,
        xperiod: int | float | str = ...,
        xperiod0: int | float | str = ...,
        xperiodalignment: str = ...,
        xsrc: str = ...,
        y=...,  # pyright: ignore[reportMissingParameterType]
        y0: int | float = ...,
        yaxis: str = ...,
        ycalendar: str = ...,
        yhoverformat: str = ...,
        yperiod: int | float | str = ...,
        yperiod0: int | float | str = ...,
        yperiodalignment: str = ...,
        ysrc: str = ...,
        row=...,  # pyright: ignore[reportMissingParameterType]
        col=...,  # pyright: ignore[reportMissingParameterType]
        secondary_y: bool | None = ...,
        **kwargs: Any,
    ) -> Figure: ...
    def add_scattermap(
        self,
        below=...,  # pyright: ignore[reportMissingParameterType]
        cluster=...,  # pyright: ignore[reportMissingParameterType]
        connectgaps: bool = ...,
        customdata: Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] | pd.Series[float] = ...,
        customdatasrc: str = ...,
        fill: str = ...,
        fillcolor: str = ...,
        hoverinfo: str | Sequence[str] = ...,
        hoverinfosrc: str = ...,
        hoverlabel: scattermap.Hoverlabel | dict[str, Any] = ...,
        hovertemplate: str
        | float
        | Sequence[str]
        | Sequence[float]
        | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        hovertemplatesrc: str = ...,
        hovertext: str
        | float
        | Sequence[str]
        | Sequence[float]
        | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        hovertextsrc: str = ...,
        ids: Sequence[str] | np.ndarray[tuple[int, ...], np.dtype[np.str_]] | pd.Series[str] = ...,
        idssrc: str = ...,
        lat=...,  # pyright: ignore[reportMissingParameterType]
        latsrc: str = ...,
        legend: str = ...,
        legendgroup: str | int = ...,
        legendgrouptitle: scattermap.Legendgrouptitle | dict[str, Any] = ...,
        legendrank: int | float = ...,
        legendwidth: int | float = ...,
        line: scattermap.Line | dict[str, str | int | float] = ...,
        lon=...,  # pyright: ignore[reportMissingParameterType]
        lonsrc: str = ...,
        marker: scattermap.Marker | dict[str, Any] = ...,
        meta: Sequence[Any] | dict[str, Any] | np.ndarray[tuple[int, ...], Any] = ...,
        metasrc: str = ...,
        mode: str = ...,
        name: str | int = ...,
        opacity: int | float = ...,
        selected: scattermap.Selected | dict[str, scattermap.selected.Marker | dict[str, Any]] = ...,
        selectedpoints: Sequence[int] = ...,
        showlegend: bool = ...,
        stream: scattermap.Stream | dict[str, int | str] = ...,
        subplot=...,  # pyright: ignore[reportMissingParameterType]
        text: str | float | Sequence[str] | Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        textfont: scattermap.Textfont | dict[str, Any] = ...,
        textposition: str | Sequence[str] | np.ndarray[tuple[int, ...], np.dtype[np.str_]] = ...,
        textsrc: str = ...,
        texttemplate: str = ...,
        texttemplatesrc: str = ...,
        uid: str | int = ...,
        uirevision: Hashable = ...,
        unselected: scattermap.Unselected | dict[str, scattermap.unselected.Marker | dict[str, Any]] = ...,
        visible: bool | str = ...,
        row=...,  # pyright: ignore[reportMissingParameterType]
        col=...,  # pyright: ignore[reportMissingParameterType]
        **kwargs: Any,
    ) -> Figure: ...
    def add_scattermapbox(
        self,
        below=...,  # pyright: ignore[reportMissingParameterType]
        cluster=...,  # pyright: ignore[reportMissingParameterType]
        connectgaps: bool = ...,
        customdata: Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] | pd.Series[float] = ...,
        customdatasrc: str = ...,
        fill: str = ...,
        fillcolor: str = ...,
        hoverinfo: str | Sequence[str] = ...,
        hoverinfosrc: str = ...,
        hoverlabel: scattermapbox.Hoverlabel | dict[str, Any] = ...,
        hovertemplate: str
        | float
        | Sequence[str]
        | Sequence[float]
        | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        hovertemplatesrc: str = ...,
        hovertext: str
        | float
        | Sequence[str]
        | Sequence[float]
        | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        hovertextsrc: str = ...,
        ids: Sequence[str] | np.ndarray[tuple[int, ...], np.dtype[np.str_]] | pd.Series[str] = ...,
        idssrc: str = ...,
        lat=...,  # pyright: ignore[reportMissingParameterType]
        latsrc: str = ...,
        legend: str = ...,
        legendgroup: str | int = ...,
        legendgrouptitle: scattermapbox.Legendgrouptitle | dict[str, Any] = ...,
        legendrank: int | float = ...,
        legendwidth: int | float = ...,
        line: scattermapbox.Line | dict[str, str | int | float] = ...,
        lon=...,  # pyright: ignore[reportMissingParameterType]
        lonsrc: str = ...,
        marker: scattermapbox.Marker | dict[str, Any] = ...,
        meta: Sequence[Any] | dict[str, Any] | np.ndarray[tuple[int, ...], Any] = ...,
        metasrc: str = ...,
        mode: str = ...,
        name: str | int = ...,
        opacity: int | float = ...,
        selected: scattermapbox.Selected | dict[str, scattermapbox.selected.Marker | dict[str, Any]] = ...,
        selectedpoints: Sequence[int] = ...,
        showlegend: bool = ...,
        stream: scattermapbox.Stream | dict[str, int | str] = ...,
        subplot=...,  # pyright: ignore[reportMissingParameterType]
        text: str | float | Sequence[str] | Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        textfont: scattermapbox.Textfont | dict[str, Any] = ...,
        textposition: str | Sequence[str] | np.ndarray[tuple[int, ...], np.dtype[np.str_]] = ...,
        textsrc: str = ...,
        texttemplate: str = ...,
        texttemplatesrc: str = ...,
        uid: str | int = ...,
        uirevision: Hashable = ...,
        unselected: scattermapbox.Unselected | dict[str, scattermapbox.unselected.Marker | dict[str, Any]] = ...,
        visible: bool | str = ...,
        row=...,  # pyright: ignore[reportMissingParameterType]
        col=...,  # pyright: ignore[reportMissingParameterType]
        **kwargs: Any,
    ) -> Figure: ...
    def add_scatterpolar(
        self,
        cliponaxis: bool = ...,
        connectgaps: bool = ...,
        customdata: Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] | pd.Series[float] = ...,
        customdatasrc: str = ...,
        dr=...,  # pyright: ignore[reportMissingParameterType]
        dtheta=...,  # pyright: ignore[reportMissingParameterType]
        fill: str = ...,
        fillcolor: str = ...,
        hoverinfo: str | Sequence[str] = ...,
        hoverinfosrc: str = ...,
        hoverlabel: scatterpolar.Hoverlabel | dict[str, Any] = ...,
        hoveron: str = ...,
        hovertemplate: str
        | float
        | Sequence[str]
        | Sequence[float]
        | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        hovertemplatesrc: str = ...,
        hovertext: str
        | float
        | Sequence[str]
        | Sequence[float]
        | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        hovertextsrc: str = ...,
        ids: Sequence[str] | np.ndarray[tuple[int, ...], np.dtype[np.str_]] | pd.Series[str] = ...,
        idssrc: str = ...,
        legend: str = ...,
        legendgroup: str | int = ...,
        legendgrouptitle: scatterpolar.Legendgrouptitle | dict[str, Any] = ...,
        legendrank: int | float = ...,
        legendwidth: int | float = ...,
        line: scatterpolar.Line | dict[str, str | int | float] = ...,
        marker: scatterpolar.Marker | dict[str, Any] = ...,
        meta: Sequence[Any] | dict[str, Any] | np.ndarray[tuple[int, ...], Any] = ...,
        metasrc: str = ...,
        mode: str = ...,
        name: str | int = ...,
        opacity: int | float = ...,
        r=...,  # pyright: ignore[reportMissingParameterType]
        r0=...,  # pyright: ignore[reportMissingParameterType]
        rsrc: str = ...,
        selected: scatterpolar.Selected
        | dict[str, scatterpolar.selected.Marker | scatterpolar.selected.Textfont | dict[str, Any]] = ...,
        selectedpoints: Sequence[int] = ...,
        showlegend: bool = ...,
        stream: scatterpolar.Stream | dict[str, int | str] = ...,
        subplot=...,  # pyright: ignore[reportMissingParameterType]
        text: str | float | Sequence[str] | Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        textfont: scatterpolar.Textfont | dict[str, Any] = ...,
        textposition: str | Sequence[str] | np.ndarray[tuple[int, ...], np.dtype[np.str_]] = ...,
        textpositionsrc: str = ...,
        textsrc: str = ...,
        texttemplate: str = ...,
        texttemplatesrc: str = ...,
        theta=...,  # pyright: ignore[reportMissingParameterType]
        theta0=...,  # pyright: ignore[reportMissingParameterType]
        thetasrc: str = ...,
        thetaunit=...,  # pyright: ignore[reportMissingParameterType]
        uid: str | int = ...,
        uirevision: Hashable = ...,
        unselected: scatterpolar.Unselected
        | dict[str, scatterpolar.unselected.Marker | scatterpolar.unselected.Textfont | dict[str, Any]] = ...,
        visible: bool | str = ...,
        row=...,  # pyright: ignore[reportMissingParameterType]
        col=...,  # pyright: ignore[reportMissingParameterType]
        **kwargs: Any,
    ) -> Figure: ...
    def add_scatterpolargl(
        self,
        connectgaps: bool = ...,
        customdata: Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] | pd.Series[float] = ...,
        customdatasrc: str = ...,
        dr=...,  # pyright: ignore[reportMissingParameterType]
        dtheta=...,  # pyright: ignore[reportMissingParameterType]
        fill: str = ...,
        fillcolor: str = ...,
        hoverinfo: str | Sequence[str] = ...,
        hoverinfosrc: str = ...,
        hoverlabel: scatterpolargl.Hoverlabel | dict[str, Any] = ...,
        hovertemplate: str
        | float
        | Sequence[str]
        | Sequence[float]
        | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        hovertemplatesrc: str = ...,
        hovertext: str
        | float
        | Sequence[str]
        | Sequence[float]
        | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        hovertextsrc: str = ...,
        ids: Sequence[str] | np.ndarray[tuple[int, ...], np.dtype[np.str_]] | pd.Series[str] = ...,
        idssrc: str = ...,
        legend: str = ...,
        legendgroup: str | int = ...,
        legendgrouptitle: scatterpolargl.Legendgrouptitle | dict[str, Any] = ...,
        legendrank: int | float = ...,
        legendwidth: int | float = ...,
        line: scatterpolargl.Line | dict[str, str | int | float] = ...,
        marker: scatterpolargl.Marker | dict[str, Any] = ...,
        meta: Sequence[Any] | dict[str, Any] | np.ndarray[tuple[int, ...], Any] = ...,
        metasrc: str = ...,
        mode: str = ...,
        name: str | int = ...,
        opacity: int | float = ...,
        r=...,  # pyright: ignore[reportMissingParameterType]
        r0=...,  # pyright: ignore[reportMissingParameterType]
        rsrc: str = ...,
        selected: scatterpolargl.Selected
        | dict[str, scatterpolargl.selected.Marker | scatterpolargl.selected.Textfont | dict[str, Any]] = ...,
        selectedpoints: Sequence[int] = ...,
        showlegend: bool = ...,
        stream: scatterpolargl.Stream | dict[str, int | str] = ...,
        subplot=...,  # pyright: ignore[reportMissingParameterType]
        text: str | float | Sequence[str] | Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        textfont: scatterpolargl.Textfont | dict[str, Any] = ...,
        textposition: str | Sequence[str] | np.ndarray[tuple[int, ...], np.dtype[np.str_]] = ...,
        textpositionsrc: str = ...,
        textsrc: str = ...,
        texttemplate: str = ...,
        texttemplatesrc: str = ...,
        theta=...,  # pyright: ignore[reportMissingParameterType]
        theta0=...,  # pyright: ignore[reportMissingParameterType]
        thetasrc: str = ...,
        thetaunit=...,  # pyright: ignore[reportMissingParameterType]
        uid: str | int = ...,
        uirevision: Hashable = ...,
        unselected: scatterpolargl.Unselected
        | dict[str, scatterpolargl.unselected.Marker | scatterpolargl.unselected.Textfont | dict[str, Any]] = ...,
        visible: bool | str = ...,
        row=...,  # pyright: ignore[reportMissingParameterType]
        col=...,  # pyright: ignore[reportMissingParameterType]
        **kwargs: Any,
    ) -> Figure: ...
    def add_scattersmith(
        self,
        cliponaxis: bool = ...,
        connectgaps: bool = ...,
        customdata: Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] | pd.Series[float] = ...,
        customdatasrc: str = ...,
        fill: str = ...,
        fillcolor: str = ...,
        hoverinfo: str | Sequence[str] = ...,
        hoverinfosrc: str = ...,
        hoverlabel: scattersmith.Hoverlabel | dict[str, Any] = ...,
        hoveron: str = ...,
        hovertemplate: str
        | float
        | Sequence[str]
        | Sequence[float]
        | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        hovertemplatesrc: str = ...,
        hovertext: str
        | float
        | Sequence[str]
        | Sequence[float]
        | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        hovertextsrc: str = ...,
        ids: Sequence[str] | np.ndarray[tuple[int, ...], np.dtype[np.str_]] | pd.Series[str] = ...,
        idssrc: str = ...,
        imag=...,  # pyright: ignore[reportMissingParameterType]
        imagsrc: str = ...,
        legend: str = ...,
        legendgroup: str | int = ...,
        legendgrouptitle: scattersmith.Legendgrouptitle | dict[str, Any] = ...,
        legendrank: int | float = ...,
        legendwidth: int | float = ...,
        line: scattersmith.Line | dict[str, str | int | float] = ...,
        marker: scattersmith.Marker | dict[str, Any] = ...,
        meta: Sequence[Any] | dict[str, Any] | np.ndarray[tuple[int, ...], Any] = ...,
        metasrc: str = ...,
        mode: str = ...,
        name: str | int = ...,
        opacity: int | float = ...,
        real=...,  # pyright: ignore[reportMissingParameterType]
        realsrc: str = ...,
        selected: scattersmith.Selected
        | dict[str, scattersmith.selected.Marker | scattersmith.selected.Textfont | dict[str, Any]] = ...,
        selectedpoints: Sequence[int] = ...,
        showlegend: bool = ...,
        stream: scattersmith.Stream | dict[str, int | str] = ...,
        subplot=...,  # pyright: ignore[reportMissingParameterType]
        text: str | float | Sequence[str] | Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        textfont: scattersmith.Textfont | dict[str, Any] = ...,
        textposition: str | Sequence[str] | np.ndarray[tuple[int, ...], np.dtype[np.str_]] = ...,
        textpositionsrc: str = ...,
        textsrc: str = ...,
        texttemplate: str = ...,
        texttemplatesrc: str = ...,
        uid: str | int = ...,
        uirevision: Hashable = ...,
        unselected: scattersmith.Unselected
        | dict[str, scattersmith.unselected.Marker | scattersmith.unselected.Textfont | dict[str, Any]] = ...,
        visible: bool | str = ...,
        row=...,  # pyright: ignore[reportMissingParameterType]
        col=...,  # pyright: ignore[reportMissingParameterType]
        **kwargs: Any,
    ) -> Figure: ...
    def add_scatterternary(
        self,
        a=...,  # pyright: ignore[reportMissingParameterType]
        asrc: str = ...,
        b=...,  # pyright: ignore[reportMissingParameterType]
        bsrc: str = ...,
        c=...,  # pyright: ignore[reportMissingParameterType]
        cliponaxis: bool = ...,
        connectgaps: bool = ...,
        csrc: str = ...,
        customdata: Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] | pd.Series[float] = ...,
        customdatasrc: str = ...,
        fill: str = ...,
        fillcolor: str = ...,
        hoverinfo: str | Sequence[str] = ...,
        hoverinfosrc: str = ...,
        hoverlabel: scatterternary.Hoverlabel | dict[str, Any] = ...,
        hoveron: str = ...,
        hovertemplate: str
        | float
        | Sequence[str]
        | Sequence[float]
        | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        hovertemplatesrc: str = ...,
        hovertext: str
        | float
        | Sequence[str]
        | Sequence[float]
        | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        hovertextsrc: str = ...,
        ids: Sequence[str] | np.ndarray[tuple[int, ...], np.dtype[np.str_]] | pd.Series[str] = ...,
        idssrc: str = ...,
        legend: str = ...,
        legendgroup: str | int = ...,
        legendgrouptitle: scatterternary.Legendgrouptitle | dict[str, Any] = ...,
        legendrank: int | float = ...,
        legendwidth: int | float = ...,
        line: scatterternary.Line | dict[str, str | int | float] = ...,
        marker: scatterternary.Marker | dict[str, Any] = ...,
        meta: Sequence[Any] | dict[str, Any] | np.ndarray[tuple[int, ...], Any] = ...,
        metasrc: str = ...,
        mode: str = ...,
        name: str | int = ...,
        opacity: int | float = ...,
        selected: scatterternary.Selected
        | dict[str, scatterternary.selected.Marker | scatterternary.selected.Textfont | dict[str, Any]] = ...,
        selectedpoints: Sequence[int] = ...,
        showlegend: bool = ...,
        stream: scatterternary.Stream | dict[str, int | str] = ...,
        subplot=...,  # pyright: ignore[reportMissingParameterType]
        sum=...,  # pyright: ignore[reportMissingParameterType]
        text: str | float | Sequence[str] | Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        textfont: scatterternary.Textfont | dict[str, Any] = ...,
        textposition: str | Sequence[str] | np.ndarray[tuple[int, ...], np.dtype[np.str_]] = ...,
        textpositionsrc: str = ...,
        textsrc: str = ...,
        texttemplate: str = ...,
        texttemplatesrc: str = ...,
        uid: str | int = ...,
        uirevision: Hashable = ...,
        unselected: scatterternary.Unselected
        | dict[str, scatterternary.unselected.Marker | scatterternary.unselected.Textfont | dict[str, Any]] = ...,
        visible: bool | str = ...,
        row=...,  # pyright: ignore[reportMissingParameterType]
        col=...,  # pyright: ignore[reportMissingParameterType]
        **kwargs: Any,
    ) -> Figure: ...
    def add_splom(
        self,
        customdata: Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] | pd.Series[float] = ...,
        customdatasrc: str = ...,
        diagonal=...,  # pyright: ignore[reportMissingParameterType]
        dimensions=...,  # pyright: ignore[reportMissingParameterType]
        dimensiondefaults=...,  # pyright: ignore[reportMissingParameterType]
        hoverinfo: str | Sequence[str] = ...,
        hoverinfosrc: str = ...,
        hoverlabel: splom.Hoverlabel | dict[str, Any] = ...,
        hovertemplate: str
        | float
        | Sequence[str]
        | Sequence[float]
        | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        hovertemplatesrc: str = ...,
        hovertext: str
        | float
        | Sequence[str]
        | Sequence[float]
        | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        hovertextsrc: str = ...,
        ids: Sequence[str] | np.ndarray[tuple[int, ...], np.dtype[np.str_]] | pd.Series[str] = ...,
        idssrc: str = ...,
        legend: str = ...,
        legendgroup: str | int = ...,
        legendgrouptitle: splom.Legendgrouptitle | dict[str, Any] = ...,
        legendrank: int | float = ...,
        legendwidth: int | float = ...,
        marker: splom.Marker | dict[str, Any] = ...,
        meta: Sequence[Any] | dict[str, Any] | np.ndarray[tuple[int, ...], Any] = ...,
        metasrc: str = ...,
        name: str | int = ...,
        opacity: int | float = ...,
        selected: splom.Selected | dict[str, splom.selected.Marker | dict[str, Any]] = ...,
        selectedpoints: Sequence[int] = ...,
        showlegend: bool = ...,
        showlowerhalf=...,  # pyright: ignore[reportMissingParameterType]
        showupperhalf=...,  # pyright: ignore[reportMissingParameterType]
        stream: splom.Stream | dict[str, int | str] = ...,
        text: str | float | Sequence[str] | Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        textsrc: str = ...,
        uid: str | int = ...,
        uirevision: Hashable = ...,
        unselected: splom.Unselected | dict[str, splom.unselected.Marker | dict[str, Any]] = ...,
        visible: bool | str = ...,
        xaxes=...,  # pyright: ignore[reportMissingParameterType]
        xhoverformat: str = ...,
        yaxes=...,  # pyright: ignore[reportMissingParameterType]
        yhoverformat: str = ...,
        row=...,  # pyright: ignore[reportMissingParameterType]
        col=...,  # pyright: ignore[reportMissingParameterType]
        **kwargs: Any,
    ) -> Figure: ...
    def add_streamtube(
        self,
        autocolorscale: bool = ...,
        cauto: bool = ...,
        cmax: int | float = ...,
        cmid: int | float = ...,
        cmin: int | float = ...,
        coloraxis: str = ...,
        colorbar: streamtube.ColorBar | dict[str, Any] = ...,
        colorscale: str | list[str] | list[tuple[float, str]] = ...,
        customdata: Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] | pd.Series[float] = ...,
        customdatasrc: str = ...,
        hoverinfo: str | Sequence[str] = ...,
        hoverinfosrc: str = ...,
        hoverlabel: streamtube.Hoverlabel | dict[str, Any] = ...,
        hovertemplate: str
        | float
        | Sequence[str]
        | Sequence[float]
        | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        hovertemplatesrc: str = ...,
        hovertext: str
        | float
        | Sequence[str]
        | Sequence[float]
        | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        ids: Sequence[str] | np.ndarray[tuple[int, ...], np.dtype[np.str_]] | pd.Series[str] = ...,
        idssrc: str = ...,
        legend: str = ...,
        legendgroup: str | int = ...,
        legendgrouptitle: streamtube.Legendgrouptitle | dict[str, Any] = ...,
        legendrank: int | float = ...,
        legendwidth: int | float = ...,
        lighting: streamtube.Lighting | dict[str, Any] = ...,
        lightposition: streamtube.Lightposition
        | dict[str, Sequence[int] | Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]]] = ...,
        maxdisplayed=...,  # pyright: ignore[reportMissingParameterType]
        meta: Sequence[Any] | dict[str, Any] | np.ndarray[tuple[int, ...], Any] = ...,
        metasrc: str = ...,
        name: str | int = ...,
        opacity: int | float = ...,
        reversescale: bool = ...,
        scene: str = ...,
        showlegend: bool = ...,
        showscale: bool = ...,
        sizeref=...,  # pyright: ignore[reportMissingParameterType]
        starts=...,  # pyright: ignore[reportMissingParameterType]
        stream: streamtube.Stream | dict[str, int | str] = ...,
        text: str | float | Sequence[str] | Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        u=...,  # pyright: ignore[reportMissingParameterType]
        uhoverformat: str = ...,
        uid: str | int = ...,
        uirevision: Hashable = ...,
        usrc: str = ...,
        v=...,  # pyright: ignore[reportMissingParameterType]
        vhoverformat: str = ...,
        visible: bool | str = ...,
        vsrc: str = ...,
        w=...,  # pyright: ignore[reportMissingParameterType]
        whoverformat: str = ...,
        wsrc: str = ...,
        x=...,  # pyright: ignore[reportMissingParameterType]
        xhoverformat: str = ...,
        xsrc: str = ...,
        y=...,  # pyright: ignore[reportMissingParameterType]
        yhoverformat: str = ...,
        ysrc: str = ...,
        z=...,  # pyright: ignore[reportMissingParameterType]
        zhoverformat: str = ...,
        zsrc: str = ...,
        row=...,  # pyright: ignore[reportMissingParameterType]
        col=...,  # pyright: ignore[reportMissingParameterType]
        **kwargs: Any,
    ) -> Figure: ...
    def add_sunburst(
        self,
        branchvalues=...,  # pyright: ignore[reportMissingParameterType]
        count=...,  # pyright: ignore[reportMissingParameterType]
        customdata: Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] | pd.Series[float] = ...,
        customdatasrc: str = ...,
        domain=...,  # pyright: ignore[reportMissingParameterType]
        hoverinfo: str | Sequence[str] = ...,
        hoverinfosrc: str = ...,
        hoverlabel: sunburst.Hoverlabel | dict[str, Any] = ...,
        hovertemplate: str
        | float
        | Sequence[str]
        | Sequence[float]
        | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        hovertemplatesrc: str = ...,
        hovertext: str
        | float
        | Sequence[str]
        | Sequence[float]
        | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        hovertextsrc: str = ...,
        ids: Sequence[str] | np.ndarray[tuple[int, ...], np.dtype[np.str_]] | pd.Series[str] = ...,
        idssrc: str = ...,
        insidetextfont=...,  # pyright: ignore[reportMissingParameterType]
        insidetextorientation=...,  # pyright: ignore[reportMissingParameterType]
        labels=...,  # pyright: ignore[reportMissingParameterType]
        labelssrc: str = ...,
        leaf=...,  # pyright: ignore[reportMissingParameterType]
        legend: str = ...,
        legendgrouptitle: sunburst.Legendgrouptitle | dict[str, Any] = ...,
        legendrank: int | float = ...,
        legendwidth: int | float = ...,
        level=...,  # pyright: ignore[reportMissingParameterType]
        marker: sunburst.Marker | dict[str, Any] = ...,
        maxdepth=...,  # pyright: ignore[reportMissingParameterType]
        meta: Sequence[Any] | dict[str, Any] | np.ndarray[tuple[int, ...], Any] = ...,
        metasrc: str = ...,
        name: str | int = ...,
        opacity: int | float = ...,
        outsidetextfont=...,  # pyright: ignore[reportMissingParameterType]
        parents=...,  # pyright: ignore[reportMissingParameterType]
        parentssrc: str = ...,
        root=...,  # pyright: ignore[reportMissingParameterType]
        rotation=...,  # pyright: ignore[reportMissingParameterType]
        sort=...,  # pyright: ignore[reportMissingParameterType]
        stream: sunburst.Stream | dict[str, int | str] = ...,
        text: str | float | Sequence[str] | Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        textfont: sunburst.Textfont | dict[str, Any] = ...,
        textinfo=...,  # pyright: ignore[reportMissingParameterType]
        textsrc: str = ...,
        texttemplate: str = ...,
        texttemplatesrc: str = ...,
        uid: str | int = ...,
        uirevision: Hashable = ...,
        values=...,  # pyright: ignore[reportMissingParameterType]
        valuessrc: str = ...,
        visible: bool | str = ...,
        row=...,  # pyright: ignore[reportMissingParameterType]
        col=...,  # pyright: ignore[reportMissingParameterType]
        **kwargs: Any,
    ) -> Figure: ...
    def add_surface(
        self,
        autocolorscale: bool = ...,
        cauto: bool = ...,
        cmax: int | float = ...,
        cmid: int | float = ...,
        cmin: int | float = ...,
        coloraxis: str = ...,
        colorbar: surface.ColorBar | dict[str, Any] = ...,
        colorscale: str | list[str] | list[tuple[float, str]] = ...,
        connectgaps: bool = ...,
        contours: surface.Contours | dict[str, Any] = ...,
        customdata: Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] | pd.Series[float] = ...,
        customdatasrc: str = ...,
        hidesurface: bool = ...,
        hoverinfo: str | Sequence[str] = ...,
        hoverinfosrc: str = ...,
        hoverlabel: surface.Hoverlabel | dict[str, Any] = ...,
        hovertemplate: str
        | float
        | Sequence[str]
        | Sequence[float]
        | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        hovertemplatesrc: str = ...,
        hovertext: str
        | float
        | Sequence[str]
        | Sequence[float]
        | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        hovertextsrc: str = ...,
        ids: Sequence[str] | np.ndarray[tuple[int, ...], np.dtype[np.str_]] | pd.Series[str] = ...,
        idssrc: str = ...,
        legend: str = ...,
        legendgroup: str | int = ...,
        legendgrouptitle: surface.Legendgrouptitle | dict[str, Any] = ...,
        legendrank: int | float = ...,
        legendwidth: int | float = ...,
        lighting: surface.Lighting | dict[str, Any] = ...,
        lightposition: surface.Lightposition
        | dict[str, Sequence[int] | Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]]] = ...,
        meta: Sequence[Any] | dict[str, Any] | np.ndarray[tuple[int, ...], Any] = ...,
        metasrc: str = ...,
        name: str | int = ...,
        opacity: int | float = ...,
        opacityscale: str | list[tuple[float, float]] = ...,
        reversescale: bool = ...,
        scene: str = ...,
        showlegend: bool = ...,
        showscale: bool = ...,
        stream: surface.Stream | dict[str, int | str] = ...,
        surfacecolor: Sequence[str] | np.ndarray[tuple[int, ...], np.dtype[np.str_]] | pd.Series[str] = ...,
        surfacecolorsrc: str = ...,
        text: str | float | Sequence[str] | Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        textsrc: str = ...,
        uid: str | int = ...,
        uirevision: Hashable = ...,
        visible: bool | str = ...,
        x: Sequence[int] | Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] | pd.Series[float] = ...,
        xcalendar: str = ...,
        xhoverformat: str = ...,
        xsrc: str = ...,
        y: Sequence[int] | Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] | pd.Series[float] = ...,
        ycalendar: str = ...,
        yhoverformat: str = ...,
        ysrc: str = ...,
        z: Sequence[int] | Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] | pd.Series[float] = ...,
        zcalendar: str = ...,
        zhoverformat: str = ...,
        zsrc: str = ...,
        row: int | str | None = ...,
        col: int | str | None = ...,
        **kwargs: Any,
    ) -> Figure: ...
    def add_table(
        self,
        cells=...,  # pyright: ignore[reportMissingParameterType]
        columnorder=...,  # pyright: ignore[reportMissingParameterType]
        columnordersrc: str = ...,
        columnwidth=...,  # pyright: ignore[reportMissingParameterType]
        columnwidthsrc: str = ...,
        customdata: Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] | pd.Series[float] = ...,
        customdatasrc: str = ...,
        domain=...,  # pyright: ignore[reportMissingParameterType]
        header=...,  # pyright: ignore[reportMissingParameterType]
        hoverinfo: str | Sequence[str] = ...,
        hoverinfosrc: str = ...,
        hoverlabel: table.Hoverlabel | dict[str, Any] = ...,
        ids: Sequence[str] | np.ndarray[tuple[int, ...], np.dtype[np.str_]] | pd.Series[str] = ...,
        idssrc: str = ...,
        legend: str = ...,
        legendgrouptitle: table.Legendgrouptitle | dict[str, Any] = ...,
        legendrank: int | float = ...,
        legendwidth: int | float = ...,
        meta: Sequence[Any] | dict[str, Any] | np.ndarray[tuple[int, ...], Any] = ...,
        metasrc: str = ...,
        name: str | int = ...,
        stream: table.Stream | dict[str, int | str] = ...,
        uid: str | int = ...,
        uirevision: Hashable = ...,
        visible: bool | str = ...,
        row=...,  # pyright: ignore[reportMissingParameterType]
        col=...,  # pyright: ignore[reportMissingParameterType]
        **kwargs: Any,
    ) -> Figure: ...
    def add_treemap(
        self,
        branchvalues=...,  # pyright: ignore[reportMissingParameterType]
        count=...,  # pyright: ignore[reportMissingParameterType]
        customdata: Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] | pd.Series[float] = ...,
        customdatasrc: str = ...,
        domain=...,  # pyright: ignore[reportMissingParameterType]
        hoverinfo: str | Sequence[str] = ...,
        hoverinfosrc: str = ...,
        hoverlabel: treemap.Hoverlabel | dict[str, Any] = ...,
        hovertemplate: str
        | float
        | Sequence[str]
        | Sequence[float]
        | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        hovertemplatesrc: str = ...,
        hovertext: str
        | float
        | Sequence[str]
        | Sequence[float]
        | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        hovertextsrc: str = ...,
        ids: Sequence[str] | np.ndarray[tuple[int, ...], np.dtype[np.str_]] | pd.Series[str] = ...,
        idssrc: str = ...,
        insidetextfont=...,  # pyright: ignore[reportMissingParameterType]
        labels=...,  # pyright: ignore[reportMissingParameterType]
        labelssrc: str = ...,
        legend: str = ...,
        legendgrouptitle: treemap.Legendgrouptitle | dict[str, Any] = ...,
        legendrank: int | float = ...,
        legendwidth: int | float = ...,
        level=...,  # pyright: ignore[reportMissingParameterType]
        marker: treemap.Marker | dict[str, Any] = ...,
        maxdepth=...,  # pyright: ignore[reportMissingParameterType]
        meta: Sequence[Any] | dict[str, Any] | np.ndarray[tuple[int, ...], Any] = ...,
        metasrc: str = ...,
        name: str | int = ...,
        opacity: int | float = ...,
        outsidetextfont=...,  # pyright: ignore[reportMissingParameterType]
        parents=...,  # pyright: ignore[reportMissingParameterType]
        parentssrc: str = ...,
        pathbar=...,  # pyright: ignore[reportMissingParameterType]
        root=...,  # pyright: ignore[reportMissingParameterType]
        sort=...,  # pyright: ignore[reportMissingParameterType]
        stream: treemap.Stream | dict[str, int | str] = ...,
        text: str | float | Sequence[str] | Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        textfont: treemap.Textfont | dict[str, Any] = ...,
        textinfo=...,  # pyright: ignore[reportMissingParameterType]
        textposition: str | Sequence[str] | np.ndarray[tuple[int, ...], np.dtype[np.str_]] = ...,
        textsrc: str = ...,
        texttemplate: str = ...,
        texttemplatesrc: str = ...,
        tiling=...,  # pyright: ignore[reportMissingParameterType]
        uid: str | int = ...,
        uirevision: Hashable = ...,
        values=...,  # pyright: ignore[reportMissingParameterType]
        valuessrc: str = ...,
        visible: bool | str = ...,
        row=...,  # pyright: ignore[reportMissingParameterType]
        col=...,  # pyright: ignore[reportMissingParameterType]
        **kwargs: Any,
    ) -> Figure: ...
    def add_violin(
        self,
        alignmentgroup: str | int = ...,
        bandwidth=...,  # pyright: ignore[reportMissingParameterType]
        box=...,  # pyright: ignore[reportMissingParameterType]
        customdata: Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] | pd.Series[float] = ...,
        customdatasrc: str = ...,
        fillcolor: str = ...,
        hoverinfo: str | Sequence[str] = ...,
        hoverinfosrc: str = ...,
        hoverlabel: violin.Hoverlabel | dict[str, Any] = ...,
        hoveron: str = ...,
        hovertemplate: str
        | float
        | Sequence[str]
        | Sequence[float]
        | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        hovertemplatesrc: str = ...,
        hovertext: str
        | float
        | Sequence[str]
        | Sequence[float]
        | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        hovertextsrc: str = ...,
        ids: Sequence[str] | np.ndarray[tuple[int, ...], np.dtype[np.str_]] | pd.Series[str] = ...,
        idssrc: str = ...,
        jitter=...,  # pyright: ignore[reportMissingParameterType]
        legend: str = ...,
        legendgroup: str | int = ...,
        legendgrouptitle: violin.Legendgrouptitle | dict[str, Any] = ...,
        legendrank: int | float = ...,
        legendwidth: int | float = ...,
        line: violin.Line | dict[str, str | int | float] = ...,
        marker: violin.Marker | dict[str, Any] = ...,
        meanline=...,  # pyright: ignore[reportMissingParameterType]
        meta: Sequence[Any] | dict[str, Any] | np.ndarray[tuple[int, ...], Any] = ...,
        metasrc: str = ...,
        name: str | int = ...,
        offsetgroup: str | int = ...,
        opacity: int | float = ...,
        orientation: str = ...,
        pointpos=...,  # pyright: ignore[reportMissingParameterType]
        points=...,  # pyright: ignore[reportMissingParameterType]
        quartilemethod=...,  # pyright: ignore[reportMissingParameterType]
        scalegroup=...,  # pyright: ignore[reportMissingParameterType]
        scalemode=...,  # pyright: ignore[reportMissingParameterType]
        selected: violin.Selected | dict[str, violin.selected.Marker | dict[str, Any]] = ...,
        selectedpoints: Sequence[int] = ...,
        showlegend: bool = ...,
        side=...,  # pyright: ignore[reportMissingParameterType]
        span=...,  # pyright: ignore[reportMissingParameterType]
        spanmode=...,  # pyright: ignore[reportMissingParameterType]
        stream: violin.Stream | dict[str, int | str] = ...,
        text: str | float | Sequence[str] | Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        textsrc: str = ...,
        uid: str | int = ...,
        uirevision: Hashable = ...,
        unselected: violin.Unselected | dict[str, violin.unselected.Marker | dict[str, Any]] = ...,
        visible: bool | str = ...,
        width=...,  # pyright: ignore[reportMissingParameterType]
        x=...,  # pyright: ignore[reportMissingParameterType]
        x0: int | float = ...,
        xaxis: str = ...,
        xhoverformat: str = ...,
        xsrc: str = ...,
        y=...,  # pyright: ignore[reportMissingParameterType]
        y0: int | float = ...,
        yaxis: str = ...,
        yhoverformat: str = ...,
        ysrc: str = ...,
        zorder: int = ...,
        row=...,  # pyright: ignore[reportMissingParameterType]
        col=...,  # pyright: ignore[reportMissingParameterType]
        secondary_y: bool | None = ...,
        **kwargs: Any,
    ) -> Figure: ...
    def add_volume(
        self,
        autocolorscale: bool = ...,
        caps=...,  # pyright: ignore[reportMissingParameterType]
        cauto: bool = ...,
        cmax: int | float = ...,
        cmid: int | float = ...,
        cmin: int | float = ...,
        coloraxis: str = ...,
        colorbar: volume.ColorBar | dict[str, Any] = ...,
        colorscale: str | list[str] | list[tuple[float, str]] = ...,
        contour=...,  # pyright: ignore[reportMissingParameterType]
        customdata: Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] | pd.Series[float] = ...,
        customdatasrc: str = ...,
        flatshading=...,  # pyright: ignore[reportMissingParameterType]
        hoverinfo: str | Sequence[str] = ...,
        hoverinfosrc: str = ...,
        hoverlabel: volume.Hoverlabel | dict[str, Any] = ...,
        hovertemplate: str
        | float
        | Sequence[str]
        | Sequence[float]
        | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        hovertemplatesrc: str = ...,
        hovertext: str
        | float
        | Sequence[str]
        | Sequence[float]
        | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        hovertextsrc: str = ...,
        ids: Sequence[str] | np.ndarray[tuple[int, ...], np.dtype[np.str_]] | pd.Series[str] = ...,
        idssrc: str = ...,
        isomax=...,  # pyright: ignore[reportMissingParameterType]
        isomin=...,  # pyright: ignore[reportMissingParameterType]
        legend: str = ...,
        legendgroup: str | int = ...,
        legendgrouptitle: volume.Legendgrouptitle | dict[str, Any] = ...,
        legendrank: int | float = ...,
        legendwidth: int | float = ...,
        lighting: volume.Lighting | dict[str, Any] = ...,
        lightposition: volume.Lightposition
        | dict[str, Sequence[int] | Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]]] = ...,
        meta: Sequence[Any] | dict[str, Any] | np.ndarray[tuple[int, ...], Any] = ...,
        metasrc: str = ...,
        name: str | int = ...,
        opacity: int | float = ...,
        opacityscale: str | list[tuple[float, float]] = ...,
        reversescale: bool = ...,
        scene: str = ...,
        showlegend: bool = ...,
        showscale: bool = ...,
        slices=...,  # pyright: ignore[reportMissingParameterType]
        spaceframe=...,  # pyright: ignore[reportMissingParameterType]
        stream: volume.Stream | dict[str, int | str] = ...,
        surface=...,  # pyright: ignore[reportMissingParameterType]
        text: str | float | Sequence[str] | Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        textsrc: str = ...,
        uid: str | int = ...,
        uirevision: Hashable = ...,
        value=...,  # pyright: ignore[reportMissingParameterType]
        valuehoverformat: str = ...,
        valuesrc: str = ...,
        visible: bool | str = ...,
        x=...,  # pyright: ignore[reportMissingParameterType]
        xhoverformat: str = ...,
        xsrc: str = ...,
        y=...,  # pyright: ignore[reportMissingParameterType]
        yhoverformat: str = ...,
        ysrc: str = ...,
        z=...,  # pyright: ignore[reportMissingParameterType]
        zhoverformat: str = ...,
        zsrc: str = ...,
        row=...,  # pyright: ignore[reportMissingParameterType]
        col=...,  # pyright: ignore[reportMissingParameterType]
        **kwargs: Any,
    ) -> Figure: ...
    def add_waterfall(
        self,
        alignmentgroup: str | int = ...,
        base=...,  # pyright: ignore[reportMissingParameterType]
        cliponaxis: bool = ...,
        connector=...,  # pyright: ignore[reportMissingParameterType]
        constraintext=...,  # pyright: ignore[reportMissingParameterType]
        customdata: Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] | pd.Series[float] = ...,
        customdatasrc: str = ...,
        decreasing=...,  # pyright: ignore[reportMissingParameterType]
        dx: int | float = ...,
        dy: int | float = ...,
        hoverinfo: str | Sequence[str] = ...,
        hoverinfosrc: str = ...,
        hoverlabel: waterfall.Hoverlabel | dict[str, Any] = ...,
        hovertemplate: str
        | float
        | Sequence[str]
        | Sequence[float]
        | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        hovertemplatesrc: str = ...,
        hovertext: str
        | float
        | Sequence[str]
        | Sequence[float]
        | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        hovertextsrc: str = ...,
        ids: Sequence[str] | np.ndarray[tuple[int, ...], np.dtype[np.str_]] | pd.Series[str] = ...,
        idssrc: str = ...,
        increasing=...,  # pyright: ignore[reportMissingParameterType]
        insidetextanchor=...,  # pyright: ignore[reportMissingParameterType]
        insidetextfont=...,  # pyright: ignore[reportMissingParameterType]
        legend: str = ...,
        legendgroup: str | int = ...,
        legendgrouptitle: waterfall.Legendgrouptitle | dict[str, Any] = ...,
        legendrank: int | float = ...,
        legendwidth: int | float = ...,
        measure=...,  # pyright: ignore[reportMissingParameterType]
        measuresrc: str = ...,
        meta: Sequence[Any] | dict[str, Any] | np.ndarray[tuple[int, ...], Any] = ...,
        metasrc: str = ...,
        name: str | int = ...,
        offset=...,  # pyright: ignore[reportMissingParameterType]
        offsetgroup: str | int = ...,
        offsetsrc: str = ...,
        opacity: int | float = ...,
        orientation: str = ...,
        outsidetextfont=...,  # pyright: ignore[reportMissingParameterType]
        selectedpoints: Sequence[int] = ...,
        showlegend: bool = ...,
        stream: waterfall.Stream | dict[str, int | str] = ...,
        text: str | float | Sequence[str] | Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        textangle: int | float = ...,
        textfont: waterfall.Textfont | dict[str, Any] = ...,
        textinfo=...,  # pyright: ignore[reportMissingParameterType]
        textposition: str | Sequence[str] | np.ndarray[tuple[int, ...], np.dtype[np.str_]] = ...,
        textpositionsrc: str = ...,
        textsrc: str = ...,
        texttemplate: str = ...,
        texttemplatesrc: str = ...,
        totals=...,  # pyright: ignore[reportMissingParameterType]
        uid: str | int = ...,
        uirevision: Hashable = ...,
        visible: bool | str = ...,
        width=...,  # pyright: ignore[reportMissingParameterType]
        widthsrc: str = ...,
        x=...,  # pyright: ignore[reportMissingParameterType]
        x0: int | float = ...,
        xaxis: str = ...,
        xhoverformat: str = ...,
        xperiod: int | float | str = ...,
        xperiod0: int | float | str = ...,
        xperiodalignment: str = ...,
        xsrc: str = ...,
        y=...,  # pyright: ignore[reportMissingParameterType]
        y0: int | float = ...,
        yaxis: str = ...,
        yhoverformat: str = ...,
        yperiod: int | float | str = ...,
        yperiod0: int | float | str = ...,
        yperiodalignment: str = ...,
        ysrc: str = ...,
        zorder: int = ...,
        row=...,  # pyright: ignore[reportMissingParameterType]
        col=...,  # pyright: ignore[reportMissingParameterType]
        secondary_y: bool | None = ...,
        **kwargs: Any,
    ) -> Figure: ...
    def select_coloraxes(
        self,
        selector: dict[str, Any] | Callable[[BaseLayoutHierarchyType], bool] | None = ...,
        row: int | None = ...,
        col: int | None = ...,
    ) -> Generator[layout.Coloraxis, None, None]:  # -> Generator[Any, Any, None]:
        ...
    def for_each_coloraxis(
        self,
        fn: Callable[[layout.Coloraxis], Any],
        selector: dict[str, Any] | Callable[[BaseLayoutHierarchyType], bool] | None = ...,
        row: int | None = ...,
        col: int | None = ...,
    ) -> Figure: ...
    def update_coloraxes(
        self,
        patch: dict[str, Any] = ...,
        selector: dict[str, Any] | Callable[[BaseLayoutHierarchyType], bool] | None = ...,
        overwrite: bool = ...,
        row: int | None = ...,
        col: int | None = ...,
        **kwargs: Any,
    ) -> Figure: ...
    def select_geos(
        self,
        selector: dict[str, Any] | Callable[[BaseLayoutHierarchyType], bool] | None = ...,
        row: int | None = ...,
        col: int | None = ...,
    ) -> Generator[layout.Geo, None, None]:  # -> Generator[Any, Any, None]:
        ...
    def for_each_geo(
        self,
        fn: Callable[[layout.Geo], Any],
        selector: dict[str, Any] | Callable[[BaseLayoutHierarchyType], bool] | None = ...,
        row: int | None = ...,
        col: int | None = ...,
    ) -> Figure: ...
    def update_geos(
        self,
        patch: dict[str, Any] = ...,
        selector: dict[str, Any] | Callable[[BaseLayoutHierarchyType], bool] | None = ...,
        overwrite: bool = ...,
        row: int | None = ...,
        col: int | None = ...,
        **kwargs: Any,
    ) -> Figure: ...
    def select_legends(
        self,
        selector: dict[str, Any] | Callable[[BaseLayoutHierarchyType], bool] | None = ...,
        row: int | None = ...,
        col: int | None = ...,
    ) -> Generator[layout.Legend, None, None]:  # -> Generator[Any, Any, None]:
        ...
    def for_each_legend(
        self,
        fn: Callable[[layout.Legend], Any],
        selector: dict[str, Any] | Callable[[BaseLayoutHierarchyType], bool] | None = ...,
        row: int | None = ...,
        col: int | None = ...,
    ) -> Figure: ...
    def update_legends(
        self,
        patch: dict[str, Any] = ...,
        selector: dict[str, Any] | Callable[[BaseLayoutHierarchyType], bool] | None = ...,
        overwrite: bool = ...,
        row: int | None = ...,
        col: int | None = ...,
        **kwargs: Any,
    ) -> Figure: ...
    def select_maps(
        self,
        selector: dict[str, Any] | Callable[[BaseLayoutHierarchyType], bool] | None = ...,
        row: int | None = ...,
        col: int | None = ...,
    ) -> Generator[layout.Map, None, None]:  # -> Generator[Any, Any, None]:
        ...
    def for_each_map(
        self,
        fn: Callable[[layout.Map], Any],
        selector: dict[str, Any] | Callable[[BaseLayoutHierarchyType], bool] | None = ...,
        row: int | None = ...,
        col: int | None = ...,
    ) -> Figure: ...
    def update_maps(
        self,
        patch: dict[str, Any] = ...,
        selector: dict[str, Any] | Callable[[BaseLayoutHierarchyType], bool] | None = ...,
        overwrite: bool = ...,
        row: int | None = ...,
        col: int | None = ...,
        **kwargs: Any,
    ) -> Figure: ...
    def select_mapboxes(
        self,
        selector: dict[str, Any] | Callable[[BaseLayoutHierarchyType], bool] | None = ...,
        row: int | None = ...,
        col: int | None = ...,
    ) -> Generator[layout.Mapbox, None, None]:  # -> Generator[Any, Any, None]:
        ...
    def for_each_mapbox(
        self,
        fn: Callable[[layout.Mapbox], Any],
        selector: dict[str, Any] | Callable[[BaseLayoutHierarchyType], bool] | None = ...,
        row: int | None = ...,
        col: int | None = ...,
    ) -> Figure: ...
    def update_mapboxes(
        self,
        patch: dict[str, Any] = ...,
        selector: dict[str, Any] | Callable[[BaseLayoutHierarchyType], bool] | None = ...,
        overwrite: bool = ...,
        row: int | None = ...,
        col: int | None = ...,
        **kwargs: Any,
    ) -> Figure: ...
    def select_polars(
        self,
        selector: dict[str, Any] | Callable[[BaseLayoutHierarchyType], bool] | None = ...,
        row: int | None = ...,
        col: int | None = ...,
    ) -> Generator[layout.Polar, None, None]:  # -> Generator[Any, Any, None]:
        ...
    def for_each_polar(
        self,
        fn: Callable[[layout.Polar], Any],
        selector: dict[str, Any] | Callable[[BaseLayoutHierarchyType], bool] | None = ...,
        row: int | None = ...,
        col: int | None = ...,
    ) -> Figure: ...
    def update_polars(
        self,
        patch: dict[str, Any] = ...,
        selector: dict[str, Any] | Callable[[BaseLayoutHierarchyType], bool] | None = ...,
        overwrite: bool = ...,
        row: int | None = ...,
        col: int | None = ...,
        **kwargs: Any,
    ) -> Figure: ...
    def select_scenes(
        self,
        selector: dict[str, Any] | Callable[[BaseLayoutHierarchyType], bool] | None = ...,
        row: int | None = ...,
        col: int | None = ...,
    ) -> Generator[layout.Scene, None, None]:  # -> Generator[Any, Any, None]:
        ...
    def for_each_scene(
        self,
        fn: Callable[[layout.Scene], Any],
        selector: dict[str, Any] | Callable[[BaseLayoutHierarchyType], bool] | None = ...,
        row: int | None = ...,
        col: int | None = ...,
    ) -> Figure: ...
    def update_scenes(
        self,
        patch: dict[str, Any] = ...,
        selector: dict[str, Any] | Callable[[BaseLayoutHierarchyType], bool] | None = ...,
        overwrite: bool = ...,
        row: int | None = ...,
        col: int | None = ...,
        **kwargs: Any,
    ) -> Figure: ...
    def select_smiths(
        self,
        selector: dict[str, Any] | Callable[[BaseLayoutHierarchyType], bool] | None = ...,
        row: int | None = ...,
        col: int | None = ...,
    ) -> Generator[layout.Smith, None, None]:  # -> Generator[Any, Any, None]:
        ...
    def for_each_smith(
        self,
        fn: Callable[[layout.Smith], Any],
        selector: dict[str, Any] | Callable[[BaseLayoutHierarchyType], bool] | None = ...,
        row: int | None = ...,
        col: int | None = ...,
    ) -> Figure: ...
    def update_smiths(
        self,
        patch: dict[str, Any] = ...,
        selector: dict[str, Any] | Callable[[BaseLayoutHierarchyType], bool] | None = ...,
        overwrite: bool = ...,
        row: int | None = ...,
        col: int | None = ...,
        **kwargs: Any,
    ) -> Figure: ...
    def select_ternaries(
        self,
        selector: dict[str, Any] | Callable[[BaseLayoutHierarchyType], bool] | None = ...,
        row: int | None = ...,
        col: int | None = ...,
    ) -> Generator[layout.Ternary, None, None]:  # -> Generator[Any, Any, None]:
        ...
    def for_each_ternary(
        self,
        fn: Callable[[layout.Ternary], Any],
        selector: dict[str, Any] | Callable[[BaseLayoutHierarchyType], bool] | None = ...,
        row: int | None = ...,
        col: int | None = ...,
    ) -> Figure: ...
    def update_ternaries(
        self,
        patch: dict[str, Any] = ...,
        selector: dict[str, Any] | Callable[[BaseLayoutHierarchyType], bool] | None = ...,
        overwrite: bool = ...,
        row: int | None = ...,
        col: int | None = ...,
        **kwargs: Any,
    ) -> Figure: ...
    def select_xaxes(
        self,
        selector: dict[str, Any] | Callable[[BaseLayoutHierarchyType], bool] | None = ...,
        row: int | None = ...,
        col: int | None = ...,
    ) -> Generator[layout.XAxis, None, None]:  # -> Generator[Any, Any, None]:
        ...
    def for_each_xaxis(
        self,
        fn: Callable[[layout.XAxis], Any],
        selector: dict[str, Any] | Callable[[BaseLayoutHierarchyType], bool] | None = ...,
        row: int | None = ...,
        col: int | None = ...,
    ) -> Figure: ...
    def update_xaxes(
        self,
        patch: dict[str, Any] = ...,
        selector: dict[str, Any] | Callable[[BaseLayoutHierarchyType], bool] | None = ...,
        overwrite: bool = ...,
        row: int | None = ...,
        col: int | None = ...,
        **kwargs: Any,
    ) -> Figure: ...
    def select_yaxes(
        self,
        selector: dict[str, Any] | Callable[[BaseLayoutHierarchyType], bool] | None = ...,
        row: int | None = ...,
        col: int | None = ...,
    ) -> Generator[layout.YAxis, None, None]:  # -> Generator[Any, Any, None]:
        ...
    def for_each_yaxis(
        self,
        fn: Callable[[layout.YAxis], Any],
        selector: dict[str, Any] | Callable[[BaseLayoutHierarchyType], bool] | None = ...,
        row: int | None = ...,
        col: int | None = ...,
    ) -> Figure: ...
    def update_yaxes(
        self,
        patch: dict[str, Any] = ...,
        selector: dict[str, Any] | Callable[[BaseLayoutHierarchyType], bool] | None = ...,
        overwrite: bool = ...,
        row: int | None = ...,
        col: int | None = ...,
        **kwargs: Any,
    ) -> Figure: ...
    def select_annotations(
        self,
        selector: dict[str, Any] | Callable[[BaseLayoutHierarchyType], bool] | int | str | None = ...,
        row: int | None = ...,
        col: int | None = ...,
        secondary_y: bool | None = ...,
    ) -> Generator[layout.Annotation, None, None]:  # -> Generator[Any, Any, None]:
        ...
    def for_each_annotation(
        self,
        fn: Callable[[layout.Annotation], Any],
        selector: dict[str, Any] | Callable[[BaseLayoutHierarchyType], bool] | int | str | None = ...,
        row: int | None = ...,
        col: int | None = ...,
        secondary_y: bool | None = ...,
    ) -> Figure: ...
    def update_annotations(
        self,
        patch: dict[str, Any] = ...,
        selector: dict[str, Any] | Callable[[BaseLayoutHierarchyType], bool] | int | str | None = ...,
        row: int | None = ...,
        col: int | None = ...,
        secondary_y: bool | None = ...,
        **kwargs: Any,
    ) -> Figure: ...
    def add_annotation(
        self,
        arg=...,  # pyright: ignore[reportMissingParameterType]
        align=...,  # pyright: ignore[reportMissingParameterType]
        arrowcolor=...,  # pyright: ignore[reportMissingParameterType]
        arrowhead=...,  # pyright: ignore[reportMissingParameterType]
        arrowside=...,  # pyright: ignore[reportMissingParameterType]
        arrowsize=...,  # pyright: ignore[reportMissingParameterType]
        arrowwidth=...,  # pyright: ignore[reportMissingParameterType]
        ax=...,  # pyright: ignore[reportMissingParameterType]
        axref=...,  # pyright: ignore[reportMissingParameterType]
        ay=...,  # pyright: ignore[reportMissingParameterType]
        ayref=...,  # pyright: ignore[reportMissingParameterType]
        bgcolor=...,  # pyright: ignore[reportMissingParameterType]
        bordercolor=...,  # pyright: ignore[reportMissingParameterType]
        borderpad=...,  # pyright: ignore[reportMissingParameterType]
        borderwidth=...,  # pyright: ignore[reportMissingParameterType]
        captureevents=...,  # pyright: ignore[reportMissingParameterType]
        clicktoshow=...,  # pyright: ignore[reportMissingParameterType]
        font=...,  # pyright: ignore[reportMissingParameterType]
        height=...,  # pyright: ignore[reportMissingParameterType]
        hoverlabel: layout.annotation.Hoverlabel | dict[str, Any] = ...,
        hovertext: str
        | float
        | Sequence[str]
        | Sequence[float]
        | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        name: str | int = ...,
        opacity: int | float = ...,
        showarrow=...,  # pyright: ignore[reportMissingParameterType]
        standoff=...,  # pyright: ignore[reportMissingParameterType]
        startarrowhead=...,  # pyright: ignore[reportMissingParameterType]
        startarrowsize=...,  # pyright: ignore[reportMissingParameterType]
        startstandoff=...,  # pyright: ignore[reportMissingParameterType]
        templateitemname=...,  # pyright: ignore[reportMissingParameterType]
        text: str | float | Sequence[str] | Sequence[float] | np.ndarray[tuple[int, ...], np.dtype[np.float64]] = ...,
        textangle: int | float = ...,
        valign=...,  # pyright: ignore[reportMissingParameterType]
        visible: bool | str = ...,
        width=...,  # pyright: ignore[reportMissingParameterType]
        x=...,  # pyright: ignore[reportMissingParameterType]
        xanchor=...,  # pyright: ignore[reportMissingParameterType]
        xclick=...,  # pyright: ignore[reportMissingParameterType]
        xref=...,  # pyright: ignore[reportMissingParameterType]
        xshift=...,  # pyright: ignore[reportMissingParameterType]
        y=...,  # pyright: ignore[reportMissingParameterType]
        yanchor=...,  # pyright: ignore[reportMissingParameterType]
        yclick=...,  # pyright: ignore[reportMissingParameterType]
        yref=...,  # pyright: ignore[reportMissingParameterType]
        yshift=...,  # pyright: ignore[reportMissingParameterType]
        row=...,  # pyright: ignore[reportMissingParameterType]
        col=...,  # pyright: ignore[reportMissingParameterType]
        secondary_y: bool | None = ...,
        exclude_empty_subplots: bool = ...,
        **kwargs: Any,
    ) -> Figure: ...
    def select_layout_images(
        self,
        selector: dict[str, Any] | Callable[[BaseLayoutHierarchyType], bool] | int | str | None = ...,
        row: int | None = ...,
        col: int | None = ...,
        secondary_y: bool | None = ...,
    ) -> Generator[layout.Image, None, None]:  # -> Generator[Any, Any, None]:
        ...
    def for_each_layout_image(
        self,
        fn: Callable[[layout.Image], Any],
        selector: dict[str, Any] | Callable[[BaseLayoutHierarchyType], bool] | int | str | None = ...,
        row: int | None = ...,
        col: int | None = ...,
        secondary_y: bool | None = ...,
    ) -> Figure: ...
    def update_layout_images(
        self,
        patch: dict[str, Any] = ...,
        selector: dict[str, Any] | Callable[[BaseLayoutHierarchyType], bool] | int | str | None = ...,
        row: int | None = ...,
        col: int | None = ...,
        secondary_y: bool | None = ...,
        **kwargs: Any,
    ) -> Figure: ...
    def add_layout_image(
        self,
        arg=...,  # pyright: ignore[reportMissingParameterType]
        layer=...,  # pyright: ignore[reportMissingParameterType]
        name: str | int = ...,
        opacity: int | float = ...,
        sizex=...,  # pyright: ignore[reportMissingParameterType]
        sizey=...,  # pyright: ignore[reportMissingParameterType]
        sizing=...,  # pyright: ignore[reportMissingParameterType]
        source=...,  # pyright: ignore[reportMissingParameterType]
        templateitemname=...,  # pyright: ignore[reportMissingParameterType]
        visible: bool | str = ...,
        x=...,  # pyright: ignore[reportMissingParameterType]
        xanchor=...,  # pyright: ignore[reportMissingParameterType]
        xref=...,  # pyright: ignore[reportMissingParameterType]
        y=...,  # pyright: ignore[reportMissingParameterType]
        yanchor=...,  # pyright: ignore[reportMissingParameterType]
        yref=...,  # pyright: ignore[reportMissingParameterType]
        row=...,  # pyright: ignore[reportMissingParameterType]
        col=...,  # pyright: ignore[reportMissingParameterType]
        secondary_y: bool | None = ...,
        exclude_empty_subplots: bool = ...,
        **kwargs: Any,
    ) -> Figure: ...
    def select_selections(
        self,
        selector: dict[str, Any] | Callable[[BaseLayoutHierarchyType], bool] | int | str | None = ...,
        row: int | None = ...,
        col: int | None = ...,
        secondary_y: bool | None = ...,
    ) -> Generator[layout.Selection, None, None]:  # -> Generator[Any, Any, None]:
        ...
    def for_each_selection(
        self,
        fn: Callable[[layout.Selection], Any],
        selector: dict[str, Any] | Callable[[BaseLayoutHierarchyType], bool] | int | str | None = ...,
        row: int | None = ...,
        col: int | None = ...,
        secondary_y: bool | None = ...,
    ) -> Figure: ...
    def update_selections(
        self,
        patch: dict[str, Any] = ...,
        selector: dict[str, Any] | Callable[[BaseLayoutHierarchyType], bool] | int | str | None = ...,
        row: int | None = ...,
        col: int | None = ...,
        secondary_y: bool | None = ...,
        **kwargs: Any,
    ) -> Figure: ...
    def add_selection(
        self,
        arg=...,  # pyright: ignore[reportMissingParameterType]
        line: layout.selection.Line | dict[str, str | int | float] = ...,
        name: str | int = ...,
        opacity: int | float = ...,
        path=...,  # pyright: ignore[reportMissingParameterType]
        templateitemname=...,  # pyright: ignore[reportMissingParameterType]
        type=...,  # pyright: ignore[reportMissingParameterType]
        x0: int | float = ...,
        x1: int | float = ...,
        xref=...,  # pyright: ignore[reportMissingParameterType]
        y0: int | float = ...,
        y1: int | float = ...,
        yref=...,  # pyright: ignore[reportMissingParameterType]
        row=...,  # pyright: ignore[reportMissingParameterType]
        col=...,  # pyright: ignore[reportMissingParameterType]
        secondary_y: bool | None = ...,
        exclude_empty_subplots: bool = ...,
        **kwargs: Any,
    ) -> Figure: ...
    def select_shapes(
        self,
        selector: dict[str, Any] | Callable[[BaseLayoutHierarchyType], bool] | int | str | None = ...,
        row: int | None = ...,
        col: int | None = ...,
        secondary_y: bool | None = ...,
    ) -> Generator[layout.Shape, None, None]:  # -> Generator[Any, Any, None]:
        ...
    def for_each_shape(
        self,
        fn: Callable[[layout.Shape], Any],
        selector: dict[str, Any] | Callable[[BaseLayoutHierarchyType], bool] | int | str | None = ...,
        row: int | None = ...,
        col: int | None = ...,
        secondary_y: bool | None = ...,
    ) -> Figure: ...
    def update_shapes(
        self,
        patch: dict[str, Any] = ...,
        selector: dict[str, Any] | Callable[[BaseLayoutHierarchyType], bool] | int | str | None = ...,
        row: int | None = ...,
        col: int | None = ...,
        secondary_y: bool | None = ...,
        **kwargs: Any,
    ) -> Figure: ...
    def add_shape(
        self,
        arg=...,  # pyright: ignore[reportMissingParameterType]
        editable=...,  # pyright: ignore[reportMissingParameterType]
        fillcolor: str = ...,
        fillrule=...,  # pyright: ignore[reportMissingParameterType]
        label=...,  # pyright: ignore[reportMissingParameterType]
        layer=...,  # pyright: ignore[reportMissingParameterType]
        legend: str = ...,
        legendgroup: str | int = ...,
        legendgrouptitle: layout.shape.Legendgrouptitle | dict[str, Any] = ...,
        legendrank: int | float = ...,
        legendwidth: int | float = ...,
        line: layout.shape.Line | dict[str, str | int | float] = ...,
        name: str | int = ...,
        opacity: int | float = ...,
        path=...,  # pyright: ignore[reportMissingParameterType]
        showlegend: bool = ...,
        templateitemname=...,  # pyright: ignore[reportMissingParameterType]
        type=...,  # pyright: ignore[reportMissingParameterType]
        visible: bool | str = ...,
        x0: int | float = ...,
        x0shift=...,  # pyright: ignore[reportMissingParameterType]
        x1: int | float = ...,
        x1shift=...,  # pyright: ignore[reportMissingParameterType]
        xanchor=...,  # pyright: ignore[reportMissingParameterType]
        xref=...,  # pyright: ignore[reportMissingParameterType]
        xsizemode=...,  # pyright: ignore[reportMissingParameterType]
        y0: int | float = ...,
        y0shift=...,  # pyright: ignore[reportMissingParameterType]
        y1: int | float = ...,
        y1shift=...,  # pyright: ignore[reportMissingParameterType]
        yanchor=...,  # pyright: ignore[reportMissingParameterType]
        yref=...,  # pyright: ignore[reportMissingParameterType]
        ysizemode=...,  # pyright: ignore[reportMissingParameterType]
        row=...,  # pyright: ignore[reportMissingParameterType]
        col=...,  # pyright: ignore[reportMissingParameterType]
        secondary_y: bool | None = ...,
        exclude_empty_subplots: bool = ...,
        **kwargs: Any,
    ) -> Figure: ...
