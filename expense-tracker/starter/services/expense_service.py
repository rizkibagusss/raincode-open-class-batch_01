"""Business logic dan query SQL untuk Expense Tracker versi starter.

Pada versi ini query sengaja diletakkan dekat dengan use case agar mudah dibaca:

    Route -> ExpenseService -> db.execute(query, params)

Versi `final` menunjukkan langkah berikutnya, yaitu memindahkan query-query ini
ke Repository Layer.
"""

from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
from typing import Optional

from database.db import db
from models.expense_model import EXPENSE_CATEGORIES
from utils.logger import get_logger

logger = get_logger(__name__)

MIN_AMOUNT = Decimal("0.01")
MAX_AMOUNT = Decimal("999999999.99")
MAX_TITLE_LENGTH = 200
MAX_NOTES_LENGTH = 1000


class ExpenseService:
    """Validasi input, jalankan query, lalu siapkan data untuk template."""

    def get_categories(self) -> list[str]:
        return EXPENSE_CATEGORIES

    def create_expense(self, form_data: dict) -> dict:
        data = self._validate_and_clean(form_data)

        # QUERY untuk API POST /create
        query = """
            INSERT INTO expenses (title, amount, category, notes)
            VALUES (%s, %s, %s, %s)
        """
        result = db.execute(
            query,
            (data["title"], data["amount"], data["category"], data["notes"]),
        )

        expense = self.get_expense_by_id(result["lastrowid"])
        if expense is None:
            raise RuntimeError("Expense berhasil dibuat tetapi tidak dapat dibaca ulang")

        logger.info("Expense created | id=%s", expense["id"])
        return expense

    def get_expenses(
        self,
        search: str = "",
        category: str = "",
        sort_by: str = "created_at",
        order: str = "desc",
    ) -> list[dict]:
        allowed_columns = {
            "id", "title", "amount", "category", "created_at", "updated_at"
        }
        if sort_by not in allowed_columns:
            sort_by = "created_at"
        order_sql = "DESC" if order.lower() == "desc" else "ASC"

        conditions = []
        params = []
        if search:
            conditions.append("(title LIKE %s OR notes LIKE %s)")
            params.extend([f"%{search}%", f"%{search}%"])
        if category:
            conditions.append("category = %s")
            params.append(category)

        where_sql = "WHERE " + " AND ".join(conditions) if conditions else ""

        # QUERY untuk API GET /expenses
        query = f"""
            SELECT id, title, amount, category, notes, created_at, updated_at
            FROM expenses
            {where_sql}
            ORDER BY {sort_by} {order_sql}
        """
        rows = db.execute(query, params, fetch="all")
        return [self._format_expense(row) for row in rows]

    def get_expense_by_id(self, expense_id: int) -> Optional[dict]:
        # QUERY untuk API GET/POST /edit/<id> dan POST /delete/<id>
        query = """
            SELECT id, title, amount, category, notes, created_at, updated_at
            FROM expenses
            WHERE id = %s
        """
        row = db.execute(query, (expense_id,), fetch="one")
        return self._format_expense(row) if row else None

    def get_recent_expenses(self, limit: int = 5) -> list[dict]:
        # QUERY transaksi terbaru untuk API GET /
        query = """
            SELECT id, title, amount, category, notes, created_at, updated_at
            FROM expenses
            ORDER BY created_at DESC
            LIMIT %s
        """
        rows = db.execute(query, (int(limit),), fetch="all")
        return [self._format_expense(row) for row in rows]

    def get_summary(self) -> dict:
        # QUERY statistik utama untuk API GET / dan GET /summary
        query = """
            SELECT COALESCE(SUM(amount), 0) AS total_amount,
                   COUNT(*) AS expense_count
            FROM expenses
        """
        row = db.execute(query, fetch="one")
        total = Decimal(str(row["total_amount"]))
        count = int(row["expense_count"])
        average = total / count if count else Decimal("0.00")

        return {
            "total_amount": total,
            "formatted_total": self._format_currency(total),
            "expense_count": count,
            "average_amount": self._format_currency(average),
        }

    def get_category_totals(self) -> list[dict]:
        # QUERY ringkasan kategori untuk API GET / dan GET /summary
        query = """
            SELECT category,
                   SUM(amount) AS total_amount,
                   COUNT(*) AS expense_count
            FROM expenses
            GROUP BY category
            ORDER BY total_amount DESC
        """
        rows = db.execute(query, fetch="all")
        grand_total = sum(
            (Decimal(str(row["total_amount"])) for row in rows),
            Decimal("0.00"),
        )

        result = []
        for row in rows:
            amount = Decimal(str(row["total_amount"]))
            percentage = (
                amount / grand_total * Decimal("100")
                if grand_total > 0
                else Decimal("0")
            )
            result.append({
                **row,
                "total_amount": amount,
                "formatted_amount": self._format_currency(amount),
                "percentage": float(round(percentage, 1)),
            })
        return result

    def update_expense(self, expense_id: int, form_data: dict) -> dict:
        data = self._validate_and_clean(form_data)

        # QUERY untuk API POST /edit/<id>
        query = """
            UPDATE expenses
            SET title = %s, amount = %s, category = %s, notes = %s
            WHERE id = %s
        """
        db.execute(
            query,
            (
                data["title"], data["amount"], data["category"],
                data["notes"], expense_id,
            ),
        )

        expense = self.get_expense_by_id(expense_id)
        if expense is None:
            raise ValueError("Expense tidak ditemukan.")
        logger.info("Expense updated | id=%s", expense_id)
        return expense

    def delete_expense(self, expense_id: int) -> bool:
        # QUERY untuk API POST /delete/<id>
        query = "DELETE FROM expenses WHERE id = %s"
        result = db.execute(query, (expense_id,))
        deleted = result["rowcount"] > 0
        if deleted:
            logger.info("Expense deleted | id=%s", expense_id)
        return deleted

    def _validate_and_clean(self, form_data: dict) -> dict:
        title = form_data.get("title", "").strip()
        amount_text = form_data.get("amount", "").strip()
        category = form_data.get("category", "").strip()
        notes = form_data.get("notes", "").strip()

        if not title:
            raise ValueError("Title is required.")
        if len(title) > MAX_TITLE_LENGTH:
            raise ValueError(f"Title must be {MAX_TITLE_LENGTH} characters or less.")
        if not amount_text:
            raise ValueError("Amount is required.")

        try:
            amount = Decimal(amount_text)
        except InvalidOperation:
            raise ValueError("Amount must be a valid number.")
        if not amount.is_finite():
            raise ValueError("Amount must be a finite number.")
        if amount < MIN_AMOUNT or amount > MAX_AMOUNT:
            raise ValueError(
                f"Amount must be between {MIN_AMOUNT} and {MAX_AMOUNT}."
            )
        if category not in EXPENSE_CATEGORIES:
            raise ValueError("Please select a valid category.")
        if len(notes) > MAX_NOTES_LENGTH:
            raise ValueError(f"Notes must be {MAX_NOTES_LENGTH} characters or less.")

        return {
            "title": title,
            "amount": amount.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP),
            "category": category,
            "notes": notes,
        }

    @staticmethod
    def _format_expense(expense: dict) -> dict:
        notes = expense.get("notes", "") or ""
        return {
            **expense,
            "formatted_amount": f"{expense['amount']:,.2f}",
            "short_notes": notes if len(notes) <= 60 else notes[:60] + "...",
        }

    @staticmethod
    def _format_currency(amount: Decimal) -> str:
        return f"{amount:,.2f}"
