# RainCode Expense Tracker — Final

> A production-inspired, beginner-friendly Expense Tracker built with Python, Flask, and MySQL — crafted for [RainCode Open Class](https://raincode.id).

This is the layered version of the Expense Tracker capstone. Compare it with
[../starter](../starter): starter keeps SQL beside each Service use case, while
this version moves SQL into a Repository Layer for better separation.

---

## What Is This Project?

This is a **full-stack web application** that allows users to track personal expenses. It's designed as a **learning project** that demonstrates how professional developers think about building software — with clean architecture, separation of concerns, logging, and proper error handling.

**Not a toy project. Not enterprise-level. Just right.**

---

## Features

| Feature | Description |
|---|---|
| **Create Expense** | Add expenses with title, amount, category, and notes |
| **View Expenses** | Search, filter by category, and sort the expense list |
| **Update Expense** | Edit any expense detail |
| **Delete Expense** | Remove expenses with a confirmation dialog |
| **Dashboard** | Total spent, transaction count, average, recent activity |
| **Category Summary** | Visual breakdown of spending by category with percentages |
| **Logging** | All actions logged to file and console |
| **Responsive UI** | Works on mobile, tablet, and desktop |

---

## Tech Stack

```
Backend:   Python 3.12+, Flask 3.x
Frontend:  HTML5, CSS3 (CSS Variables), Vanilla JavaScript
Database:  MySQL 8.x with MySQL Connector/Python
Font:      Inter (Google Fonts)
Logging:   Python standard library logging module
Config:    python-dotenv (.env files)
```

---

## Architecture

This project uses **Clean Architecture** — separating code by responsibility:

```
Browser Request
    │
    ▼
┌─────────────────────────────────────────────────────────────────┐
│  app.py — Route Layer                                           │
│  Receives HTTP requests. Calls service. Returns HTML response.  │
└────────────────────────┬────────────────────────────────────────┘
                         │ calls
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│  expense_service.py — Service Layer                             │
│  Business logic: validates input, formats data, calculations.   │
└────────────────────────┬────────────────────────────────────────┘
                         │ calls
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│  expense_repository.py — Repository Layer                       │
│  Data access: all SQL queries live here and ONLY here.          │
└────────────────────────┬────────────────────────────────────────┘
                         │ uses
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│  database/db.py — Database Layer                                │
│  Manages MySQL connections. One place to change DB settings.    │
└────────────────────────┬────────────────────────────────────────┘
                         │ reads/writes
                         ▼
                     MySQL Database
                    (expense_tracker)
```

### Why This Architecture?

| Layer | Its Job | What It Does NOT Do |
|---|---|---|
| Route (`app.py`) | Handle HTTP, call service | Write SQL, validate data |
| Service | Validate, calculate, format | Write SQL, handle HTTP |
| Repository | Run SQL queries | Validate data, handle HTTP |
| Database (`db.py`) | Open/close connections | Write queries |

**Benefit:** Database-specific code is isolated in `db.py` and `expense_repository.py`; routes and templates do not open database connections.

---

## Project Structure

```
expense-tracker/
│
├── app.py                    ← Entry point. Flask routes. HTTP layer.
├── config.py                 ← All configuration from .env file
├── requirements.txt          ← Python packages to install
├── .env.example              ← Template: copy this to .env
├── .env                      ← Your local config (never commit!)
├── .gitignore                ← Files git should ignore
│
├── models/
│   └── expense_model.py      ← Expense data structure (blueprint)
│
├── repositories/
│   └── expense_repository.py ← All SQL queries (data access layer)
│
├── services/
│   └── expense_service.py    ← Business logic, validation, formatting
│
├── database/
│   └── db.py                 ← MySQL connection and schema initialization
│
├── utils/
│   └── logger.py             ← Logging configuration
│
├── templates/
│   ├── base.html             ← Master layout (nav, flash, footer)
│   ├── index.html            ← Dashboard page
│   ├── expenses.html         ← Expense list with search & filter
│   ├── create.html           ← Create expense form
│   ├── edit.html             ← Edit expense form
│   ├── summary.html          ← Category spending summary
│   └── errors/
│       ├── 404.html          ← Page not found
│       └── 500.html          ← Server error
│
├── static/
│   ├── css/
│   │   └── style.css         ← All styles (CSS Variables, responsive)
│   └── js/
│       └── app.js            ← Modal, nav, debounce, category colors
│
└── logs/
    └── app.log               ← Application logs (auto-created)
```

---

## Expense Categories

| Category | Description |
|---|---|
| Food | Meals, groceries, beverages |
| Transportation | Grab, KRL, bus, fuel, parking |
| Shopping | Clothes, electronics, household items |
| Bills | Electricity, internet, rent, subscriptions |
| Entertainment | Movies, games, concerts |
| Education | Books, courses, workshops |
| Other | Anything that doesn't fit above |

---

## Installation

### Prerequisites

- Python 3.12 or newer
- pip (Python package manager)
- MySQL Server 8.x

### Steps

**1. Masuk ke folder ini**

Project ini sudah ada di dalam repository RainCode Open Class yang kamu clone — tidak perlu clone terpisah.

```bash
cd projects/expense-tracker/final
```

**2. Create and activate a virtual environment**

```bash
# Create virtual environment
python -m venv venv

# Activate (Linux / macOS)
source venv/bin/activate

# Activate (Windows Command Prompt)
venv\Scripts\activate

# Activate (Windows PowerShell)
venv\Scripts\Activate.ps1
```

> **Why virtual environment?** Isolates this project's packages from your system Python. Every project can have different package versions without conflicts.

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Set up environment variables**

```bash
cp .env.example .env
# Edit .env if needed (defaults work out of the box for development)
```

**5. Create the MySQL database and user**

```sql
CREATE DATABASE expense_tracker
    CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'expense_app'@'localhost' IDENTIFIED BY 'change-this-local-password';
GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, ALTER, INDEX
    ON expense_tracker.* TO 'expense_app'@'localhost';
```

Set the same credentials in `.env`. The application creates the `expenses`
table, but the database and application user must already exist.

**6. Run the application**

```bash
python app.py
```

**7. Open in browser**

```
http://localhost:5000
```

The `expenses` table and log file (`logs/app.log`) are created automatically on first run.

---

## Usage

### Dashboard
Visit `http://localhost:5000` to see:
- Total amount spent
- Number of transactions
- Average per expense
- Recent transactions
- Category breakdown

### Add an Expense
1. Click **Add Expense** in the navigation bar
2. Fill in the title, amount, and category
3. Click **Save Expense**

### Search & Filter Expenses
Visit `/expenses` and use the search bar or category dropdown to filter.

### Edit an Expense
Click the pencil icon next to any expense in the list.

### Delete an Expense
Click the trash icon. A confirmation dialog appears before anything is deleted.

### View Summary
Visit `/summary` for a visual category breakdown with percentage bars.

---

## Database Schema

```sql
CREATE TABLE expenses (
    id          BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    title       VARCHAR(200)    NOT NULL,
    amount      DECIMAL(15, 2)  NOT NULL,
    category    VARCHAR(100)    NOT NULL DEFAULT 'Other',
    notes       TEXT            NOT NULL,
    created_at  DATETIME        NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at  DATETIME        NOT NULL DEFAULT CURRENT_TIMESTAMP
                                            ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
```

---

## Logging

All significant events are logged to both **terminal** and **`logs/app.log`**.

```
2024-01-15 14:30:25 | INFO     | app                           | Application started | env=development
2024-01-15 14:31:02 | INFO     | services.expense_service      | Expense created successfully | expense_id=1 category=Food amount=25000.0
2024-01-15 14:31:45 | WARNING  | services.expense_service      | Validation error on create: Amount is required.
2024-01-15 14:32:10 | INFO     | services.expense_service      | Expense deleted successfully | expense_id=1
2024-01-15 14:35:00 | ERROR    | database.db                   | Database initialization failed: Access denied
```

**Log Levels:**

| Level | When Used |
|---|---|
| `INFO` | Normal operations: started, created, updated, deleted |
| `WARNING` | Validation errors, unexpected input, missing resources |
| `ERROR` | Database failures, unexpected exceptions |
| `CRITICAL` | App cannot start (e.g. MySQL unavailable or credentials invalid) |

---

## Security Practices Demonstrated

| Practice | Where Applied |
|---|---|
| **Parameterized SQL Queries** | All values in `expense_repository.py` use `%s` placeholders — prevents SQL Injection |
| **Server-side Validation** | `expense_service.py` validates all input — client-side JavaScript can be bypassed |
| **POST for Mutations** | Create, Update, Delete use `POST`, not `GET` — prevents accidental/crawler-triggered actions |
| **Input Sanitization** | All form values are `.strip()`-ped to remove leading/trailing whitespace |
| **No Secret Exposure** | Error pages show friendly messages, not stack traces — full errors go to logs only |
| **Environment Variables** | Secrets in `.env`, never hardcoded in source files |

---

## Request Flow (Detailed)

```
1. User fills form and clicks "Save Expense"
      │
      ▼
2. Browser sends POST /create with form data
      │
      ▼
3. Flask router matches @app.route("/create", methods=["POST"])
      │
      ▼
4. create() function extracts data from request.form
      │
      ▼
5. expense_service.create_expense(form_data) is called
      │
      ▼
6. Service validates:
   - title not empty
   - amount is a number > 0
   - category is in approved list
      │ validation passes
      ▼
7. Service calls repository.create_expense(title, amount, category, notes)
      │
      ▼
8. Repository runs: INSERT INTO expenses (title, amount, category, notes) VALUES (%s, %s, %s, %s)
      │
      ▼
9. MySQL writes the row, returns auto-generated id
      │
      ▼
10. Repository fetches the complete row (with timestamps) and returns it
      │
      ▼
11. Service formats the data (currency string, etc.) and returns it
      │
      ▼
12. Route calls flash("Expense created!") and redirect(url_for("expenses"))
      │
      ▼
13. Browser follows redirect to GET /expenses
      │
      ▼
14. Jinja2 renders expenses.html with the updated list
      │
      ▼
15. User sees updated expenses list with success notification
```

---

## Learning Outcomes

After studying this project, you will understand:

### Python Fundamentals
- [x] Classes and methods
- [x] Type hints (`str`, `Decimal`, `Optional[dict]`, `list[dict]`)
- [x] Dataclasses (`@dataclass`)
- [x] Exception handling (`try/except/raise`)
- [x] f-strings and string formatting
- [x] Dictionary operations (`.get()`, unpacking with `**`)
- [x] List comprehensions

### Flask Framework
- [x] Creating a Flask app
- [x] URL routing with `@app.route()`
- [x] URL parameters (`<int:expense_id>`)
- [x] HTTP methods (GET vs POST)
- [x] `request.form` and `request.args`
- [x] `flash()` messages
- [x] `redirect()` and `url_for()`
- [x] Jinja2 templates (`{% extends %}`, `{% block %}`, `{% for %}`, `{% if %}`)
- [x] Error handlers (`@app.errorhandler`)

### Database
- [x] MySQL connection and transaction basics
- [x] SQL CRUD: INSERT, SELECT, UPDATE, DELETE
- [x] SQL aggregation: SUM, COUNT, GROUP BY
- [x] Parameterized queries (SQL Injection prevention)
- [x] MySQL Connector/Python
- [x] Dictionary cursors, commit, rollback, and resource cleanup

### Software Engineering
- [x] Layered architecture (Route → Service → Repository)
- [x] Separation of concerns
- [x] Configuration management with `.env`
- [x] Logging (what, why, and how)
- [x] Error handling patterns
- [x] PRG pattern (Post/Redirect/Get)

### Frontend
- [x] Semantic HTML5 (`<header>`, `<nav>`, `<main>`, `<footer>`)
- [x] CSS Variables (design tokens)
- [x] Responsive design with media queries
- [x] JavaScript: DOM manipulation, event listeners
- [x] JavaScript: Debounce pattern
- [x] Accessibility basics (`aria-*` attributes, `<label>`, `<th scope>`)

---

## Future Improvements

This project is designed as a foundation. Here are natural next steps:

| Feature | Concepts to Learn |
|---|---|
| **User Authentication** | Flask-Login, password hashing (bcrypt), sessions |
| **Multi-User Support** | Foreign keys, user_id in expenses table |
| **REST API** | Flask blueprints, `jsonify()`, API design |
| **CSV Export** | Python `csv` module, file downloads |
| **Monthly Reports** | Date filtering and MySQL date functions |
| **Pagination** | LIMIT/OFFSET in SQL, page number tracking |
| **Cloud Database** | Managed MySQL, TLS, backups, and connection pooling |
| **Deployment** | Gunicorn, Nginx, Railway, Render, or Fly.io |
| **Unit Tests** | `pytest`, mocking, testing each layer separately |
| **Dashboard Charts** | Chart.js integration with category data |

---

## Portfolio Description

When presenting this project, you can describe it as:

> *"A full-stack Expense Tracker application built with Python and Flask, using a 3-layer architecture (Route → Service → Repository) and MySQL for data persistence. Features include CRUD operations, search/filter/sort, category analytics, structured logging, Decimal-based money handling, transactions, and SQL Injection prevention via parameterized queries. The responsive UI is built with vanilla CSS and JavaScript."*

---

## About RainCode Open Class

This project was built as part of **RainCode Open Class** — a free, practical programming education initiative designed to help aspiring developers learn by building real applications.

Learn more: [raincode.id](https://raincode.id)

---

*Built with Python + Flask + MySQL · RainCode Open Class*
