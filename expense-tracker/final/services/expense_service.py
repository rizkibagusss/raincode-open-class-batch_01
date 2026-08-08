"""
services/expense_service.py - Business Logic Layer
====================================================

WHY THIS FILE EXISTS:
    This is the "brain" of the application. It enforces all business rules.

WHAT IS THE SERVICE LAYER?
    The service layer sits between the Route (app.py) and the Repository (database).

    REQUEST FLOW:
    ┌──────────────┐         ┌──────────────────────┐         ┌──────────────────────┐
    │  app.py      │  calls  │  ExpenseService       │  calls  │  ExpenseRepository   │
    │              │ ──────► │                      │ ──────► │                      │
    │  (routes)    │         │  - validates input   │         │  - runs SQL queries  │
    │              │ ◄────── │  - formats output    │ ◄────── │  - returns raw data  │
    └──────────────┘ returns └──────────────────────┘ returns └──────────────────────┘

WHY SEPARATE FROM ROUTE (app.py)?
    Without a service layer, app.py becomes a "fat controller" —
    one file doing everything: HTTP handling, validation, SQL, formatting.
    That becomes impossible to maintain and test.

    Service = Business Rules Layer
    Examples of business rules:
    - "Amount must be greater than 0"
    - "Category must be in our approved list"
    - "Title cannot be blank or only whitespace"
    - "Format amount as 25,000.00 for display"
    - "Calculate percentage of total for each category"

WHY SEPARATE FROM REPOSITORY?
    Service  = "Is this data valid? Should I save it?" (rules)
    Repository = "How do I save it to the database?" (SQL)

    If you change a business rule (e.g., max amount changes from 1M to 10M),
    you ONLY change this file. The SQL in repository.py stays the same.

VALIDATION PHILOSOPHY:
    Always validate server-side, even if you have JavaScript validation!
    Attackers can bypass JavaScript with browser dev tools or direct HTTP requests.
    Server-side validation is your last line of defense.
"""

from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
from typing import Optional

from models.expense_model import EXPENSE_CATEGORIES
from repositories.expense_repository import ExpenseRepository
from utils.logger import get_logger

logger = get_logger(__name__)

# ── Business Rule Constants ────────────────────────────────────────────────────
# Named constants instead of "magic numbers" scattered throughout the code.
# If the max amount policy changes, you change it in ONE place.
MIN_AMOUNT: Decimal = Decimal("0.01")
MAX_AMOUNT: Decimal = Decimal("999999999.99")
MAX_TITLE_LENGTH: int = 200
MAX_NOTES_LENGTH: int = 1000


