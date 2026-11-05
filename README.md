# 💰 CLI Expense Tracker

A clean, modular, and user-friendly **Command-Line Expense Tracker** built with Python.

The application allows users to record, view, filter, summarize, and delete expenses directly from the terminal. It uses **JSON-based local storage** for data persistence and follows a modular architecture that separates data models, storage operations, business logic, utilities, and the user interface.

---

## 📌 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Project Architecture](#-project-architecture)
- [Project Structure](#-project-structure)
- [How It Works](#-how-it-works)
- [Requirements](#-requirements)
- [Installation](#-installation)
- [Running the Application](#-running-the-application)
- [Application Interface](#-application-interface)
- [Expense Data Structure](#-expense-data-structure)
- [Example Workflow](#-example-workflow)
- [Architecture Principles](#-architecture-principles)
- [Data Persistence](#-data-persistence)
- [Error Handling](#-error-handling)
- [Future Improvements](#-future-improvements)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🎯 Overview

**CLI Expense Tracker** is a lightweight personal finance application designed to demonstrate how a Python application can be structured using a **modular and maintainable architecture**.

Instead of placing all functionality inside a single Python file, the project divides responsibilities across multiple modules:

- **Models** → Define application data
- **Storage** → Handle JSON file operations
- **Services** → Implement business logic
- **Utils** → Provide reusable display and formatting helpers
- **Main** → Manage the command-line user interface
- **Config** → Store application configuration and constants

This approach makes the application easier to understand, test, maintain, and extend.

---

## ✨ Features

### 📝 Add Expenses

Record an expense by providing:

- Amount
- Category
- Description
- Date

Example:

```text
Amount: 2500
Category: Food
Description: Dinner with friends
```

---

### 🗑️ Delete Expenses

Remove an existing expense from the tracker using its identifier.

---

### 📊 View Expenses

Display recorded expenses in a structured and readable format.

Users can view:

- Individual expenses
- Expense categories
- Descriptions
- Dates
- Amounts
- Total spending

---

### 📅 Monthly Filtering

Filter expenses by a specific month using the `YYYY-MM` format.

Example:

```text
2026-08
```

This allows users to analyze how much they spent during a particular month.

---

### 💵 Expense Summaries

The application can calculate total spending based on:

- All recorded expenses
- A specific month
- Selected expense records

---

### 💾 JSON Data Persistence

Expense data is automatically stored locally in a JSON file.

This means data remains available even after the application is closed.

---

### 🛡️ Data Validation

The application validates stored data and handles invalid or corrupted JSON data gracefully.

---

### 🧩 Modular Architecture

The project follows a separation-of-concerns approach.

Each module has a specific responsibility, making the application easier to maintain and test.

---

## 🏗️ Project Architecture

The application follows a layered architecture:

```text
                    ┌─────────────────────┐
                    │      main.py        │
                    │     CLI / UI        │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │    services.py      │
                    │   Business Logic    │
                    └──────────┬──────────┘
                               │
                    ┌──────────┴──────────┐
                    ▼                     ▼
          ┌─────────────────┐   ┌─────────────────┐
          │    models.py    │   │    storage.py   │
          │   Data Models   │   │  JSON Storage   │
          └─────────────────┘   └─────────────────┘
                                        │
                                        ▼
                                ┌───────────────┐
                                │   data.json   │
                                │ Persistent DB │
                                └───────────────┘

                    ┌─────────────────────┐
                    │      utils.py       │
                    │ Formatting / Output │
                    └─────────────────────┘

                    ┌─────────────────────┐
                    │      config.py      │
                    │ Configuration      │
                    └─────────────────────┘
```

### Module Responsibilities

| Module | Responsibility |
|---|---|
| `config.py` | Application configuration and constants |
| `models.py` | Expense data model |
| `storage.py` | Reading and writing JSON data |
| `services.py` | Expense CRUD operations and calculations |
| `utils.py` | Formatting and display helpers |
| `main.py` | CLI interface and application flow |

---

## 📂 Project Structure

```text
Expense-Tracker/
│
├── config.py
├── models.py
├── storage.py
├── services.py
├── utils.py
├── main.py
│
├── data/
│   └── expenses.json
│
├── .gitignore
├── requirements.txt
└── README.md
```

> The `data/` directory can be created automatically by the application if it does not already exist.

---

## ⚙️ How It Works

The application follows this general workflow:

```text
User
  │
  ▼
CLI Interface
(main.py)
  │
  ▼
Business Logic
(services.py)
  │
  ├──────────────► Data Model
  │                (models.py)
  │
  ▼
Storage Layer
(storage.py)
  │
  ▼
JSON File
(expenses.json)
```

### Step 1 — User Input

The user interacts with the application through the terminal.

### Step 2 — Validation

Input values such as amount, category, and date are validated.

### Step 3 — Create Expense

A new `Expense` object is created using the data model.

### Step 4 — Business Logic

The service layer processes the requested operation.

### Step 5 — Persistence

The storage layer saves the updated data to the JSON file.

### Step 6 — Display

The CLI displays the result to the user in a readable format.

---

## 📋 Requirements

### Software

- Python **3.9+**
- pip

### Python Libraries

The project primarily uses Python's standard library.

If additional dependencies are used, they are listed in:

```text
requirements.txt
```

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Expense-Tracker.git
```

Navigate to the project directory:

```bash
cd Expense-Tracker
```

---

### 2. Create a Virtual Environment

Windows:

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Install Dependencies

If the project contains external dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

Run the application using:

```bash
python main.py
```

The application will display the main menu:

```text
==============================
       EXPENSE TRACKER
==============================

1. Add Expense
2. Delete Expense
3. View Expenses / Total
4. Exit

------------------------------
Select an option (1-4):
```

---

## 🖥️ Application Interface

### Main Menu

```text
==============================
       EXPENSE TRACKER
==============================

1. Add Expense
2. Delete Expense
3. View Expenses / Total
4. Exit

------------------------------
Select an option (1-4):
```

### Add Expense

```text
Enter amount: 2500
Enter category: Food
Enter description: Dinner
Enter date: 2026-08-18

Expense added successfully!
```

### View Expenses

```text
ID   Date          Category    Amount    Description
-----------------------------------------------------
1    2026-08-18    Food        2500      Dinner
2    2026-08-17    Transport   800       Fuel
3    2026-08-15    Bills       5000      Electricity

Total Expenses: 8300
```

### Monthly Summary

```text
Enter month (YYYY-MM): 2026-08

Total expenses for 2026-08: 8300
```

---

## 🧱 Expense Data Structure

Expenses can be represented using a Python `dataclass`.

Conceptually, an expense contains:

```text
Expense
├── id
├── amount
├── category
├── description
└── date
```

Example JSON representation:

```json
{
    "id": 1,
    "amount": 2500,
    "category": "Food",
    "description": "Dinner with friends",
    "date": "2026-08-18"
}
```

---

## 🔄 Example Workflow

A typical user session might look like this:

```text
Start Application
       │
       ▼
   Main Menu
       │
       ▼
  Add Expense
       │
       ▼
Enter Expense Details
       │
       ▼
 Validate Input
       │
       ▼
Save to JSON
       │
       ▼
Return to Main Menu
       │
       ▼
 View Expenses
       │
       ▼
Calculate Total
       │
       ▼
 Display Results
```

---

## 🧠 Architecture Principles

This project follows several important software engineering principles.

### 1. Separation of Concerns

Each module has a clearly defined responsibility.

For example:

```text
main.py      → User interaction
services.py  → Business rules
storage.py   → File operations
models.py    → Data representation
utils.py     → Formatting
```

This prevents the application from becoming a large monolithic Python file.

---

### 2. Single Responsibility

Each component should ideally have one primary responsibility.

For example, `storage.py` should handle data persistence rather than calculating monthly expenses.

---

### 3. Reusability

Common functionality is placed inside reusable functions and modules instead of being duplicated throughout the application.

---

### 4. Maintainability

Because responsibilities are separated, changes can be made to one part of the application without unnecessarily modifying the entire project.

For example, JSON storage could later be replaced with SQLite while keeping most of the business logic unchanged.

---

### 5. Testability

The business logic in `services.py` can be tested independently from the command-line interface.

This makes automated testing easier to implement.

---

## 💾 Data Persistence

The application uses a local JSON file to persist expense data.

Example:

```text
data/
└── expenses.json
```

A simplified file might look like:

```json
[
    {
        "id": 1,
        "amount": 2500,
        "category": "Food",
        "description": "Dinner",
        "date": "2026-08-18"
    },
    {
        "id": 2,
        "amount": 800,
        "category": "Transport",
        "description": "Fuel",
        "date": "2026-08-17"
    }
]
```

### Why JSON?

JSON is suitable for this project because it is:

- Lightweight
- Human-readable
- Easy to parse with Python
- Easy to inspect manually
- Suitable for a small local application

For a larger production application, a database such as **SQLite** or **PostgreSQL** would be more appropriate.

---

## 🛡️ Error Handling

The application is designed to handle common input and storage problems gracefully.

Examples include:

- Invalid amount
- Empty category
- Invalid date format
- Invalid menu selection
- Missing data file
- Corrupted JSON data
- Attempting to delete a non-existent expense

Instead of unexpectedly terminating, the application should provide a meaningful error message and allow the user to continue.

Example:

```text
Invalid amount.

Please enter a valid numeric value.
```

---

## 🔮 Future Improvements

The project can be extended with several useful features.

### Expense Management

- [ ] Edit existing expenses
- [ ] Search expenses
- [ ] Filter by category
- [ ] Sort expenses by date or amount
- [ ] Recurring expenses

### Reporting

- [ ] Category-wise spending summary
- [ ] Monthly spending reports
- [ ] Yearly spending reports
- [ ] Highest and lowest expenses
- [ ] Average monthly spending

### Visualization

- [ ] Generate expense charts
- [ ] Category-wise pie charts
- [ ] Monthly spending bar charts

### Data Storage

- [ ] Replace JSON with SQLite
- [ ] Add database migrations
- [ ] Add automatic backups
- [ ] Export data to CSV

### User Experience

- [ ] Colored terminal output
- [ ] Better table formatting
- [ ] Command-line arguments
- [ ] Configuration file
- [ ] Multiple user profiles

### Testing

- [ ] Unit tests
- [ ] Integration tests
- [ ] Input validation tests
- [ ] Storage layer tests

---

## 🧪 Testing

Automated tests can be added to verify:

```text
├── Expense creation
├── Expense deletion
├── Expense filtering
├── Total calculation
├── Monthly summaries
├── JSON persistence
└── Input validation
```

A future test structure could look like:

```text
tests/
│
├── test_models.py
├── test_services.py
├── test_storage.py
└── test_utils.py
```

---

## 🤝 Contributing

Contributions are welcome!

To contribute:

### 1. Fork the repository

Create your own fork of the project.

### 2. Create a feature branch

```bash
git checkout -b feature/new-feature
```

### 3. Make your changes

Implement and test your changes.

### 4. Commit your changes

```bash
git commit -m "Add new expense feature"
```

### 5. Push the branch

```bash
git push origin feature/new-feature
```

### 6. Open a Pull Request

Create a Pull Request describing your changes.

---

## 📄 License

This project is available for educational and personal use.

You can add a specific open-source license such as **MIT License** if you plan to distribute the project publicly.

---

## 👨‍💻 Author

**Your Name**

If you found this project useful, consider ⭐ starring the repository.

---

## 📌 Project Status

**Status:** 🟢 Active Development

This project is designed as a practical Python application demonstrating:

- Object-Oriented Programming
- Python Dataclasses
- Modular Programming
- CRUD Operations
- JSON File Handling
- Data Validation
- Separation of Concerns
- Clean Architecture Principles
- Command-Line Application Development

---

### ⭐ If You Like This Project

If this project helped you learn Python or software architecture, consider giving the repository a ⭐ on GitHub.
