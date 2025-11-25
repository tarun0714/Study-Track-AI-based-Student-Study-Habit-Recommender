from __future__ import annotations

import yaml
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict


CONFIG_PATH = Path(__file__).resolve().parents[1] / "config.yaml"


@dataclass
class AppConfig:
    paths: Dict[str, Any]
    clustering: Dict[str, Any]
    features: Dict[str, Any]
    recommendations: Dict[str, Any]


def load_config(path: Path | None = None) -> AppConfig:
    cfg_path = path or CONFIG_PATH
    with open(cfg_path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    return AppConfig(
        paths=data.get("paths", {}),
        clustering=data.get("clustering", {}),
        features=data.get("features", {}),
        recommendations=data.get("recommendations", {}),
    )
