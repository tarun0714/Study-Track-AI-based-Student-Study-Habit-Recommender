from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd

from .utils.io import load_model, ensure_dir, save_csv
from .data_preprocessing import load_and_prepare, transform
from .recommendation import cluster_to_recommendation, weekly_plan


def main():
    parser = argparse.ArgumentParser(description="Assign clusters and generate recommendations")
    parser.add_argument("--data", type=str, required=True, help="Path to new study_logs CSV")
    parser.add_argument("--models", type=str, default="models", help="Models directory")
    parser.add_argument("--out", type=str, default="data/processed/assigned.csv", help="Output CSV")
    args = parser.parse_args()

    models_dir = Path(args.models)
    artifacts = load_model(models_dir / "preprocess.joblib")
    kmeans = load_model(models_dir / "kmeans.joblib")

    df = load_and_prepare(Path(args.data))
    X = transform(df, artifacts)

    labels = kmeans.predict(X)
    df_out = df.copy()
    df_out["cluster"] = labels

    # Example: add simple plan text column
    plans = []
    for lbl, hrs in zip(labels, df_out.get("studyhours", [1.5] * len(df_out))):
        rec = cluster_to_recommendation(int(lbl), float(hrs) if pd.notna(hrs) else None)
        plan = weekly_plan(rec, sessions_per_week=5)
        plans.append("; ".join(f"S{int(r['session'])}:{r['target_hours']}h {r['method']}" for _, r in plan.iterrows()))
    df_out["weekly_plan"] = plans

    save_csv(df_out, Path(args.out))
    print(f"Saved assignments to {args.out}")


if __name__ == "__main__":
    main()
