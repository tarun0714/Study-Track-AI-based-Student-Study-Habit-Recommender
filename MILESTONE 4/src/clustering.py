from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Optional

import numpy as np
import pandas as pd
from sklearn.cluster import DBSCAN, KMeans
from sklearn.metrics import silhouette_score

from .config import load_config


@dataclass
class ClusterModels:
    kmeans: Optional[KMeans]
    dbscan: Optional[DBSCAN]


@dataclass
class ClusterResult:
    labels: np.ndarray
    silhouette: Optional[float]


def train_kmeans(X: np.ndarray) -> KMeans:
    cfg = load_config()
    params = cfg.clustering.get("kmeans", {})
    model = KMeans(**params)
    model.fit(X)
    return model


def train_dbscan(X: np.ndarray) -> DBSCAN:
    cfg = load_config()
    params = cfg.clustering.get("dbscan", {})
    model = DBSCAN(**params)
    model.fit(X)
    return model


def evaluate_clusters(X: np.ndarray, labels: np.ndarray) -> Optional[float]:
    unique = set(labels)
    if len(unique) <= 1 or (-1 in unique and len(unique) == 2):
        return None
    try:
        return float(silhouette_score(X, labels))
    except Exception:
        return None


def assign_labels(model, X: np.ndarray) -> np.ndarray:
    if hasattr(model, "predict"):
        return model.predict(X)
    # fallback for DBSCAN
    return model.fit_predict(X)


def profile_clusters(df_features: pd.DataFrame, labels: np.ndarray, feature_cols: list[str]) -> pd.DataFrame:
    out = df_features.copy()
    out["cluster"] = labels
    summary = out.groupby("cluster")[feature_cols].mean().reset_index()
    return summary
