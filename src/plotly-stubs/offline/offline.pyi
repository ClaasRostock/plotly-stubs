from typing import Any

from plotly.graph_objs import Figure

__IMAGE_FORMATS = ...

def download_plotlyjs(download_url: str) -> None: ...
def get_plotlyjs_version() -> str: ...  # -> Literal['3.0.0']:
def get_plotlyjs() -> str: ...

_window_plotly_config = ...
_mathjax_config = ...

def get_image_download_script(caller: str) -> str: ...
def build_save_image_post_script(
    image: str | None,
    image_filename: str,
    image_height: int | float,
    image_width: int | float,
    caller: str,
) -> str | None: ...
def init_notebook_mode(connected: bool = ...) -> None: ...
def iplot(
    figure_or_data: Figure | dict[str, Any] | list[dict[str, Any]],
    show_link: bool = ...,
    link_text: str = ...,
    validate: bool = ...,
    image: str | None = ...,
    filename: str | None = ...,
    image_width: int | float = ...,
    image_height: int | float = ...,
    config: dict[str, Any] | None = ...,
    auto_play: bool = ...,
    animation_opts: dict[str, Any] | None = ...,
) -> None: ...
def plot(
    figure_or_data: Figure | dict[str, Any] | list[dict[str, Any]],
    show_link: bool = ...,
    link_text: str = ...,
    validate: bool = ...,
    output_type: str = ...,
    include_plotlyjs: bool | str = ...,
    filename: str = ...,
    auto_open: bool = ...,
    image: str | None = ...,
    image_filename: str = ...,
    image_width: int | float = ...,
    image_height: int | float = ...,
    config: dict[str, Any] | None = ...,
    include_mathjax: bool | str = ...,
    auto_play: bool = ...,
    animation_opts: dict[str, Any] | None = ...,
) -> str: ...
def plot_mpl(
    mpl_fig: Any,
    resize: bool = ...,
    strip_style: bool = ...,
    verbose: bool = ...,
    show_link: bool = ...,
    link_text: str = ...,
    validate: bool = ...,
    output_type: str = ...,
    include_plotlyjs: bool | str = ...,
    filename: str = ...,
    auto_open: bool = ...,
    image: str | None = ...,
    image_filename: str = ...,
    image_height: int | float = ...,
    image_width: int | float = ...,
) -> str: ...
def iplot_mpl(
    mpl_fig: Any,
    resize: bool = ...,
    strip_style: bool = ...,
    verbose: bool = ...,
    show_link: bool = ...,
    link_text: str = ...,
    validate: bool = ...,
    image: str | None = ...,
    image_filename: str = ...,
    image_height: int | float = ...,
    image_width: int | float = ...,
) -> None: ...
def enable_mpl_offline(
    resize: bool = ...,
    strip_style: bool = ...,
    verbose: bool = ...,
    show_link: bool = ...,
    link_text: str = ...,
    validate: bool = ...,
) -> None: ...
