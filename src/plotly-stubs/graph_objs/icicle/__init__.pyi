# NOTE: Some import statements are intentionally written as alias imports, i.e.
#       `import package.subpackage as subpackage`
#       This is necessary for subpackages for which no stubs have been created yet.
#       -> For these imports, DO NOT CHANGE the import statements to `from package import subpackage`.
#       Once stubs for these subpackages are created, the import statements can
#       be changed to their respective `from package import subpackage` form.

# Import of subpackages for which _no_ stubs have been created yet:
import plotly.graph_objs.icicle.hoverlabel as hoverlabel
import plotly.graph_objs.icicle.legendgrouptitle as legendgrouptitle
import plotly.graph_objs.icicle.marker as marker
import plotly.graph_objs.icicle.pathbar as pathbar

# Import of subpackages for which stubs have been created:
# -/-
#
# Direct import of names this subpackage exports:
from plotly.graph_objs.icicle._domain import Domain
from plotly.graph_objs.icicle._hoverlabel import Hoverlabel
from plotly.graph_objs.icicle._insidetextfont import Insidetextfont
from plotly.graph_objs.icicle._leaf import Leaf
from plotly.graph_objs.icicle._legendgrouptitle import Legendgrouptitle
from plotly.graph_objs.icicle._marker import Marker
from plotly.graph_objs.icicle._outsidetextfont import Outsidetextfont
from plotly.graph_objs.icicle._pathbar import Pathbar
from plotly.graph_objs.icicle._root import Root
from plotly.graph_objs.icicle._stream import Stream
from plotly.graph_objs.icicle._textfont import Textfont
from plotly.graph_objs.icicle._tiling import Tiling

__all__ = [
    "Domain",
    "Hoverlabel",
    "Insidetextfont",
    "Leaf",
    "Legendgrouptitle",
    "Marker",
    "Outsidetextfont",
    "Pathbar",
    "Root",
    "Stream",
    "Textfont",
    "Tiling",
    "hoverlabel",
    "legendgrouptitle",
    "marker",
    "pathbar",
]
