# NOTE: Some import statements are intentionally written as alias imports, i.e.
#       `import package.subpackage as subpackage`
#       This is necessary for subpackages for which no stubs have been created yet.
#       -> For these imports, DO NOT CHANGE the import statements to `from package import subpackage`.
#       Once stubs for these subpackages are created, the import statements can
#       be changed to their respective `from package import subpackage` form.

# Import of subpackages for which _no_ stubs have been created yet:
import plotly.graph_objs.scattergl.hoverlabel as hoverlabel
import plotly.graph_objs.scattergl.legendgrouptitle as legendgrouptitle
import plotly.graph_objs.scattergl.marker as marker
import plotly.graph_objs.scattergl.selected as selected
import plotly.graph_objs.scattergl.unselected as unselected

# Import of subpackages for which stubs have been created:
# -/-
#
# Direct import of names this subpackage exports:
from plotly.graph_objs.scattergl._error_x import ErrorX
from plotly.graph_objs.scattergl._error_y import ErrorY
from plotly.graph_objs.scattergl._hoverlabel import Hoverlabel
from plotly.graph_objs.scattergl._legendgrouptitle import Legendgrouptitle
from plotly.graph_objs.scattergl._line import Line
from plotly.graph_objs.scattergl._marker import Marker
from plotly.graph_objs.scattergl._selected import Selected
from plotly.graph_objs.scattergl._stream import Stream
from plotly.graph_objs.scattergl._textfont import Textfont
from plotly.graph_objs.scattergl._unselected import Unselected

__all__ = [
    "ErrorX",
    "ErrorY",
    "Hoverlabel",
    "Legendgrouptitle",
    "Line",
    "Marker",
    "Selected",
    "Stream",
    "Textfont",
    "Unselected",
    "hoverlabel",
    "legendgrouptitle",
    "marker",
    "selected",
    "unselected",
]
