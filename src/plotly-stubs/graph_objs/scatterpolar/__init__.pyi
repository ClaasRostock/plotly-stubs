# NOTE: Some import statements are intentionally written as alias imports, i.e.
#       `import package.subpackage as subpackage`
#       This is necessary for subpackages for which no stubs have been created yet.
#       -> For these imports, DO NOT CHANGE the import statements to `from package import subpackage`.
#       Once stubs for these subpackages are created, the import statements can
#       be changed to their respective `from package import subpackage` form.

# Import of subpackages for which _no_ stubs have been created yet:
import plotly.graph_objs.scatterpolar.hoverlabel as hoverlabel
import plotly.graph_objs.scatterpolar.legendgrouptitle as legendgrouptitle
import plotly.graph_objs.scatterpolar.marker as marker
import plotly.graph_objs.scatterpolar.selected as selected
import plotly.graph_objs.scatterpolar.unselected as unselected

# Import of subpackages for which stubs have been created:
# -/-
#
# Direct import of names this subpackage exports:
from plotly.graph_objs.scatterpolar._hoverlabel import Hoverlabel
from plotly.graph_objs.scatterpolar._legendgrouptitle import Legendgrouptitle
from plotly.graph_objs.scatterpolar._line import Line
from plotly.graph_objs.scatterpolar._marker import Marker
from plotly.graph_objs.scatterpolar._selected import Selected
from plotly.graph_objs.scatterpolar._stream import Stream
from plotly.graph_objs.scatterpolar._textfont import Textfont
from plotly.graph_objs.scatterpolar._unselected import Unselected

__all__ = [
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
