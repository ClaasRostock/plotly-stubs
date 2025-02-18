# NOTE: Some import statements are intentionally written as alias imports, i.e.
#       `import package.subpackage as subpackage`
#       This is necessary for subpackages for which no stubs have been created yet.
#       -> For these imports, DO NOT CHANGE the import statements to `from package import subpackage`.
#       Once stubs for these subpackages are created, the import statements can
#       be changed to their respective `from package import subpackage` form.

# Import of subpackages for which _no_ stubs have been created yet:
import plotly.graph_objs.funnel.connector as connector
import plotly.graph_objs.funnel.hoverlabel as hoverlabel
import plotly.graph_objs.funnel.legendgrouptitle as legendgrouptitle
import plotly.graph_objs.funnel.marker as marker

# Import of subpackages for which stubs have been created:
# -/-
#
# Direct import of names this subpackage exports:
from plotly.graph_objs.funnel._connector import Connector
from plotly.graph_objs.funnel._hoverlabel import Hoverlabel
from plotly.graph_objs.funnel._insidetextfont import Insidetextfont
from plotly.graph_objs.funnel._legendgrouptitle import Legendgrouptitle
from plotly.graph_objs.funnel._marker import Marker
from plotly.graph_objs.funnel._outsidetextfont import Outsidetextfont
from plotly.graph_objs.funnel._stream import Stream
from plotly.graph_objs.funnel._textfont import Textfont

__all__ = [
    "Connector",
    "Hoverlabel",
    "Insidetextfont",
    "Legendgrouptitle",
    "Marker",
    "Outsidetextfont",
    "Stream",
    "Textfont",
    "connector",
    "hoverlabel",
    "legendgrouptitle",
    "marker",
]
