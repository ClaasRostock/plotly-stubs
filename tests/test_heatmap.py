# Regression tests for the array properties `x`, `y` and `z` of `Heatmap` (issue #21).
#
# Every construction below is asserted twice: pytest asserts that plotly accepts the value at
# runtime, and the mypy and pyright jobs of the code quality workflow assert that the stub accepts
# it statically (both check `tests` in addition to `src`). Narrowing one of these annotations
# therefore fails CI, which is what the 0.1.4 regression slipped through. The static half only
# holds because those two jobs install the project non-editably: a stub-only package contains no
# `.py` file for hatchling's dev mode to expose, so under `uv sync` alone the type checkers see no
# `plotly` at all and every assertion here silently degrades to `Any`.
#
# plotly states the contract in the error it raises for an invalid value: "The 'x' property is an
# array that may be specified as a tuple, list, numpy array, or pandas Series".

from typing import TYPE_CHECKING

import numpy as np
import plotly.graph_objects as go
import pytest

if TYPE_CHECKING:
    import pandas as pd

Z: list[list[float]] = [[1.0, 2.0], [3.0, 4.0]]


def test_x_and_y_accept_int_sequences() -> None:
    trace = go.Heatmap(x=[0, 1], y=[0, 1], z=Z)
    assert list(trace.x) == [0, 1]
    assert list(trace.y) == [0, 1]


def test_x_and_y_accept_float_sequences() -> None:
    trace = go.Heatmap(x=[0.0, 1.0], y=[0.0, 1.0], z=Z)
    assert list(trace.x) == [0.0, 1.0]
    assert list(trace.y) == [0.0, 1.0]


def test_x_and_y_accept_str_sequences() -> None:
    trace = go.Heatmap(x=["a", "b"], y=["c", "d"], z=Z)
    assert list(trace.x) == ["a", "b"]
    assert list(trace.y) == ["c", "d"]


def test_x_and_y_accept_tuples() -> None:
    trace = go.Heatmap(x=(0, 1), y=("c", "d"), z=Z)
    assert list(trace.x) == [0, 1]
    assert list(trace.y) == ["c", "d"]


def test_x_and_y_accept_numpy_arrays() -> None:
    x = np.arange(2)
    y = np.arange(2, dtype=np.float64)
    trace = go.Heatmap(x=x, y=y, z=Z)
    assert isinstance(trace.x, np.ndarray)
    assert isinstance(trace.y, np.ndarray)
    assert trace.x.tolist() == [0, 1]
    assert trace.y.tolist() == [0.0, 1.0]


def test_x_accepts_datetime64_arrays() -> None:
    x = np.array(["2026-01-01", "2026-01-02"], dtype="datetime64[D]")
    trace = go.Heatmap(x=x, z=Z)
    assert isinstance(trace.x, np.ndarray)
    assert trace.x.dtype == x.dtype


def x_accepts_pandas_series(series: "pd.Series[float]") -> None:
    # Not a test: pandas-stubs is a development dependency but pandas itself is not, so the
    # `pd.Series` member of the annotation can only be exercised statically. mypy and pyright
    # check this body; pytest never collects or runs it.
    go.Heatmap(x=series, y=series, z=Z)


def test_z_accepts_nested_sequences() -> None:
    trace = go.Heatmap(z=[[1.0, 2.0], [3.0, 4.0]])
    assert list(trace.z) == [[1.0, 2.0], [3.0, 4.0]]


def test_z_accepts_flat_sequences_and_arrays() -> None:
    assert list(go.Heatmap(z=[1.0, 2.0]).z) == [1.0, 2.0]
    trace = go.Heatmap(z=np.zeros((2, 2)))
    assert isinstance(trace.z, np.ndarray)
    assert trace.z.shape == (2, 2)


def test_setters_accept_the_same_types_as_the_constructor() -> None:
    trace = go.Heatmap(z=Z)
    trace.x = [0, 1]
    trace.y = np.arange(2, dtype=np.float64)
    trace.z = np.zeros((2, 2))
    assert list(trace.x) == [0, 1]
    assert isinstance(trace.y, np.ndarray)
    assert isinstance(trace.z, np.ndarray)


def test_scalars_are_rejected() -> None:
    # `x`, `y` and `z` are array properties, so plotly rejects a scalar at runtime and the stub
    # rejects it statically -- hence the `type: ignore` comments, which are part of the assertion:
    # `warn_unused_ignores` turns a stub that starts accepting scalars into a CI failure.
    with pytest.raises(ValueError, match="Invalid value of type"):
        go.Heatmap(x=3, z=Z)  # type: ignore[arg-type]
    with pytest.raises(ValueError, match="Invalid value of type"):
        go.Heatmap(y=3.0, z=Z)  # type: ignore[arg-type]
    with pytest.raises(ValueError, match="Invalid value of type"):
        go.Heatmap(z=1.0)  # type: ignore[arg-type]


def test_a_bare_str_is_rejected_at_runtime_only() -> None:
    # `str` is itself a `Sequence[str]`, so no annotation can reject this statically without also
    # rejecting the `Sequence[str]` of issue #15. plotly rejects it at runtime.
    with pytest.raises(ValueError, match="Invalid value of type"):
        go.Heatmap(x="ab", z=Z)
