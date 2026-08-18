from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

DATA_FILE = BASE_DIR / "expenses.json"

CATEGORIES = [
    "Food",
    "Entertainment",
    "Utilities",
    "Clothing",
    "Medical",
    "Travel",
    "Other",
]