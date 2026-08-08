"""Flask routes untuk Expense Tracker versi starter yang disederhanakan."""

from flask import Flask, flash, redirect, render_template, request, url_for

from config import config
from database.db import init_db
from services.expense_service import ExpenseService
from utils.logger import get_logger

logger = get_logger(__name__)

app = Flask(__name__)
app.secret_key = config.SECRET_KEY

init_db()
expense_service = ExpenseService()


@app.route("/")
def index():
    """Tampilkan dashboard dan ringkasan pengeluaran."""
    try:
        return render_template(
            "index.html",
            page_title="Dashboard",
            summary=expense_service.get_summary(),
            recent_expenses=expense_service.get_recent_expenses(
                config.RECENT_EXPENSES_LIMIT
            ),
            category_totals=expense_service.get_category_totals(),
        )
    except Exception as exc:
        logger.error("Failed to load dashboard | %s", exc)
        flash("Could not load the dashboard.", "error")
        return render_template(
            "index.html",
            page_title="Dashboard",
            summary={},
            recent_expenses=[],
            category_totals=[],
        )


@app.route("/expenses")
def expenses():
    """Tampilkan daftar expense beserta search, filter, dan sorting."""
    search = request.args.get("search", "").strip()
    category = request.args.get("category", "").strip()
    sort_by = request.args.get("sort", "created_at").strip()
    order = request.args.get("order", "desc").strip()

    try:
        rows = expense_service.get_expenses(search, category, sort_by, order)
        return render_template(
            "expenses.html",
            page_title="Expenses",
            expenses=rows,
            categories=expense_service.get_categories(),
            search=search,
            selected_category=category,
            sort_by=sort_by,
            order=order,
        )
    except Exception as exc:
        logger.error("Failed to load expenses | %s", exc)
        flash("Could not load expenses.", "error")
        return redirect(url_for("index"))


@app.route("/create", methods=["GET", "POST"])
def create():
    """Tampilkan form atau jalankan query INSERT melalui Service."""
    categories = expense_service.get_categories()
    form_data = {}

    if request.method == "POST":
        form_data = _expense_form_data()
        try:
            expense = expense_service.create_expense(form_data)
            flash(f"Expense '{expense['title']}' created successfully!", "success")
            return redirect(url_for("expenses"))
        except ValueError as exc:
            flash(str(exc), "error")
        except Exception as exc:
            logger.error("Failed to create expense | %s", exc)
            flash("Something went wrong. Please try again.", "error")

    return render_template(
        "create.html",
        page_title="Create Expense",
        categories=categories,
        form_data=form_data,
    )


@app.route("/edit/<int:expense_id>", methods=["GET", "POST"])
def edit(expense_id: int):
    """Tampilkan form atau jalankan query UPDATE melalui Service."""
    try:
        expense = expense_service.get_expense_by_id(expense_id)
    except Exception as exc:
        logger.error("Failed to find expense | id=%s | %s", expense_id, exc)
        flash("Could not load the expense.", "error")
        return redirect(url_for("expenses"))

    if expense is None:
        flash("Expense not found.", "error")
        return redirect(url_for("expenses"))

    form_data = expense
    if request.method == "POST":
        form_data = _expense_form_data()
        try:
            updated = expense_service.update_expense(expense_id, form_data)
            flash(f"Expense '{updated['title']}' updated successfully!", "success")
            return redirect(url_for("expenses"))
        except ValueError as exc:
            flash(str(exc), "error")
        except Exception as exc:
            logger.error("Failed to update expense | id=%s | %s", expense_id, exc)
            flash("Something went wrong. Please try again.", "error")

    return render_template(
        "edit.html",
        page_title="Edit Expense",
        expense=expense,
        categories=expense_service.get_categories(),
        form_data=form_data,
    )


@app.route("/delete/<int:expense_id>", methods=["POST"])
def delete(expense_id: int):
    """Jalankan query DELETE melalui Service."""
    try:
        expense = expense_service.get_expense_by_id(expense_id)
        if expense is None:
            flash("Expense not found.", "error")
        elif expense_service.delete_expense(expense_id):
            flash(f"Expense '{expense['title']}' deleted successfully.", "success")
    except Exception as exc:
        logger.error("Failed to delete expense | id=%s | %s", expense_id, exc)
        flash("Could not delete the expense.", "error")
    return redirect(url_for("expenses"))


@app.route("/summary")
def summary():
    """Tampilkan query agregasi per kategori."""
    try:
        return render_template(
            "summary.html",
            page_title="Summary",
            category_totals=expense_service.get_category_totals(),
            summary=expense_service.get_summary(),
        )
    except Exception as exc:
        logger.error("Failed to load summary | %s", exc)
        flash("Could not load the summary.", "error")
        return redirect(url_for("index"))


def _expense_form_data() -> dict:
    """Ambil empat input expense dari form HTML."""
    return {
        "title": request.form.get("title", "").strip(),
        "amount": request.form.get("amount", "").strip(),
        "category": request.form.get("category", "").strip(),
        "notes": request.form.get("notes", "").strip(),
    }


@app.errorhandler(404)
def page_not_found(error):
    return render_template("errors/404.html", page_title="Page Not Found"), 404


@app.errorhandler(500)
def internal_server_error(error):
    logger.error("Unhandled server error | %s", error)
    return render_template("errors/500.html", page_title="Server Error"), 500


if __name__ == "__main__":
    app.run(debug=config.DEBUG, host="0.0.0.0", port=5000)
