"""Loading and saving expenses to disk."""

import json
import logging
from pathlib import Path

from config import DATA_FILE
from models import Expense

logger = logging.getLogger(__name__)


def load_expenses() -> list[Expense]:
    path = Path(DATA_FILE)
    if not path.exists():
        return []

    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            return [Expense.from_dict(item) for item in data]
    except (json.JSONDecodeError, KeyError, ValueError) as e:
        logger.error(f"Failed to parse expense data from {path}: {e}")
        return []  # Return an empty list or raise a custom domain exception
    except PermissionError:
        logger.error(f"Permission denied reading {path}")
        raise


def save_expenses(expenses: list[Expense]) -> None:
    path = Path(DATA_FILE)
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            json.dump([e.to_dict() for e in expenses], f, indent=2)
    except (PermissionError, OSError) as e:
        logger.error(f"Failed to save expenses to {path}: {e}")
        raise