import datetime as dt
from pathlib import Path

import pandas as pd
import streamlit as st

from src.database import execute, query
from src.utils.io import load_model
from src.data_preprocessing import load_and_prepare, transform
from src.recommendation import cluster_to_recommendation, weekly_plan

st.title("Student Dashboard")

student_rows = query("SELECT studentid, name FROM Students ORDER BY name")
student_map = {f"{r['name']} (ID {r['studentid']})": r["studentid"] for r in student_rows}

with st.form("log_form"):
    student_choice = st.selectbox("Student", list(student_map.keys()))
    date = st.date_input("Study Date", value=dt.date.today())
    studyhours = st.number_input("Study Hours", min_value=0.0, max_value=12.0, value=1.5, step=0.25)
    methodused = st.selectbox("Method Used", ["Pomodoro", "Spaced Repetition", "Active Recall", "Other"])
    distractions = st.text_input("Distractions (comma-separated)", value="")
    quizscore = st.number_input("Quiz Score (0-100)", min_value=0.0, max_value=100.0, value=75.0, step=1.0)
    submitted = st.form_submit_button("Log Session & Get Suggestion")

if submitted:
    sid = student_map[student_choice]
    execute(
        "INSERT INTO StudyLogs(studentid, date, studyhours, methodused, distractions, quizscore) VALUES (?, ?, ?, ?, ?, ?)",
        (sid, date.isoformat(), float(studyhours), methodused, distractions, float(quizscore)),
    )

    # Build a tiny dataframe for assignment
    df = pd.DataFrame([
        {
            "logid": 0,
            "studentid": sid,
            "date": date,
            "studyhours": studyhours,
            "methodused": methodused,
            "distractions": distractions,
            "quizscore": quizscore,
        }
    ])

    models_dir = Path("models")
    try:
        artifacts = load_model(models_dir / "preprocess.joblib")
        kmeans = load_model(models_dir / "kmeans.joblib")
        df_prep = df.copy()
        X = transform(load_and_prepare(Path("dummy.csv")) if False else df_prep, artifacts)  # uses same columns
        label = int(kmeans.predict(X)[0])
    except Exception:
        # fallback if models not trained yet
        label = 0

    rec = cluster_to_recommendation(label, float(studyhours))
    st.subheader("Suggested Weekly Plan")
    st.dataframe(weekly_plan(rec, sessions_per_week=5), use_container_width=True)
