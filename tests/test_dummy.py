# pyright: reportPrivateUsage=false

import plotly.graph_objects as go


def test_figure() -> None:
    # Prepare
    figure = go.Figure()
    # Execute
    data = figure.to_dict()
    # Assert
    assert data["data"] == []
