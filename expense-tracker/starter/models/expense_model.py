"""
models/expense_model.py - The Expense Data Model
==================================================

WHY THIS FILE EXISTS:
    Defines the "shape" of an Expense — what fields it has and what types they are.
    This is the core data entity of our application.

WHAT IS A MODEL?
    A model is a Python class that mirrors a database table.
    Every row in the `expenses` table becomes an Expense object.

    Database Table (expenses):          Python Object (Expense):
    ┌─────────────────────────┐         ┌──────────────────────────┐
    │ id       INTEGER        │   →     │ expense.id   : int       │
    │ title    TEXT           │   →     │ expense.title: str       │
    │ amount   DECIMAL(15,2)  │   →     │ expense.amount: Decimal  │
    │ category TEXT           │   →     │ expense.category: str    │
    │ notes    TEXT           │   →     │ expense.notes: str       │
    │ created_at TEXT         │   →     │ expense.created_at: str  │
    │ updated_at TEXT         │   →     │ expense.updated_at: str  │
    └─────────────────────────┘         └──────────────────────────┘

WHY @dataclass?
    Python's @dataclass decorator automatically writes repetitive code for us:
    - __init__() → so we can do Expense(title="Coffee", amount=25000)
    - __repr__() → so print(expense) shows something useful
    - No boilerplate needed!

INDUSTRY NOTE:
    In larger projects you might use SQLAlchemy ORM (Object Relational Mapper).
    We use a simple dataclass here to keep things transparent and teach
    you how SQL works without magic happening behind the scenes.
"""

from dataclasses import dataclass
from decimal import Decimal
from typing import Optional


# ── Category Constants ──────────────────────────────────────────────────────────
# Defined here so every part of the app uses the SAME list.
# If you add a new category, you only change it in ONE place.
EXPENSE_CATEGORIES: list[str] = [
    "Food",
    "Transportation",
    "Shopping",
    "Bills",
    "Entertainment",
    "Education",
    "Other",
]

# Maps each category to a color for the UI
# Used in templates and JavaScript for consistent styling
CATEGORY_COLORS: dict[str, str] = {
    "Food":           "#f97316",   # Orange
    "Transportation": "#3b82f6",   # Blue
    "Shopping":       "#ec4899",   # Pink
    "Bills":          "#ef4444",   # Red
    "Entertainment":  "#8b5cf6",   # Purple
    "Education":      "#06b6d4",   # Cyan
    "Other":          "#6b7280",   # Gray
}


@dataclass
class Expense:
    """
    Represents a single expense record.

    This is the central data object that flows through all layers:
    Database → Service → Route → Template

    Attributes:
        id:         Auto-assigned by the database (None before saving)
        title:      Short name like "Morning Coffee" or "Bus Ticket"
        amount:     Cost in decimal (e.g. 25000.00)
        category:   One of EXPENSE_CATEGORIES
        notes:      Optional extra details
        created_at: Timestamp when first created (set by DB)
        updated_at: Timestamp of last edit (set by DB)
    """

    id: Optional[int] = None
    title: str = ""
    amount: Decimal = Decimal("0.00")
    category: str = "Other"
    notes: str = ""
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

    def to_dict(self) -> dict:
        """
        Convert this Expense object to a plain dictionary.

        Why?
        Flask's render_template() works best with dictionaries.
        JSON APIs also expect dictionaries, not custom objects.

        Returns:
            dict: All fields as a plain Python dictionary
        """
        return {
            "id": self.id,
            "title": self.title,
            "amount": self.amount,
            "category": self.category,
            "notes": self.notes,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Expense":
        """
        Create an Expense object from a dictionary.

        Used when we receive data from the database.
        (The MySQL dictionary cursor returns dicts, not Expense objects)

        Args:
            data: Dictionary with expense fields

        Returns:
            Expense: A new Expense instance
        """
        return cls(
            id=data.get("id"),
            title=data.get("title", ""),
            amount=Decimal(str(data.get("amount", "0.00"))),
            category=data.get("category", "Other"),
            notes=data.get("notes", ""),
            created_at=data.get("created_at"),
            updated_at=data.get("updated_at"),
        )
