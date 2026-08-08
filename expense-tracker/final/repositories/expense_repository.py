"""
repositories/expense_repository.py - MySQL Data Access Layer
=============================================================

All SQL for the expenses table lives here. Queries use MySQL Connector/Python
parameter placeholders (%s); user values are never interpolated into SQL.
"""

from contextlib import contextmanager
from decimal import Decimal
from typing import Any, Iterator, Optional

from mysql.connector import Error

from database.db import get_connection
from utils.logger import get_logger

logger = get_logger(__name__)


@contextmanager
def _dictionary_cursor() -> Iterator[tuple[Any, Any]]:
    """Yield a connection and dictionary cursor, then close both resources."""
    connection = get_connection()
    cursor = None
    try:
        cursor = connection.cursor(dictionary=True)
        yield connection, cursor
    finally:
        try:
            if cursor is not None:
                cursor.close()
        finally:
            if connection.is_connected():
                connection.close()


class ExpenseRepository:
    """All MySQL operations for the expenses table."""

    def create_expense(
        self,
        title: str,
        amount: Decimal,
        category: str,
        notes: str,
    ) -> dict:
        sql = """
            INSERT INTO expenses (title, amount, category, notes)
            VALUES (%s, %s, %s, %s)
        """

        try:
            with _dictionary_cursor() as (connection, cursor):
                try:
                    cursor.execute(sql, (title, amount, category, notes))
                    new_id = cursor.lastrowid
                    connection.commit()
                except Error:
                    connection.rollback()
                    raise

            expense = self.get_expense_by_id(new_id)
            if expense is None:
                raise RuntimeError("Created expense could not be read back")
            return expense
        except Error as exc:
            logger.error("DB error creating expense | title=%s | %s", title, exc)
            raise

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

        order_sql = "DESC" if order.strip().lower() == "desc" else "ASC"
        conditions: list[str] = []
        params: list[Any] = []

        if search:
            conditions.append("(title LIKE %s OR notes LIKE %s)")
            params.extend([f"%{search}%", f"%{search}%"])
        if category:
            conditions.append("category = %s")
            params.append(category)

        where_clause = ("WHERE " + " AND ".join(conditions)) if conditions else ""
        sql = f"""
            SELECT id, title, amount, category, notes, created_at, updated_at
            FROM expenses
            {where_clause}
            ORDER BY {sort_by} {order_sql}
        """

        try:
            with _dictionary_cursor() as (_, cursor):
                cursor.execute(sql, tuple(params))
                return cursor.fetchall()
        except Error as exc:
            logger.error("DB error fetching expenses | search=%s | %s", search, exc)
            raise

    def get_expense_by_id(self, expense_id: int) -> Optional[dict]:
        sql = """
            SELECT id, title, amount, category, notes, created_at, updated_at
            FROM expenses
            WHERE id = %s
        """

        try:
            with _dictionary_cursor() as (_, cursor):
                cursor.execute(sql, (expense_id,))
                return cursor.fetchone()
        except Error as exc:
            logger.error("DB error fetching expense | id=%s | %s", expense_id, exc)
            raise

    def get_recent_expenses(self, limit: int = 5) -> list[dict]:
        sql = """
            SELECT id, title, amount, category, notes, created_at, updated_at
            FROM expenses
            ORDER BY created_at DESC
            LIMIT %s
        """

        try:
            with _dictionary_cursor() as (_, cursor):
                cursor.execute(sql, (int(limit),))
                return cursor.fetchall()
        except Error as exc:
            logger.error("DB error fetching recent expenses: %s", exc)
            raise

    def get_category_totals(self) -> list[dict]:
        sql = """
            SELECT
                category,
                SUM(amount) AS total_amount,
                COUNT(*) AS expense_count
            FROM expenses
            GROUP BY category
            ORDER BY total_amount DESC
        """

        try:
            with _dictionary_cursor() as (_, cursor):
                cursor.execute(sql)
                return cursor.fetchall()
        except Error as exc:
            logger.error("DB error fetching category totals: %s", exc)
            raise

    def get_total_amount(self) -> Decimal:
        sql = "SELECT COALESCE(SUM(amount), 0) AS total FROM expenses"

        try:
            with _dictionary_cursor() as (_, cursor):
                cursor.execute(sql)
                row = cursor.fetchone()
                return Decimal(str(row["total"]))
        except Error as exc:
            logger.error("DB error calculating total: %s", exc)
            raise

    def get_expense_count(self) -> int:
        sql = "SELECT COUNT(*) AS count FROM expenses"

        try:
            with _dictionary_cursor() as (_, cursor):
                cursor.execute(sql)
                row = cursor.fetchone()
                return int(row["count"])
        except Error as exc:
            logger.error("DB error counting expenses: %s", exc)
            raise

    def update_expense(
        self,
        expense_id: int,
        title: str,
        amount: Decimal,
        category: str,
        notes: str,
    ) -> Optional[dict]:
        sql = """
            UPDATE expenses
            SET title = %s, amount = %s, category = %s, notes = %s
            WHERE id = %s
        """

        try:
            with _dictionary_cursor() as (connection, cursor):
                try:
                    cursor.execute(
                        sql, (title, amount, category, notes, expense_id)
                    )
                    connection.commit()
                except Error:
                    connection.rollback()
                    raise
            return self.get_expense_by_id(expense_id)
        except Error as exc:
            logger.error("DB error updating expense | id=%s | %s", expense_id, exc)
            raise

    def delete_expense(self, expense_id: int) -> bool:
        sql = "DELETE FROM expenses WHERE id = %s"

        try:
            with _dictionary_cursor() as (connection, cursor):
                try:
                    cursor.execute(sql, (expense_id,))
                    deleted = cursor.rowcount > 0
                    connection.commit()
                    return deleted
                except Error:
                    connection.rollback()
                    raise
        except Error as exc:
            logger.error("DB error deleting expense | id=%s | %s", expense_id, exc)
            raise
