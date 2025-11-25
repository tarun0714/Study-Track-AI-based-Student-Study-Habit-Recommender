Architecture Overview

- Data Sources: CSV uploads (mentor datasets), StudyLogs from UI
- Storage: SQLite (db/app.db), schema in db/schema.sql
- Processing: src/data_preprocessing.py -> feature engineering and pipelines
- Models: src/clustering.py (KMeans, DBSCAN) saved in models/
- Recommendations: src/recommendation.py (rule-based mapping per cluster)
- UI: Streamlit app with Student Dashboard and Admin Panel

Workflow
1. Admin uploads/collects study logs
2. Train clustering model; save preprocess + model artifacts
3. Student logs a session; system assigns cluster and generates weekly plan
4. Recommendations and adherence feedback stored; periodic retraining

Extensibility
- Replace rule-based recommendations with collaborative filtering using similarities within clusters
- Add RBAC for admin/student separation
- Move to MySQL by updating DSN and schema
