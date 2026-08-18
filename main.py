import services
from utils import format_currency, format_table


def handle_add():
    try:
        amount = float(input("Enter amount: "))
        if amount <= 0:
            print("Amount must be greater than 0.")
            return
    except ValueError:
        print("Invalid input. Please enter a valid number for amount.")
        return

    category = input("Enter category: ").strip()
    description = input("Enter description: ").strip()

    if not category:
        print("Category cannot be empty.")
        return

    expense = services.add_expense(amount, category, description)
    print(
        f"\nAdded {format_currency(expense.amount)} "
        f"to '{expense.category}' (id: {expense.id})\n"
    )


def handle_delete():
    expense_id = input("Enter the expense ID to delete: ").strip()
    if not expense_id:
        print("ID cannot be empty.")
        return

    if services.delete_expense(expense_id):
        print(f"\nDeleted expense {expense_id}\n")
    else:
        print(f"\nNo expense with id '{expense_id}'.\n")


def handle_view_total():
    month = input("Filter by month (YYYY-MM, or press Enter for all): ").strip() or None

    expenses = services.list_expenses(month=month)
    if not expenses:
        print("\nNo expenses found.\n")
        return

    rows = [
        [e.id, e.date, e.category, format_currency(e.amount), e.description]
        for e in expenses
    ]

    print("\n" + format_table(rows, ["ID", "Date", "Category", "Amount", "Description"]))
    print(f"Total: {format_currency(sum(e.amount for e in expenses))}\n")


def print_menu():
    print("=" * 30)
    print("      EXPENSE TRACKER")
    print("=" * 30)
    print("1. Add Expense")
    print("2. Delete Expense")
    print("3. View Expenses / Total")
    print("4. Exit")
    print("-" * 30)


def main():
    while True:
        print_menu()
        choice = input("Select an option (1-4): ").strip()

        if choice == "1":
            handle_add()
        elif choice == "2":
            handle_delete()
        elif choice == "3":
            handle_view_total()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("\nInvalid option. Please choose between 1 and 4.\n")


if __name__ == "__main__":
    main()