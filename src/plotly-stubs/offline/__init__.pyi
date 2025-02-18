# NOTE: Some import statements are intentionally written as alias imports, i.e.
#       `import package.subpackage as subpackage`
#       This is necessary for subpackages for which no stubs have been created yet.
#       -> For these imports, DO NOT CHANGE the import statements to `from package import subpackage`.
#       Once stubs for these subpackages are created, the import statements can
#       be changed to their respective `from package import subpackage` form.

# Import of subpackages for which _no_ stubs have been created yet:
import plotly.offline.offline as offline

# Import of subpackages for which stubs have been created:
# -/-
#
# Direct import of names this subpackage exports:
from plotly.offline.offline import (
    download_plotlyjs,
    enable_mpl_offline,
    get_plotlyjs,
    get_plotlyjs_version,
    init_notebook_mode,
    iplot,
    iplot_mpl,
    plot,
    plot_mpl,
)

__all__ = [
    "download_plotlyjs",
    "enable_mpl_offline",
    "get_plotlyjs",
    "get_plotlyjs_version",
    "init_notebook_mode",
    "iplot",
    "iplot_mpl",
    "offline",
    "plot",
    "plot_mpl",
]