class ExpenseService:
    """
    Handles all business logic for expense management.

    Responsibilities:
    - Input validation (raises ValueError with user-friendly messages)
    - Data formatting (currency, truncation, percentages)
    - Orchestrating calls to the repository
    - Logging significant events

    The service never writes SQL directly.
    The service never handles HTTP requests directly.
    """

    def __init__(self) -> None:
        # The service depends on the repository for data access
        # More advanced patterns use "Dependency Injection" here,
        # but direct instantiation is fine for learning purposes.
        self.repository = ExpenseRepository()

    # ── Categories ─────────────────────────────────────────────────────────────

    def get_categories(self) -> list[str]:
        """
        Return the list of valid expense categories.

        Why define this in the service instead of the template?
        Because templates should not contain business rules.
        The service decides what categories are valid.

        Returns:
            list[str]: Available category names
        """
        return EXPENSE_CATEGORIES

    # ── CREATE ─────────────────────────────────────────────────────────────────

    def create_expense(self, form_data: dict) -> dict:
        """
        Validate form data and create a new expense.

        Process:
            1. Validate and clean all inputs
            2. Pass cleaned data to repository for saving
            3. Log the successful creation
            4. Return the created expense with formatted fields

        Args:
            form_data: Raw dictionary from the HTML form
                Keys: 'title', 'amount', 'category', 'notes'

        Returns:
            dict: The created expense with id, timestamps, and formatted fields

        Raises:
            ValueError: If any validation rule fails (user error)
            mysql.connector.Error: If the database operation fails (system error)
        """
        cleaned = self._validate_and_clean(form_data)

        expense = self.repository.create_expense(
            title=cleaned["title"],
            amount=cleaned["amount"],
            category=cleaned["category"],
            notes=cleaned["notes"],
        )

        logger.info(
            f"Expense created successfully | "
            f"expense_id={expense['id']} "
            f"category={expense['category']} "
            f"amount={expense['amount']}"
        )

        return self._format_expense(expense)

    # ── READ ───────────────────────────────────────────────────────────────────

    def get_expenses(
        self,
        search: str = "",
        category: str = "",
        sort_by: str = "created_at",
        order: str = "desc",
    ) -> list[dict]:
        """
        Retrieve and format expenses with optional filtering and sorting.

        Args:
            search:   Text to search in title and notes
            category: Filter by exact category name
            sort_by:  Column to sort by ('created_at', 'amount', 'title', etc.)
            order:    Sort direction ('asc' or 'desc')

        Returns:
            list[dict]: Formatted expense dictionaries ready for template rendering
        """
        raw_expenses = self.repository.get_expenses(
            search=search,
            category=category,
            sort_by=sort_by,
            order=order,
        )
        return [self._format_expense(e) for e in raw_expenses]

    def get_expense_by_id(self, expense_id: int) -> Optional[dict]:
        """
        Get a single expense by ID.

        Args:
            expense_id: The expense's unique database ID

        Returns:
            dict: Formatted expense if found
            None: If the expense doesn't exist
        """
        expense = self.repository.get_expense_by_id(expense_id)
        if expense:
            return self._format_expense(expense)
        return None

    def get_recent_expenses(self, limit: int = 5) -> list[dict]:
        """
        Get the most recent N expenses for the dashboard.

        Args:
            limit: Maximum number of expenses to return

        Returns:
            list[dict]: Most recent expenses, newest first
        """
        expenses = self.repository.get_recent_expenses(limit=limit)
        return [self._format_expense(e) for e in expenses]

    def get_summary(self) -> dict:
        """
        Calculate overall spending statistics for the dashboard.

        Returns a dict with:
        - total_amount:     Raw Decimal (e.g. Decimal("250000.50"))
        - formatted_total:  Display string (e.g. "250,000.50")
        - expense_count:    Total number of records
        - average_amount:   Formatted average per expense

        Returns:
            dict: Summary statistics
        """
        total = self.repository.get_total_amount()
        count = self.repository.get_expense_count()
        average = total / count if count > 0 else Decimal("0.00")

        return {
            "total_amount": total,
            "formatted_total": self._format_currency(total),
            "expense_count": count,
            "average_amount": self._format_currency(average),
        }

    def get_category_totals(self) -> list[dict]:
        """
        Get spending totals per category, with calculated percentages.

        WHY CALCULATE PERCENTAGE HERE AND NOT IN THE TEMPLATE?
        Templates should only display data, not calculate it.
        This keeps templates simple and the logic testable.

        Returns:
            list[dict]: Each category with amount, count, and percentage of total
        """
        category_data = self.repository.get_category_totals()
        grand_total = sum(row["total_amount"] for row in category_data)

        result = []
        for row in category_data:
            amount = row["total_amount"]
            percentage = (
                amount / grand_total * Decimal("100")
                if grand_total > 0
                else Decimal("0.0")
            )

            result.append({
                "category":        row["category"],
                "total_amount":    amount,
                "formatted_amount": self._format_currency(amount),
                "expense_count":   row["expense_count"],
                "percentage":      round(percentage, 1),
            })

        return result

    # ── UPDATE ─────────────────────────────────────────────────────────────────

    def update_expense(self, expense_id: int, form_data: dict) -> dict:
        """
        Validate and update an existing expense.

        Args:
            expense_id: ID of the expense to update
            form_data:  New data from the edit form

        Returns:
            dict: The updated expense with formatted fields

        Raises:
            ValueError: If validation fails
        """
        cleaned = self._validate_and_clean(form_data)

        expense = self.repository.update_expense(
            expense_id=expense_id,
            title=cleaned["title"],
            amount=cleaned["amount"],
            category=cleaned["category"],
            notes=cleaned["notes"],
        )

        logger.info(
            f"Expense updated successfully | "
            f"expense_id={expense_id} "
            f"category={expense['category']} "
            f"amount={expense['amount']}"
        )

        return self._format_expense(expense)

    # ── DELETE ─────────────────────────────────────────────────────────────────

    def delete_expense(self, expense_id: int) -> bool:
        """
        Delete an expense permanently.

        Args:
            expense_id: ID of the expense to delete

        Returns:
            True:  Expense was found and deleted
            False: Expense was not found
        """
        deleted = self.repository.delete_expense(expense_id)

        if deleted:
            logger.info(f"Expense deleted successfully | expense_id={expense_id}")
        else:
            logger.warning(f"Delete attempted on non-existent expense | expense_id={expense_id}")

        return deleted

    # ── Private Helpers ────────────────────────────────────────────────────────
    # Methods prefixed with _ are internal (private by convention in Python).
    # They are called by other methods in THIS class only.

    def _validate_and_clean(self, form_data: dict) -> dict:
        """
        Validate form data and return a cleaned, safe version.

        WHY SERVER-SIDE VALIDATION?
        JavaScript validation (client-side) can be bypassed by:
        - Disabling JavaScript in the browser
        - Using developer tools to modify the form
        - Sending HTTP requests directly (curl, Postman)

        Server-side validation is the authoritative source of truth.
        Always validate on the server, even with frontend validation.

        Args:
            form_data: Raw form data dictionary

        Returns:
            dict: Cleaned and validated data

        Raises:
            ValueError: With a user-friendly error message if invalid
        """
        title    = form_data.get("title", "").strip()
        amount_s = form_data.get("amount", "").strip()
        category = form_data.get("category", "").strip()
        notes    = form_data.get("notes", "").strip()

        # ── Title ──────────────────────────────────────────────────────────────
        if not title:
            raise ValueError("Title is required.")

        if len(title) > MAX_TITLE_LENGTH:
            raise ValueError(f"Title must be {MAX_TITLE_LENGTH} characters or less.")

        # ── Amount ─────────────────────────────────────────────────────────────
        if not amount_s:
            raise ValueError("Amount is required.")

        try:
            amount = Decimal(amount_s)
        except InvalidOperation:
            raise ValueError("Amount must be a valid number (e.g. 25000 or 25000.50).")

        if not amount.is_finite():
            raise ValueError("Amount must be a finite number.")

        if amount < MIN_AMOUNT:
            raise ValueError(f"Amount must be at least {self._format_currency(MIN_AMOUNT)}.")

        if amount > MAX_AMOUNT:
            raise ValueError(f"Amount cannot exceed {self._format_currency(MAX_AMOUNT)}.")

        # ── Category ───────────────────────────────────────────────────────────
        if not category:
            raise ValueError("Please select a category.")

        if category not in EXPENSE_CATEGORIES:
            raise ValueError(
                f"'{category}' is not a valid category. "
                f"Choose from: {', '.join(EXPENSE_CATEGORIES)}"
            )

        # ── Notes ──────────────────────────────────────────────────────────────
        if len(notes) > MAX_NOTES_LENGTH:
            raise ValueError(f"Notes must be {MAX_NOTES_LENGTH} characters or less.")

        return {
            "title":    title,
            "amount":   amount.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP),
            "category": category,
            "notes":    notes,
        }

    def _format_expense(self, expense: dict) -> dict:
        """
        Enrich a raw expense dict with display-ready computed fields.

        WHY ADD FORMATTED FIELDS HERE?
        Templates should be as simple as possible.
        Instead of writing complex Jinja2 filters in templates,
        we pre-format everything here so templates just print variables.

        Added fields:
        - formatted_amount: "25,000.50" (for display)
        - short_notes:      Truncated notes for table view

        Args:
            expense: Raw expense dict from the repository

        Returns:
            dict: Expense with additional formatted fields
        """
        return {
            **expense,                  # Spread operator: keep all original fields
            "formatted_amount": self._format_currency(expense["amount"]),
            "short_notes": self._truncate(expense.get("notes", ""), max_length=60),
        }

    def _format_currency(self, amount: Decimal) -> str:
        """
        Format a Decimal as a currency string with thousand separators.

        Examples:
            25000    → "25,000.00"
            1234567  → "1,234,567.00"
            0.5      → "0.50"

        Args:
            amount: Numeric amount to format

        Returns:
            str: Formatted currency string (no currency symbol — international friendly)
        """
        return f"{amount:,.2f}"

    def _truncate(self, text: str, max_length: int) -> str:
        """
        Truncate text to max_length characters, adding "..." if cut.

        Used for the notes preview in the expenses table so long notes
        don't break the table layout.

        Args:
            text:       The text to potentially truncate
            max_length: Maximum allowed character count

        Returns:
            str: Original text if short enough, or truncated + "..." version
        """
        if len(text) <= max_length:
            return text
        return text[:max_length].rstrip() + "..."
