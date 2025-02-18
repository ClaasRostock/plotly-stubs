from typing import Any

import pandas as pd
import plotly.colors as colors
import plotly.data as data
import plotly.graph_objs as graph_objs
import plotly.io as io
import plotly.offline as offline
import plotly.tools as tools
import plotly.utils as utils
from plotly.graph_objs import Figure
from plotly.version import __version__

__all__ = [
    "__version__",
    "colors",
    "data",
    "graph_objs",
    "io",
    "offline",
    "tools",
    "utils",
]

def plot(
    data_frame: pd.DataFrame,
    kind: str,
    **kwargs: Any,
) -> Figure: ...
def boxplot_frame(
    data_frame: pd.DataFrame,
    **kwargs: Any,
) -> Figure: ...
def hist_frame(
    data_frame: pd.DataFrame,
    **kwargs: Any,
) -> Figure: ...
def hist_series(
    data_frame: pd.DataFrame,
    **kwargs: Any,
) -> Figure: ...
