from pathlib import Path

import pandas as pd
import streamlit as st

from src.utils.io import ensure_dir, save_csv, load_model
from src.data_preprocessing import load_and_prepare, fit_transform
from src.clustering import train_kmeans, evaluate_clusters
from src.utils.viz import scatter_2d, bar_feature_by_cluster

st.title("Admin Panel")

st.subheader("Upload Data and Retrain")
uploaded = st.file_uploader("Upload study_logs.csv", type=["csv"])
if uploaded is not None:
    df = pd.read_csv(uploaded)
    st.write("Preview:")
    st.dataframe(df.head(), use_container_width=True)
    if st.button("Preprocess & Train KMeans"):
        df_prep = load_and_prepare(Path("dummy.csv")) if False else df
        X, artifacts = fit_transform(df_prep)
        model = train_kmeans(X)
        sil = evaluate_clusters(X, model.labels_)

        models_dir = Path("models")
        ensure_dir(models_dir)
        import joblib

        joblib.dump(artifacts, models_dir / "preprocess.joblib")
        joblib.dump(model, models_dir / "kmeans.joblib")
        st.success(f"Model trained. Silhouette: {sil}")

st.subheader("Visualizations")
models_ok = (Path("models") / "preprocess.joblib").exists()
if not models_ok:
    st.info("Train a model to enable visualizations.")
else:
    # demo visualization from a small sample if exists
    sample_path = Path("data/samples/study_logs.csv")
    if sample_path.exists():
        df = pd.read_csv(sample_path)
        st.write("Sample data preview:")
        st.dataframe(df.head(), use_container_width=True)
        if {"studyhours", "quizscore"}.issubset(df.columns):
            st.plotly_chart(scatter_2d(df, x="studyhours", y="quizscore", color=None, title="Hours vs Score"))
