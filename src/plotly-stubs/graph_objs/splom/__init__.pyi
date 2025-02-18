# NOTE: Some import statements are intentionally written as alias imports, i.e.
#       `import package.subpackage as subpackage`
#       This is necessary for subpackages for which no stubs have been created yet.
#       -> For these imports, DO NOT CHANGE the import statements to `from package import subpackage`.
#       Once stubs for these subpackages are created, the import statements can
#       be changed to their respective `from package import subpackage` form.

# Import of subpackages for which _no_ stubs have been created yet:
import plotly.graph_objs.splom.dimension as dimension
import plotly.graph_objs.splom.hoverlabel as hoverlabel
import plotly.graph_objs.splom.legendgrouptitle as legendgrouptitle
import plotly.graph_objs.splom.marker as marker
import plotly.graph_objs.splom.selected as selected
import plotly.graph_objs.splom.unselected as unselected

# Import of subpackages for which stubs have been created:
# -/-
#
# Direct import of names this subpackage exports:
from plotly.graph_objs.splom._diagonal import Diagonal
from plotly.graph_objs.splom._dimension import Dimension
from plotly.graph_objs.splom._hoverlabel import Hoverlabel
from plotly.graph_objs.splom._legendgrouptitle import Legendgrouptitle
from plotly.graph_objs.splom._marker import Marker
from plotly.graph_objs.splom._selected import Selected
from plotly.graph_objs.splom._stream import Stream
from plotly.graph_objs.splom._unselected import Unselected

__all__ = [
    "Diagonal",
    "Dimension",
    "Hoverlabel",
    "Legendgrouptitle",
    "Marker",
    "Selected",
    "Stream",
    "Unselected",
    "dimension",
    "hoverlabel",
    "legendgrouptitle",
    "marker",
    "selected",
    "unselected",
]
