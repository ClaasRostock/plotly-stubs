# NOTE: Some import statements are intentionally written as alias imports, i.e.
#       `import package.subpackage as subpackage`
#       This is necessary for subpackages for which no stubs have been created yet.
#       -> For these imports, DO NOT CHANGE the import statements to `from package import subpackage`.
#       Once stubs for these subpackages are created, the import statements can
#       be changed to their respective `from package import subpackage` form.

# Import of subpackages for which _no_ stubs have been created yet:
import plotly.graph_objs.violin.box as box
import plotly.graph_objs.violin.hoverlabel as hoverlabel
import plotly.graph_objs.violin.legendgrouptitle as legendgrouptitle
import plotly.graph_objs.violin.marker as marker
import plotly.graph_objs.violin.selected as selected
import plotly.graph_objs.violin.unselected as unselected

# Import of subpackages for which stubs have been created:
# -/-
#
# Direct import of names this subpackage exports:
from plotly.graph_objs.violin._box import Box
from plotly.graph_objs.violin._hoverlabel import Hoverlabel
from plotly.graph_objs.violin._legendgrouptitle import Legendgrouptitle
from plotly.graph_objs.violin._line import Line
from plotly.graph_objs.violin._marker import Marker
from plotly.graph_objs.violin._meanline import Meanline
from plotly.graph_objs.violin._selected import Selected
from plotly.graph_objs.violin._stream import Stream
from plotly.graph_objs.violin._unselected import Unselected

__all__ = [
    "Box",
    "Hoverlabel",
    "Legendgrouptitle",
    "Line",
    "Marker",
    "Meanline",
    "Selected",
    "Stream",
    "Unselected",
    "box",
    "hoverlabel",
    "legendgrouptitle",
    "marker",
    "selected",
    "unselected",
]
