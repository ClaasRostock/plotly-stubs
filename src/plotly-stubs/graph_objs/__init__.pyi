import plotly.graph_objs.bar as bar
import plotly.graph_objs.barpolar as barpolar
import plotly.graph_objs.box as box
import plotly.graph_objs.candlestick as candlestick
import plotly.graph_objs.carpet as carpet
import plotly.graph_objs.choropleth as choropleth
import plotly.graph_objs.choroplethmap as choroplethmap
import plotly.graph_objs.choroplethmapbox as choroplethmapbox
import plotly.graph_objs.cone as cone
import plotly.graph_objs.contour as contour
import plotly.graph_objs.contourcarpet as contourcarpet
import plotly.graph_objs.densitymap as densitymap
import plotly.graph_objs.densitymapbox as densitymapbox
import plotly.graph_objs.funnel as funnel
import plotly.graph_objs.funnelarea as funnelarea
import plotly.graph_objs.heatmap as heatmap
import plotly.graph_objs.histogram as histogram
import plotly.graph_objs.histogram2d as histogram2d
import plotly.graph_objs.histogram2dcontour as histogram2dcontour
import plotly.graph_objs.icicle as icicle
import plotly.graph_objs.image as image
import plotly.graph_objs.indicator as indicator
import plotly.graph_objs.isosurface as isosurface
import plotly.graph_objs.layout as layout
import plotly.graph_objs.mesh3d as mesh3d
import plotly.graph_objs.ohlc as ohlc
import plotly.graph_objs.parcats as parcats
import plotly.graph_objs.parcoords as parcoords
import plotly.graph_objs.pie as pie
import plotly.graph_objs.sankey as sankey
import plotly.graph_objs.scatter as scatter
import plotly.graph_objs.scatter3d as scatter3d
import plotly.graph_objs.scattercarpet as scattercarpet
import plotly.graph_objs.scattergeo as scattergeo
import plotly.graph_objs.scattergl as scattergl
import plotly.graph_objs.scattermap as scattermap
import plotly.graph_objs.scattermapbox as scattermapbox
import plotly.graph_objs.scatterpolar as scatterpolar
import plotly.graph_objs.scatterpolargl as scatterpolargl
import plotly.graph_objs.scattersmith as scattersmith
import plotly.graph_objs.scatterternary as scatterternary
import plotly.graph_objs.splom as splom
import plotly.graph_objs.streamtube as streamtube
import plotly.graph_objs.sunburst as sunburst
import plotly.graph_objs.surface as surface
import plotly.graph_objs.table as table
import plotly.graph_objs.treemap as treemap
import plotly.graph_objs.violin as violin
import plotly.graph_objs.volume as volume
import plotly.graph_objs.waterfall as waterfall
from plotly.graph_objs._bar import Bar
from plotly.graph_objs._barpolar import Barpolar
from plotly.graph_objs._box import Box
from plotly.graph_objs._candlestick import Candlestick
from plotly.graph_objs._carpet import Carpet
from plotly.graph_objs._choropleth import Choropleth
from plotly.graph_objs._choroplethmap import Choroplethmap
from plotly.graph_objs._choroplethmapbox import Choroplethmapbox
from plotly.graph_objs._cone import Cone
from plotly.graph_objs._contour import Contour
from plotly.graph_objs._contourcarpet import Contourcarpet
from plotly.graph_objs._densitymap import Densitymap
from plotly.graph_objs._densitymapbox import Densitymapbox
from plotly.graph_objs._figure import Figure

