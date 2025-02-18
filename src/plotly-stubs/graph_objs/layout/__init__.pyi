# NOTE: Some import statements are intentionally written as alias imports, i.e.
#       `import package.subpackage as subpackage`
#       This is necessary for subpackages for which no stubs have been created yet.
#       -> For these imports, DO NOT CHANGE the import statements to `from package import subpackage`.
#       Once stubs for these subpackages are created, the import statements can
#       be changed to their respective `from package import subpackage` form.

# Import of subpackages for which _no_ stubs have been created yet:
import plotly.graph_objs.layout.annotation as annotation
import plotly.graph_objs.layout.coloraxis as coloraxis
import plotly.graph_objs.layout.geo as geo
import plotly.graph_objs.layout.grid as grid
import plotly.graph_objs.layout.hoverlabel as hoverlabel
import plotly.graph_objs.layout.legend as legend
import plotly.graph_objs.layout.map as map  # noqa: A004
import plotly.graph_objs.layout.mapbox as mapbox
import plotly.graph_objs.layout.newshape as newshape
import plotly.graph_objs.layout.polar as polar
import plotly.graph_objs.layout.scene as scene
import plotly.graph_objs.layout.selection as selection
import plotly.graph_objs.layout.shape as shape
import plotly.graph_objs.layout.slider as slider
import plotly.graph_objs.layout.smith as smith
import plotly.graph_objs.layout.template as template
import plotly.graph_objs.layout.ternary as ternary
import plotly.graph_objs.layout.title as title
import plotly.graph_objs.layout.updatemenu as updatemenu
import plotly.graph_objs.layout.xaxis as xaxis
import plotly.graph_objs.layout.yaxis as yaxis

# Import of subpackages for which stubs have been created:
from plotly.graph_objs.layout import newselection

#
# Direct import of names this subpackage exports:
from plotly.graph_objs.layout._activeselection import Activeselection
from plotly.graph_objs.layout._activeshape import Activeshape
from plotly.graph_objs.layout._annotation import Annotation
from plotly.graph_objs.layout._coloraxis import Coloraxis
from plotly.graph_objs.layout._colorscale import Colorscale
from plotly.graph_objs.layout._font import Font
from plotly.graph_objs.layout._geo import Geo
from plotly.graph_objs.layout._grid import Grid
from plotly.graph_objs.layout._hoverlabel import Hoverlabel
from plotly.graph_objs.layout._image import Image
from plotly.graph_objs.layout._legend import Legend
from plotly.graph_objs.layout._map import Map
from plotly.graph_objs.layout._mapbox import Mapbox
from plotly.graph_objs.layout._margin import Margin
from plotly.graph_objs.layout._modebar import Modebar
from plotly.graph_objs.layout._newselection import Newselection
from plotly.graph_objs.layout._newshape import Newshape
from plotly.graph_objs.layout._polar import Polar
from plotly.graph_objs.layout._scene import Scene
from plotly.graph_objs.layout._selection import Selection
from plotly.graph_objs.layout._shape import Shape
from plotly.graph_objs.layout._slider import Slider
from plotly.graph_objs.layout._smith import Smith
from plotly.graph_objs.layout._template import Template
from plotly.graph_objs.layout._ternary import Ternary
from plotly.graph_objs.layout._title import Title
from plotly.graph_objs.layout._transition import Transition
from plotly.graph_objs.layout._uniformtext import Uniformtext
from plotly.graph_objs.layout._updatemenu import Updatemenu
from plotly.graph_objs.layout._xaxis import XAxis
from plotly.graph_objs.layout._yaxis import YAxis

__all__ = [
    "Activeselection",
    "Activeshape",
    "Annotation",
    "Coloraxis",
    "Colorscale",
    "Font",
    "Geo",
    "Grid",
    "Hoverlabel",
    "Image",
    "Legend",
    "Map",
    "Mapbox",
    "Margin",
    "Modebar",
    "Newselection",
    "Newshape",
    "Polar",
    "Scene",
    "Selection",
    "Shape",
    "Slider",
    "Smith",
    "Template",
    "Ternary",
    "Title",
    "Transition",
    "Uniformtext",
    "Updatemenu",
    "XAxis",
    "YAxis",
    "annotation",
    "coloraxis",
    "geo",
    "grid",
    "hoverlabel",
    "legend",
    "map",
    "mapbox",
    "newselection",
    "newshape",
    "polar",
    "scene",
    "selection",
    "shape",
    "slider",
    "smith",
    "template",
    "ternary",
    "title",
    "updatemenu",
    "xaxis",
    "yaxis",
]
