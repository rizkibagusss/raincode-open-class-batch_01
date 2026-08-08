"""
app.py - Flask Application & Route Definitions
================================================

WHY THIS FILE EXISTS:
    This is the entry point of the web application.
    It creates the Flask app, registers all URL routes, and starts the server.

WHAT ARE ROUTES?
    Routes map URLs to Python functions.

    When a user visits http://localhost:5000/create:
    1. Flask sees the URL /create
    2. Flask finds the matching @app.route("/create") decorator
    3. Flask calls the create() function below
    4. The function returns an HTML response

THIS FILE'S JOB (and ONLY its job):
    ✅ Receive HTTP requests
    ✅ Extract form data / URL parameters
    ✅ Call the service layer
    ✅ Handle success/error responses
    ✅ Return rendered HTML templates

THIS FILE DOES NOT:
    ❌ Write SQL queries (that's repositories/)
    ❌ Validate business rules (that's services/)
    ❌ Calculate summaries or format data (that's services/)

THE FULL REQUEST FLOW:
    Browser
       ↓   HTTP Request (GET /expenses?search=coffee)
    Flask Route (here)
       ↓   calls
    ExpenseService
       ↓   calls
    ExpenseRepository
       ↓   runs SQL
    MySQL Database
       ↑   returns rows
    ExpenseRepository
       ↑   returns dict
    ExpenseService
       ↑   returns formatted dict
    Flask Route (here)
       ↑   passes to
    Jinja2 Template (templates/*.html)
       ↑   renders HTML
    Browser displays page

HTTP METHODS — GET vs POST:
    GET:  "Give me this page / data." Safe, can be bookmarked, cached.
          Used for: viewing pages, searching, filtering
    POST: "Process this action / data." Changes state on the server.
          Used for: creating, updating, deleting records

    WHY NOT USE GET FOR DELETE?
    Browser prefetch, crawlers, and accidental clicks can trigger GET requests.
    A crawler scanning your site shouldn't be able to delete all your data!
    POST requires a deliberate form submission — it's intentional.
"""

from flask import Flask, flash, redirect, render_template, request, url_for

from config import config
from database.db import init_db
from services.expense_service import ExpenseService
from utils.logger import get_logger

# ── Logger ──────────────────────────────────────────────────────────────────────
logger = get_logger(__name__)

# ── Flask App Instance ──────────────────────────────────────────────────────────
# __name__ tells Flask where this file lives (used to locate templates/ and static/)
app = Flask(__name__)

# SECRET_KEY is required for flash messages and session data.
# In production: use a long random string in .env, never commit it!
app.secret_key = config.SECRET_KEY

# ── Database Setup ──────────────────────────────────────────────────────────────
# Create the expenses table if it doesn't already exist.
# Safe to call multiple times (IF NOT EXISTS handles it).
init_db()

# ── Service Instance ────────────────────────────────────────────────────────────
# One shared service instance for all routes.
expense_service = ExpenseService()

logger.info(f"Application started | name={config.APP_NAME} | env={config.APP_ENV}")


# ══════════════════════════════════════════════════════════════════════════════
# ROUTES
# ══════════════════════════════════════════════════════════════════════════════


@app.route("/")
def index():
    """
    Dashboard Route — Home Page

    Displays:
    - Summary statistics (total spent, transaction count, average)
    - Recent transactions (last 5)
    - Category breakdown with percentages

    URL:     GET /
    Template: templates/index.html
    """
    try:
        summary        = expense_service.get_summary()
        recent         = expense_service.get_recent_expenses(limit=config.RECENT_EXPENSES_LIMIT)
        category_totals = expense_service.get_category_totals()

        logger.info("Dashboard loaded successfully")

        return render_template(
            "index.html",
            page_title="Dashboard",
            summary=summary,
            recent_expenses=recent,
            category_totals=category_totals,
        )

    except Exception as e:
        logger.error(f"Error loading dashboard: {e}")
        flash("Could not load the dashboard. Please try again.", "error")
        return render_template(
            "index.html",
            page_title="Dashboard",
            summary={},
            recent_expenses=[],
            category_totals=[],
        )


