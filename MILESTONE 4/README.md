# AI-based Student Study Habit Recommender

A modular Python + Streamlit project that recommends personalized study routines for students using behavioral data and clustering analysis.

## Features
- Data preprocessing: missing values, normalization, encoding, effectiveness labels
- Behavior clustering: K-Means and DBSCAN with visualizations and cluster profiles
- Recommendation engine: maps clusters to optimal habits and tools
- Web UI (Streamlit): student dashboard and admin panel
- SQLite storage, retraining hooks, feedback logging

## Tech Stack
- Python: pandas, scikit-learn, numpy, matplotlib/plotly, pydantic
- Streamlit for UI
- SQLite for storage (easily swappable to MySQL)

## Project Structure
```
.
├── README.md
├── requirements.txt
├── config.yaml
├── data/
│   ├── raw/
│   ├── processed/
│   └── samples/
│       ├── students.csv
│       ├── study_logs.csv
│       ├── distractions.csv
│       └── methods.csv
├── db/
│   ├── schema.sql
│   └── seed.py
├── docs/
│   ├── wireframes.md
│   └── architecture.md
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── database.py
│   ├── data_preprocessing.py
│   ├── clustering.py
│   ├── recommendation.py
│   ├── evaluation.py
│   ├── pipeline_train.py
│   ├── pipeline_assign.py
│   └── utils/
│       ├── __init__.py
│       ├── io.py
│       ├── features.py
│       └── viz.py
└── web/
    ├── app.py
    └── pages/
        ├── 1_Student_Dashboard.py
        └── 2_Admin_Panel.py
```

## Quickstart
1) Create virtual environment and install dependencies
```
python -m venv .venv
. .venv/Scripts/activate
pip install -r requirements.txt
```

2) Initialize database and seed samples
```
python db/seed.py
```

3) Train initial clustering models and rules
```
python -m src.pipeline_train --data data/samples/study_logs.csv
```

4) Run the app
```
streamlit run web/app.py
```

## Milestones
- Weeks 1–2: preprocessing, EDA, pattern analysis (src/data_preprocessing.py, src/utils/viz.py)
- Weeks 3–4: clustering and visualization (src/clustering.py), assign new users (src/pipeline_assign.py)
- Weeks 5–6: recommendation engine and weekly plan generation (src/recommendation.py)
- Weeks 7–8: UI (Streamlit), retraining, feedback loop (web/pages/*)

## Evaluation
- Model metrics: silhouette score, cluster stability
- Outcome: correlation between recommended habits and improved quiz scores (src/evaluation.py)
- Feedback loop: student adherence and feedback stored in DB, retraining hooks

## Notes
- Replace samples with mentor datasets when available
- Update config.yaml for paths and hyperparameters
- Switch to MySQL by updating DSN in src/database.py and applying an equivalent schema
