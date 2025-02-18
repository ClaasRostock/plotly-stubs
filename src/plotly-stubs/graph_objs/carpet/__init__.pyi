# NOTE: Some import statements are intentionally written as alias imports, i.e.
#       `import package.subpackage as subpackage`
#       This is necessary for subpackages for which no stubs have been created yet.
#       -> For these imports, DO NOT CHANGE the import statements to `from package import subpackage`.
#       Once stubs for these subpackages are created, the import statements can
#       be changed to their respective `from package import subpackage` form.

# Import of subpackages for which _no_ stubs have been created yet:
import plotly.graph_objs.carpet.aaxis as aaxis
import plotly.graph_objs.carpet.baxis as baxis
import plotly.graph_objs.carpet.legendgrouptitle as legendgrouptitle

# Import of subpackages for which stubs have been created:
# -/-
#
# Direct import of names this subpackage exports:
from plotly.graph_objs.carpet._aaxis import Aaxis
from plotly.graph_objs.carpet._baxis import Baxis
from plotly.graph_objs.carpet._font import Font
from plotly.graph_objs.carpet._legendgrouptitle import Legendgrouptitle
from plotly.graph_objs.carpet._stream import Stream

__all__ = [
    "Aaxis",
    "Baxis",
    "Font",
    "Legendgrouptitle",
    "Stream",
    "aaxis",
    "baxis",
    "legendgrouptitle",
]
