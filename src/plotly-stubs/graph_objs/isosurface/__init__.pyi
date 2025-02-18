# NOTE: Some import statements are intentionally written as alias imports, i.e.
#       `import package.subpackage as subpackage`
#       This is necessary for subpackages for which no stubs have been created yet.
#       -> For these imports, DO NOT CHANGE the import statements to `from package import subpackage`.
#       Once stubs for these subpackages are created, the import statements can
#       be changed to their respective `from package import subpackage` form.

# Import of subpackages for which _no_ stubs have been created yet:
import plotly.graph_objs.isosurface.caps as caps
import plotly.graph_objs.isosurface.colorbar as colorbar
import plotly.graph_objs.isosurface.hoverlabel as hoverlabel
import plotly.graph_objs.isosurface.legendgrouptitle as legendgrouptitle
import plotly.graph_objs.isosurface.slices as slices

# Import of subpackages for which stubs have been created:
# -/-
#
# Direct import of names this subpackage exports:
from plotly.graph_objs.isosurface._caps import Caps
from plotly.graph_objs.isosurface._colorbar import ColorBar
from plotly.graph_objs.isosurface._contour import Contour
from plotly.graph_objs.isosurface._hoverlabel import Hoverlabel
from plotly.graph_objs.isosurface._legendgrouptitle import Legendgrouptitle
from plotly.graph_objs.isosurface._lighting import Lighting
from plotly.graph_objs.isosurface._lightposition import Lightposition
from plotly.graph_objs.isosurface._slices import Slices
from plotly.graph_objs.isosurface._spaceframe import Spaceframe
from plotly.graph_objs.isosurface._stream import Stream
from plotly.graph_objs.isosurface._surface import Surface

__all__ = [
    "Caps",
    "ColorBar",
    "Contour",
    "Hoverlabel",
    "Legendgrouptitle",
    "Lighting",
    "Lightposition",
    "Slices",
    "Spaceframe",
    "Stream",
    "Surface",
    "caps",
    "colorbar",
    "hoverlabel",
    "legendgrouptitle",
    "slices",
]