@app.route("/expenses")
def expenses():
    """
    Expenses List Route

    Displays all expenses in a searchable, filterable, sortable table.

    URL Query Parameters:
        ?search=coffee           Filter by title/notes containing "coffee"
        ?category=Food           Filter by exact category
        ?sort=amount             Sort by column (default: created_at)
        ?order=asc               Sort direction (default: desc)

    Example:
        /expenses?search=grab&category=Transportation&sort=amount&order=desc

    URL:      GET /expenses
    Template: templates/expenses.html
    """
    try:
        # Read query parameters from the URL
        # request.args is Flask's dictionary of URL query parameters
        search   = request.args.get("search", "").strip()
        category = request.args.get("category", "").strip()
        sort_by  = request.args.get("sort", "created_at").strip()
        order    = request.args.get("order", "desc").strip()

        all_expenses = expense_service.get_expenses(
            search=search,
            category=category,
            sort_by=sort_by,
            order=order,
        )
        categories = expense_service.get_categories()

        logger.info(
            f"Expenses list loaded | "
            f"count={len(all_expenses)} search='{search}' category='{category}'"
        )

        return render_template(
            "expenses.html",
            page_title="Expenses",
            expenses=all_expenses,
            categories=categories,
            search=search,
            selected_category=category,
            sort_by=sort_by,
            order=order,
        )

    except Exception as e:
        logger.error(f"Error loading expenses list: {e}")
        flash("Could not load expenses. Please try again.", "error")
        return redirect(url_for("index"))


@app.route("/create", methods=["GET", "POST"])
def create():
    """
    Create Expense Route

    GET  /create → Display the empty create form
    POST /create → Process form submission, save expense, redirect

    WHY HANDLE BOTH GET AND POST IN ONE FUNCTION?
    This is a common pattern called "PRG" (Post/Redirect/Get).
    1. GET:  Show the form
    2. POST: Validate and save; if success → redirect; if error → show form again

    The redirect after successful POST prevents "form resubmission" when
    the user refreshes the page.

    URL:      GET/POST /create
    Template: templates/create.html
    """
    categories = expense_service.get_categories()

    if request.method == "POST":
        # request.form is Flask's dictionary of submitted form fields
        form_data = {
            "title":    request.form.get("title", "").strip(),
            "amount":   request.form.get("amount", "").strip(),
            "category": request.form.get("category", "").strip(),
            "notes":    request.form.get("notes", "").strip(),
        }

        try:
            expense = expense_service.create_expense(form_data)

            # flash() stores a one-time message shown on the next page
            flash(f"Expense '{expense['title']}' created successfully!", "success")

            # Redirect to /expenses after successful save (PRG pattern)
            return redirect(url_for("expenses"))

        except ValueError as ve:
            # ValueError = user's input was invalid
            # Show the error and re-display the form WITH the user's data still filled in
            logger.warning(f"Validation error on create: {ve}")
            flash(str(ve), "error")
            return render_template(
                "create.html",
                page_title="Create Expense",
                categories=categories,
                form_data=form_data,    # ← Re-fill the form so user doesn't retype everything
            )

        except Exception as e:
            # Unexpected error (database issue, etc.) — not the user's fault
            logger.error(f"Unexpected error creating expense: {e}")
            flash("Something went wrong. Please try again.", "error")
            return render_template(
                "create.html",
                page_title="Create Expense",
                categories=categories,
                form_data=form_data,
            )

    # GET request: display the empty form
    return render_template(
        "create.html",
        page_title="Create Expense",
        categories=categories,
        form_data={},           # Empty dict = blank form
    )


