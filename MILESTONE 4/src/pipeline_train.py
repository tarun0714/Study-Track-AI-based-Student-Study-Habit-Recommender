from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd

from .config import load_config
from .data_preprocessing import fit_transform, load_and_prepare
from .clustering import train_kmeans, train_dbscan, evaluate_clusters
from .utils.io import save_model, ensure_dir


def main():
    parser = argparse.ArgumentParser(description="Train clustering models")
    parser.add_argument("--data", type=str, required=True, help="Path to study_logs CSV")
    args = parser.parse_args()

    cfg = load_config()
    models_dir = Path(cfg.paths.get("models", "models"))
    ensure_dir(models_dir)

    df = load_and_prepare(Path(args.data))
    X, artifacts = fit_transform(df)

    kmeans = train_kmeans(X)
    dbscan = train_dbscan(X)

    km_labels = kmeans.labels_
    km_sil = evaluate_clusters(X, km_labels)

    print(f"KMeans clusters: {len(set(km_labels))}, silhouette: {km_sil}")

    # Save models and preprocessing pipeline
    save_model(artifacts, models_dir / "preprocess.joblib")
    save_model(kmeans, models_dir / "kmeans.joblib")
    save_model(dbscan, models_dir / "dbscan.joblib")


if __name__ == "__main__":
    main()
