from __future__ import annotations

import sqlite3
from pathlib import Path
from typing import Iterable, Optional, Sequence, Tuple

from .config import load_config


def get_db_path() -> Path:
    cfg = load_config()
    return Path(cfg.paths.get("database", "db/app.db"))


def connect(db_path: Optional[Path] = None) -> sqlite3.Connection:
    path = db_path or get_db_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    return conn


def execute(sql: str, params: Sequence | None = None) -> None:
    with connect() as conn:
        conn.execute(sql, params or [])
        conn.commit()


def executemany(sql: str, rows: Iterable[Sequence]) -> None:
    with connect() as conn:
        conn.executemany(sql, rows)
        conn.commit()


def query(sql: str, params: Sequence | None = None) -> list[sqlite3.Row]:
    with connect() as conn:
        cur = conn.execute(sql, params or [])
        return cur.fetchall()
