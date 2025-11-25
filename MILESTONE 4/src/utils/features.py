from __future__ import annotations

import pandas as pd


def compute_distractions_count(df: pd.DataFrame) -> pd.Series:
    # 'distractions' is pipe or comma separated string; count items
    def count_items(val: str | float | None) -> int:
        if not isinstance(val, str) or not val.strip():
            return 0
        # split on comma or pipe
        parts = [p.strip() for p in val.replace("|", ",").split(",") if p.strip()]
        return len(parts)

    return df["distractions"].apply(count_items)


essential_time_buckets = {
    "morning": (5, 12),
    "afternoon": (12, 17),
    "evening": (17, 21),
    "night": (21, 24),
}


def infer_time_of_day(date_series: pd.Series) -> pd.Series:
    dt = pd.to_datetime(date_series, errors="coerce")
    hours = dt.dt.hour.fillna(12)

    def bucket(h: float) -> str:
        if 5 <= h < 12:
            return "morning"
        if 12 <= h < 17:
            return "afternoon"
        if 17 <= h < 21:
            return "evening"
        return "night"

    return hours.apply(bucket)
