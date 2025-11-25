import os
import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DB_PATH = ROOT / "db" / "app.db"
SCHEMA_PATH = ROOT / "db" / "schema.sql"
SAMPLES_DIR = ROOT / "data" / "samples"


def run_schema(conn: sqlite3.Connection) -> None:
    with open(SCHEMA_PATH, "r", encoding="utf-8") as f:
        conn.executescript(f.read())


def seed_minimal(conn: sqlite3.Connection) -> None:
    cur = conn.cursor()
    # Students
    cur.executemany(
        "INSERT OR IGNORE INTO Students(studentid, name, email) VALUES (?, ?, ?)",
        [
            (1, "Alice Kumar", "alice@example.com"),
            (2, "Brian Lee", "brian@example.com"),
            (3, "Chitra Rao", "chitra@example.com"),
        ],
    )

    # Clusters (initial profiles)
    cur.executemany(
        "INSERT OR IGNORE INTO Clusters(clusterid, name, averagestudyduration, recommendedmethod, breakinterval) VALUES (?, ?, ?, ?, ?)",
        [
            (0, "Focused Studiers", 2.0, "Pomodoro", 10),
            (1, "Night Owls", 1.5, "Spaced Repetition", 15),
            (2, "Short Burst Learners", 0.75, "Active Recall", 5),
            (3, "Distracted Learners", 0.5, "Distraction Blocking + Pomodoro", 5),
        ],
    )

    # StudyLogs (from samples if available)
    study_logs_csv = SAMPLES_DIR / "study_logs.csv"
    if study_logs_csv.exists():
        import csv

        with open(study_logs_csv, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            rows = [
                (
                    int(row["logid"]),
                    int(row["studentid"]),
                    row["date"],
                    float(row.get("studyhours", 0) or 0),
                    row.get("methodused") or None,
                    row.get("distractions") or None,
                    float(row.get("quizscore", 0) or 0),
                )
                for row in reader
            ]
        cur.executemany(
            "INSERT OR IGNORE INTO StudyLogs(logid, studentid, date, studyhours, methodused, distractions, quizscore) VALUES (?, ?, ?, ?, ?, ?, ?)",
            rows,
        )

    conn.commit()


def main() -> None:
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    if not SCHEMA_PATH.exists():
        raise FileNotFoundError(f"Missing schema: {SCHEMA_PATH}")

    with sqlite3.connect(DB_PATH) as conn:
        run_schema(conn)
        seed_minimal(conn)

    print(f"Database initialized at: {DB_PATH}")


if __name__ == "__main__":
    main()
