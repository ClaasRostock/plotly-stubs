# NOTE: Some import statements are intentionally written as alias imports, i.e.
#       `import package.subpackage as subpackage`
#       This is necessary for subpackages for which no stubs have been created yet.
#       -> For these imports, DO NOT CHANGE the import statements to `from package import subpackage`.
#       Once stubs for these subpackages are created, the import statements can
#       be changed to their respective `from package import subpackage` form.

# Import of subpackages for which _no_ stubs have been created yet:
# -/-

# Import of subpackages for which stubs have been created:
from plotly.graph_objs.scatter.marker import colorbar

# Direct import of names this subpackage exports:
from plotly.graph_objs.scatter.marker._colorbar import ColorBar
from plotly.graph_objs.scatter.marker._gradient import Gradient
from plotly.graph_objs.scatter.marker._line import Line

__all__ = [
    "ColorBar",
    "Gradient",
    "Line",
    "colorbar",
]
