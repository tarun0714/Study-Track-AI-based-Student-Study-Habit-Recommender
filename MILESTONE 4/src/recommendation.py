from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List

import pandas as pd

from .config import load_config


@dataclass
class Recommendation:
    recommended_hours: float
    suggested_method: str
    tools: List[str]
    breakpattern: str


DEFAULT_TOOLS = {
    "Pomodoro": ["Timer", "Focus music", "Website blocker"],
    "Spaced Repetition": ["Anki", "Flashcards"],
    "Active Recall": ["Practice problems", "Whiteboard"],
    "Distraction Blocking + Pomodoro": ["Cold Turkey", "Forest", "Timer"],
}


def cluster_to_recommendation(cluster_id: int, avg_studyhours: float | None = None) -> Recommendation:
    cfg = load_config()
    profile = cfg.recommendations.get("cluster_profiles", {}).get(int(cluster_id), {})
    method = profile.get("recommendedmethod", "Pomodoro")
    break_interval = int(profile.get("breakinterval", 10))

    hours = avg_studyhours if avg_studyhours is not None else 1.5
    tools = DEFAULT_TOOLS.get(method, ["Timer"])

    return Recommendation(
        recommended_hours=float(hours),
        suggested_method=method,
        tools=tools,
        breakpattern=f"{break_interval} minutes break"
    )


def weekly_plan(rec: Recommendation, sessions_per_week: int = 5) -> pd.DataFrame:
    rows = []
    for i in range(1, sessions_per_week + 1):
        rows.append(
            {
                "session": i,
                "target_hours": rec.recommended_hours,
                "method": rec.suggested_method,
                "tools": ", ".join(rec.tools),
                "breaks": rec.breakpattern,
            }
        )
    return pd.DataFrame(rows)
