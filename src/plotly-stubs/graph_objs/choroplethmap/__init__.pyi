# NOTE: Some import statements are intentionally written as alias imports, i.e.
#       `import package.subpackage as subpackage`
#       This is necessary for subpackages for which no stubs have been created yet.
#       -> For these imports, DO NOT CHANGE the import statements to `from package import subpackage`.
#       Once stubs for these subpackages are created, the import statements can
#       be changed to their respective `from package import subpackage` form.

# Import of subpackages for which _no_ stubs have been created yet:
import plotly.graph_objs.choroplethmap.colorbar as colorbar
import plotly.graph_objs.choroplethmap.hoverlabel as hoverlabel
import plotly.graph_objs.choroplethmap.legendgrouptitle as legendgrouptitle
import plotly.graph_objs.choroplethmap.marker as marker
import plotly.graph_objs.choroplethmap.selected as selected
import plotly.graph_objs.choroplethmap.unselected as unselected

# Import of subpackages for which stubs have been created:
# -/-
#
# Direct import of names this subpackage exports:
from plotly.graph_objs.choroplethmap._colorbar import ColorBar
from plotly.graph_objs.choroplethmap._hoverlabel import Hoverlabel
from plotly.graph_objs.choroplethmap._legendgrouptitle import Legendgrouptitle
from plotly.graph_objs.choroplethmap._marker import Marker
from plotly.graph_objs.choroplethmap._selected import Selected
from plotly.graph_objs.choroplethmap._stream import Stream
from plotly.graph_objs.choroplethmap._unselected import Unselected

__all__ = [
    "ColorBar",
    "Hoverlabel",
    "Legendgrouptitle",
    "Marker",
    "Selected",
    "Stream",
    "Unselected",
    "colorbar",
    "hoverlabel",
    "legendgrouptitle",
    "marker",
    "selected",
    "unselected",
]
