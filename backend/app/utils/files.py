from __future__ import annotations
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[2] / "data"
DATA_DIR.mkdir(exist_ok=True)


def save_text(task_id: str, filename: str, text: str) -> Path:
    """Save text for a research task and return the file path."""
    task_dir = DATA_DIR / task_id
    task_dir.mkdir(parents=True, exist_ok=True)
    path = task_dir / filename
    path.write_text(text, encoding="utf-8")
    return path
