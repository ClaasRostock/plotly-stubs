from collections.abc import Generator
from pprint import PrettyPrinter
from typing import Any, TypeVar

from _plotly_utils.data_utils import *
from _plotly_utils.utils import *
from _plotly_utils.utils import PlotlyJSONEncoder

__all__ = [
    "ElidedPrettyPrinter",
    "ElidedWrapper",
    "PlotlyJSONEncoder",
    "decode_unicode",
    "get_by_path",
    "node_generator",
]

class ElidedWrapper:
    def __init__(
        self,
        v: Any,
        threshold: int,
        indent: int,
    ) -> None: ...
    @staticmethod
    def is_wrappable(v: Any) -> bool: ...

class ElidedPrettyPrinter(PrettyPrinter):
    def __init__(
        self,
        *args: Any,
        **kwargs: Any,
    ) -> None: ...

def node_generator(
    node: Any,
    path: str = ...,
) -> Generator[tuple[dict[Any, Any], Any] | Any, Any, None]: ...
def get_by_path(
    obj: Any,
    path: str = ...,
) -> Any: ...

_VT = TypeVar("_VT", bound=list[Any] | dict[Any, Any] | Any)

def decode_unicode(coll: _VT) -> _VT: ...
