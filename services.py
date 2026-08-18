
from collections import defaultdict

from models import Expense
from storage import load_expenses, save_expenses


def add_expense(amount: float, category: str, description: str) -> Expense:
    if amount <= 0:
        raise ValueError("Amount must be positive.")
    expenses = load_expenses()
    expense = Expense(amount=amount, category=category.lower(),
                      description=description)
    expenses.append(expense)
    save_expenses(expenses)
    return expense


def delete_expense(expense_id: str) -> bool:
    expenses = load_expenses()
    remaining = [e for e in expenses if e.id != expense_id]
    if len(remaining) == len(expenses):
        return False
    save_expenses(remaining)
    return True


def list_expenses(month: str | None = None) -> list[Expense]:
    expenses = load_expenses()
    if month:  # e.g. "2026-08"
        expenses = [e for e in expenses if e.date.startswith(month)]
    return sorted(expenses, key=lambda e: e.date)


def summary_by_category(month: str | None = None) -> dict[str, float]:
    totals = defaultdict(float)
    for e in list_expenses(month):
        totals[e.category] += e.amount
    return dict(sorted(totals.items(), key=lambda kv: kv[1], reverse=True))