# from plotly.graph_objs._deprecations import (
#     AngularAxis,
#     Annotation,
#     Annotations,
#     ColorBar,
#     Contours,
#     Data,
#     ErrorX,
#     ErrorY,
#     ErrorZ,
#     Font,
#     Frames,
#     Histogram2dcontour,
#     Legend,
#     Line,
#     Margin,
#     Marker,
#     RadialAxis,
#     Scene,
#     Stream,
#     Trace,
#     XAxis,
#     XBins,
#     YAxis,
#     YBins,
#     ZAxis,
# )
from plotly.graph_objs._frame import Frame
from plotly.graph_objs._funnel import Funnel
from plotly.graph_objs._funnelarea import Funnelarea
from plotly.graph_objs._heatmap import Heatmap
from plotly.graph_objs._histogram import Histogram
from plotly.graph_objs._histogram2d import Histogram2d
from plotly.graph_objs._histogram2dcontour import Histogram2dContour
from plotly.graph_objs._icicle import Icicle
from plotly.graph_objs._image import Image
from plotly.graph_objs._indicator import Indicator
from plotly.graph_objs._isosurface import Isosurface
from plotly.graph_objs._layout import Layout
from plotly.graph_objs._mesh3d import Mesh3d
from plotly.graph_objs._ohlc import Ohlc
from plotly.graph_objs._parcats import Parcats
from plotly.graph_objs._parcoords import Parcoords
from plotly.graph_objs._pie import Pie
from plotly.graph_objs._sankey import Sankey
from plotly.graph_objs._scatter import Scatter
from plotly.graph_objs._scatter3d import Scatter3d
from plotly.graph_objs._scattercarpet import Scattercarpet
from plotly.graph_objs._scattergeo import Scattergeo
from plotly.graph_objs._scattergl import Scattergl
from plotly.graph_objs._scattermap import Scattermap
from plotly.graph_objs._scattermapbox import Scattermapbox
from plotly.graph_objs._scatterpolar import Scatterpolar
from plotly.graph_objs._scatterpolargl import Scatterpolargl
from plotly.graph_objs._scattersmith import Scattersmith
from plotly.graph_objs._scatterternary import Scatterternary
from plotly.graph_objs._splom import Splom
from plotly.graph_objs._streamtube import Streamtube
from plotly.graph_objs._sunburst import Sunburst
from plotly.graph_objs._surface import Surface
from plotly.graph_objs._table import Table
from plotly.graph_objs._treemap import Treemap
from plotly.graph_objs._violin import Violin
from plotly.graph_objs._volume import Volume
from plotly.graph_objs._waterfall import Waterfall

__all__ = [
    # "AngularAxis",
    # "Annotation",
    # "Annotations",
    "Bar",
    "Barpolar",
    "Box",
    "Candlestick",
    "Carpet",
    "Choropleth",
    "Choroplethmap",
    "Choroplethmapbox",
    # "ColorBar",
    "Cone",
    "Contour",
    "Contourcarpet",
    # "Contours",
    # "Data",
    "Densitymap",
    "Densitymapbox",
    # "ErrorX",
    # "ErrorY",
    # "ErrorZ",
    "Figure",
    # "Font",
    "Frame",
    # "Frames",
    "Funnel",
    "Funnelarea",
    "Heatmap",
    "Histogram",
    "Histogram2d",
    "Histogram2dContour",
    # "Histogram2dcontour",
    "Icicle",
    "Image",
    "Indicator",
    "Isosurface",
    "Layout",
    # "Legend",
    # "Line",
    # "Margin",
    # "Marker",
    "Mesh3d",
    "Ohlc",
    "Parcats",
    "Parcoords",
    "Pie",
    # "RadialAxis",
    "Sankey",
    "Scatter",
    "Scatter3d",
    "Scattercarpet",
    "Scattergeo",
    "Scattergl",
    "Scattermap",
    "Scattermapbox",
    "Scatterpolar",
    "Scatterpolargl",
    "Scattersmith",
    "Scatterternary",
    # "Scene",
    "Splom",
    # "Stream",
    "Streamtube",
    "Sunburst",
    "Surface",
    "Table",
    # "Trace",
    "Treemap",
    "Violin",
    "Volume",
    "Waterfall",
    # "XAxis",
    # "XBins",
    # "YAxis",
    # "YBins",
    # "ZAxis",
    "bar",
    "barpolar",
    "box",
    "candlestick",
    "carpet",
    "choropleth",
    "choroplethmap",
    "choroplethmapbox",
    "cone",
    "contour",
    "contourcarpet",
    "densitymap",
    "densitymapbox",
    "funnel",
    "funnelarea",
    "heatmap",
    "histogram",
    "histogram2d",
    "histogram2dcontour",
    "icicle",
    "image",
    "indicator",
    "isosurface",
    "layout",
    "mesh3d",
    "ohlc",
    "parcats",
    "parcoords",
    "pie",
    "sankey",
    "scatter",
    "scatter3d",
    "scattercarpet",
    "scattergeo",
    "scattergl",
    "scattermap",
    "scattermapbox",
    "scatterpolar",
    "scatterpolargl",
    "scattersmith",
    "scatterternary",
    "splom",
    "streamtube",
    "sunburst",
    "surface",
    "table",
    "treemap",
    "violin",
    "volume",
    "waterfall",
]
