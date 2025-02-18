from typing import Any

import pandas as pd

# NOTE: Some import statements are intentionally written as alias imports, i.e.
#       `import package.subpackage as subpackage`
#       This is necessary for subpackages for which no stubs have been created yet.
#       -> For these imports, DO NOT CHANGE the import statements to `from package import subpackage`.
#       Once stubs for these subpackages are created, the import statements can
#       be changed to their respective `from package import subpackage` form.
# Import of subpackages for which _no_ stubs have been created yet:
import plotly.data as data
import plotly.tools as tools

# Import of subpackages for which stubs have been created:
from plotly import (
    colors,
    graph_objs,
    io,
    offline,
    utils,
)
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
) -> graph_objs.Figure: ...
def boxplot_frame(
    data_frame: pd.DataFrame,
    **kwargs: Any,
) -> graph_objs.Figure: ...
def hist_frame(
    data_frame: pd.DataFrame,
    **kwargs: Any,
) -> graph_objs.Figure: ...
def hist_series(
    data_frame: pd.DataFrame,
    **kwargs: Any,
) -> graph_objs.Figure: ...
