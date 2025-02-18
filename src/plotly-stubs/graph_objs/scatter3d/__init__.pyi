# NOTE: Some import statements are intentionally written as alias imports, i.e.
#       `import package.subpackage as subpackage`
#       This is necessary for subpackages for which no stubs have been created yet.
#       -> For these imports, DO NOT CHANGE the import statements to `from package import subpackage`.
#       Once stubs for these subpackages are created, the import statements can
#       be changed to their respective `from package import subpackage` form.

# Import of subpackages for which _no_ stubs have been created yet:
import plotly.graph_objs.scatter3d.hoverlabel as hoverlabel
import plotly.graph_objs.scatter3d.legendgrouptitle as legendgrouptitle
import plotly.graph_objs.scatter3d.line as line
import plotly.graph_objs.scatter3d.marker as marker
import plotly.graph_objs.scatter3d.projection as projection

# Import of subpackages for which stubs have been created:
# -/-
#
# Direct import of names this subpackage exports:
from plotly.graph_objs.scatter3d._error_x import ErrorX
from plotly.graph_objs.scatter3d._error_y import ErrorY
from plotly.graph_objs.scatter3d._error_z import ErrorZ
from plotly.graph_objs.scatter3d._hoverlabel import Hoverlabel
from plotly.graph_objs.scatter3d._legendgrouptitle import Legendgrouptitle
from plotly.graph_objs.scatter3d._line import Line
from plotly.graph_objs.scatter3d._marker import Marker
from plotly.graph_objs.scatter3d._projection import Projection
from plotly.graph_objs.scatter3d._stream import Stream
from plotly.graph_objs.scatter3d._textfont import Textfont

__all__ = [
    "ErrorX",
    "ErrorY",
    "ErrorZ",
    "Hoverlabel",
    "Legendgrouptitle",
    "Line",
    "Marker",
    "Projection",
    "Stream",
    "Textfont",
    "hoverlabel",
    "legendgrouptitle",
    "line",
    "marker",
    "projection",
]
