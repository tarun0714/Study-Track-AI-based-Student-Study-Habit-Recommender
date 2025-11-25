from __future__ import annotations

import pandas as pd
import plotly.express as px


def scatter_2d(df: pd.DataFrame, x: str, y: str, color: str | None = None, title: str | None = None):
    fig = px.scatter(df, x=x, y=y, color=color, title=title)
    return fig


def bar_feature_by_cluster(df: pd.DataFrame, feature: str, cluster_col: str = "cluster", title: str | None = None):
    grouped = df.groupby(cluster_col)[feature].mean().reset_index()
    fig = px.bar(grouped, x=cluster_col, y=feature, title=title or f"Avg {feature} by cluster")
    return fig
