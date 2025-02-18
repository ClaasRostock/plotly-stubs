# NOTE: Some import statements are intentionally written as alias imports, i.e.
#       `import package.subpackage as subpackage`
#       This is necessary for subpackages for which no stubs have been created yet.
#       -> For these imports, DO NOT CHANGE the import statements to `from package import subpackage`.
#       Once stubs for these subpackages are created, the import statements can
#       be changed to their respective `from package import subpackage` form.

# Import of subpackages for which _no_ stubs have been created yet:
import plotly.io.base_renderers as base_renderers
import plotly.io.json as json
import plotly.io.kaleido as kaleido
import plotly.io.orca as orca

# Import of subpackages for which stubs have been created:
# -/-
#
# Direct import of names this subpackage exports:
from plotly.io._html import to_html, write_html
from plotly.io._json import from_json, read_json, to_json, write_json
from plotly.io._kaleido import full_figure_for_development, to_image, write_image
from plotly.io._renderers import renderers, show
from plotly.io._templates import templates, to_templated

__all__ = [
    "base_renderers",
    "from_json",
    "full_figure_for_development",
    "json",
    "kaleido",
    "orca",
    "read_json",
    "renderers",
    "show",
    "templates",
    "to_html",
    "to_image",
    "to_json",
    "to_templated",
    "write_html",
    "write_image",
    "write_json",
]
