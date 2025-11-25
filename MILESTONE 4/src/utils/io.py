from __future__ import annotations

from pathlib import Path
from typing import Optional

import joblib
import pandas as pd


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def load_csv(path: Path) -> pd.DataFrame:
    return pd.read_csv(path)


def save_csv(df: pd.DataFrame, path: Path) -> None:
    ensure_dir(path.parent)
    df.to_csv(path, index=False)


def save_model(obj, path: Path) -> None:
    ensure_dir(path.parent)
    joblib.dump(obj, path)


def load_model(path: Path):
    return joblib.load(path)
