from typing import Any

import plotly.graph_objs as go

def make_subplots(
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
    figure: go.Figure | None = ...,
    **kwargs: Any,
) -> go.Figure: ...
