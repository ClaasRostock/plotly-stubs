# NOTE: Some import statements are intentionally written as alias imports, i.e.
#       `import package.subpackage as subpackage`
#       This is necessary for subpackages for which no stubs have been created yet.
#       -> For these imports, DO NOT CHANGE the import statements to `from package import subpackage`.
#       Once stubs for these subpackages are created, the import statements can
#       be changed to their respective `from package import subpackage` form.

# Import of subpackages for which _no_ stubs have been created yet:
import plotly.graph_objs.indicator.delta as delta
import plotly.graph_objs.indicator.gauge as gauge
import plotly.graph_objs.indicator.legendgrouptitle as legendgrouptitle
import plotly.graph_objs.indicator.number as number
import plotly.graph_objs.indicator.title as title

# Import of subpackages for which stubs have been created:
# -/-
#
# Direct import of names this subpackage exports:
from plotly.graph_objs.indicator._delta import Delta
from plotly.graph_objs.indicator._domain import Domain
from plotly.graph_objs.indicator._gauge import Gauge
from plotly.graph_objs.indicator._legendgrouptitle import Legendgrouptitle
from plotly.graph_objs.indicator._number import Number
from plotly.graph_objs.indicator._stream import Stream
from plotly.graph_objs.indicator._title import Title

__all__ = [
    "Delta",
    "Domain",
    "Gauge",
    "Legendgrouptitle",
    "Number",
    "Stream",
    "Title",
    "delta",
    "gauge",
    "legendgrouptitle",
    "number",
    "title",
]
