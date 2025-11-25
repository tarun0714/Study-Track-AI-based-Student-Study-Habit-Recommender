from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Tuple

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from .config import load_config
from .utils.features import compute_distractions_count, infer_time_of_day


@dataclass
class PreprocessArtifacts:
    pipeline: Pipeline
    feature_names: list[str]


def load_and_prepare(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path)
    if "date" in df.columns:
        # normalize date to ISO and keep as string; finer features extracted later
        df["date"] = pd.to_datetime(df["date"], errors="coerce")
    # engineered features
    if "distractions" in df.columns:
        df["distractions_count"] = compute_distractions_count(df)
    else:
        df["distractions_count"] = 0
    if "date" in df.columns:
        df["time_of_day"] = infer_time_of_day(df["date"])
    # simple sessions_per_day proxy: count logs by student-date
    if "studentid" in df.columns and "date" in df.columns:
        day = df["date"].dt.date
        df["sessions_per_day"] = (
            df.groupby(["studentid", day])
            .transform("count")["logid"].fillna(1)
            .astype(float)
        )
    else:
        df["sessions_per_day"] = 1.0

    # effectiveness label (optional) based on quizscore trend
    if "quizscore" in df.columns:
        df["effective"] = (df["quizscore"] >= df["quizscore"].median()).astype(int)

    # fill essential columns
    for col in ["studyhours", "quizscore"]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    # fallback defaults
    df["methodused"] = df.get("methodused", pd.Series(["Unknown"] * len(df)))
    df["time_of_day"] = df.get("time_of_day", pd.Series(["unknown"] * len(df)))

    return df


def build_preprocess_pipeline() -> Tuple[Pipeline, list[str]]:
    cfg = load_config()
    num_features = cfg.features.get("numerical", [])
    cat_features = cfg.features.get("categorical", [])

    numeric_transformer = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="median")),
            ("scaler", StandardScaler()),
        ]
    )

    categorical_transformer = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("onehot", OneHotEncoder(handle_unknown="ignore")),
        ]
    )

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", numeric_transformer, num_features),
            ("cat", categorical_transformer, cat_features),
        ]
    )

    # construct feature names after fit using get_feature_names_out
    feature_names = num_features + cat_features
    return preprocessor, feature_names


def fit_transform(df: pd.DataFrame) -> Tuple[np.ndarray, PreprocessArtifacts]:
    preprocessor, feature_names = build_preprocess_pipeline()
    X = preprocessor.fit_transform(df)
    # resolve feature names for one-hot
    if hasattr(preprocessor, "get_feature_names_out"):
        names = list(preprocessor.get_feature_names_out())
    else:
        names = feature_names
    artifacts = PreprocessArtifacts(pipeline=preprocessor, feature_names=names)
    return X, artifacts


def transform(df: pd.DataFrame, artifacts: PreprocessArtifacts) -> np.ndarray:
    return artifacts.pipeline.transform(df)