@app.route("/edit/<int:expense_id>", methods=["GET", "POST"])
def edit(expense_id: int):
    """
    Edit Expense Route

    <int:expense_id> is a URL converter:
    - /edit/42 → expense_id = 42 (integer)
    - Flask rejects /edit/abc automatically (not an int → 404)

    GET  /edit/<id> → Show form pre-filled with existing expense data
    POST /edit/<id> → Update the expense and redirect

    URL:      GET/POST /edit/<expense_id>
    Template: templates/edit.html
    """
    categories = expense_service.get_categories()

    # ── Look up the expense first ───────────────────────────────────────────────
    try:
        expense = expense_service.get_expense_by_id(expense_id)
    except Exception as e:
        logger.error(f"Error finding expense for edit | id={expense_id} | {e}")
        flash("Could not load the expense.", "error")
        return redirect(url_for("expenses"))

    if not expense:
        logger.warning(f"Edit attempted on non-existent expense | id={expense_id}")
        flash("Expense not found.", "error")
        return redirect(url_for("expenses"))

    if request.method == "POST":
        form_data = {
            "title":    request.form.get("title", "").strip(),
            "amount":   request.form.get("amount", "").strip(),
            "category": request.form.get("category", "").strip(),
            "notes":    request.form.get("notes", "").strip(),
        }

        try:
            updated = expense_service.update_expense(expense_id, form_data)

            flash(f"Expense '{updated['title']}' updated successfully!", "success")
            return redirect(url_for("expenses"))

        except ValueError as ve:
            logger.warning(f"Validation error on edit | id={expense_id} | {ve}")
            flash(str(ve), "error")
            return render_template(
                "edit.html",
                page_title="Edit Expense",
                expense=expense,
                categories=categories,
                form_data=form_data,
            )

        except Exception as e:
            logger.error(f"Unexpected error updating expense | id={expense_id} | {e}")
            flash("Something went wrong. Please try again.", "error")
            return render_template(
                "edit.html",
                page_title="Edit Expense",
                expense=expense,
                categories=categories,
                form_data=form_data,
            )

    # GET request: pre-fill form with existing expense data
    return render_template(
        "edit.html",
        page_title="Edit Expense",
        expense=expense,
        categories=categories,
        form_data=expense,      # ← expense dict pre-fills the form fields
    )


@app.route("/delete/<int:expense_id>", methods=["POST"])
def delete(expense_id: int):
    """
    Delete Expense Route

    WHY POST ONLY (no GET)?

    SECURITY LESSON:
    Destructive operations must NEVER be triggered by a GET request.
    GET requests can be triggered by:
    - Browser prefetch ("I'll load the next page the user might visit")
    - Search engine crawlers (Googlebot visiting every link it finds)
    - Antivirus scanning all links in the page
    - A user accidentally hovering over a link

    POST requires a deliberate form submission, so it must be intentional.
    This is standard web security practice (OWASP recommendation).

    The confirmation dialog in JavaScript adds another layer of protection.

    URL: POST /delete/<expense_id>
    """
    try:
        # Get expense info BEFORE deleting (for the flash message)
        expense = expense_service.get_expense_by_id(expense_id)

        if not expense:
            flash("Expense not found.", "error")
            return redirect(url_for("expenses"))

        expense_service.delete_expense(expense_id)
        flash(f"Expense '{expense['title']}' deleted successfully.", "success")

    except Exception as e:
        logger.error(f"Error deleting expense | id={expense_id} | {e}")
        flash("Could not delete the expense. Please try again.", "error")

    return redirect(url_for("expenses"))


@app.route("/summary")
def summary():
    """
    Summary / Analytics Route

    Displays spending breakdown by category with:
    - Total amount per category
    - Number of expenses per category
    - Percentage of total spending per category

    URL:      GET /summary
    Template: templates/summary.html
    """
    try:
        category_totals = expense_service.get_category_totals()
        overall         = expense_service.get_summary()

        logger.info("Summary page loaded")

        return render_template(
            "summary.html",
            page_title="Summary",
            category_totals=category_totals,
            summary=overall,
        )

    except Exception as e:
        logger.error(f"Error loading summary: {e}")
        flash("Could not load the summary.", "error")
        return redirect(url_for("index"))


# ══════════════════════════════════════════════════════════════════════════════
# ERROR HANDLERS
# ══════════════════════════════════════════════════════════════════════════════

@app.errorhandler(404)
def page_not_found(error):
    """Handle 404 Not Found — URL doesn't exist."""
    logger.warning(f"404 | {request.method} {request.url}")
    return render_template("errors/404.html", page_title="Page Not Found"), 404


@app.errorhandler(500)
def internal_server_error(error):
    """Handle 500 Internal Server Error — unexpected crash."""
    logger.error(f"500 | {error}")
    return render_template("errors/500.html", page_title="Server Error"), 500


# ══════════════════════════════════════════════════════════════════════════════
# ENTRY POINT
# ══════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    # This block runs ONLY when you execute: python app.py
    # In production, a WSGI server like Gunicorn runs the app instead:
    #   gunicorn app:app --workers 4 --bind 0.0.0.0:5000
    app.run(
        debug=config.DEBUG,
        host="0.0.0.0",    # Listen on all interfaces (required for WSL/Docker)
        port=5000,
    )
