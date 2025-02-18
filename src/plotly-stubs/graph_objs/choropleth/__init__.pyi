# NOTE: Some import statements are intentionally written as alias imports, i.e.
#       `import package.subpackage as subpackage`
#       This is necessary for subpackages for which no stubs have been created yet.
#       -> For these imports, DO NOT CHANGE the import statements to `from package import subpackage`.
#       Once stubs for these subpackages are created, the import statements can
#       be changed to their respective `from package import subpackage` form.

# Import of subpackages for which _no_ stubs have been created yet:
import plotly.graph_objs.choropleth.colorbar as colorbar
import plotly.graph_objs.choropleth.hoverlabel as hoverlabel
import plotly.graph_objs.choropleth.legendgrouptitle as legendgrouptitle
import plotly.graph_objs.choropleth.marker as marker

# Import of subpackages for which stubs have been created:
import plotly.graph_objs.choropleth.selected as selected
import plotly.graph_objs.choropleth.unselected as unselected

#
# Direct import of names this subpackage exports:
from plotly.graph_objs.choropleth._colorbar import ColorBar
from plotly.graph_objs.choropleth._hoverlabel import Hoverlabel
from plotly.graph_objs.choropleth._legendgrouptitle import Legendgrouptitle
from plotly.graph_objs.choropleth._marker import Marker
from plotly.graph_objs.choropleth._selected import Selected
from plotly.graph_objs.choropleth._stream import Stream
from plotly.graph_objs.choropleth._unselected import Unselected

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
