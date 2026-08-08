"""Business rule dan query untuk setiap operation API."""

from datetime import datetime
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP

from database import db


class TransactionService:
    def get_all(self) -> list[dict]:
        # READ — dipanggil GET /api/transactions
        query = """
            SELECT id, nama, total, created_at, updated_at
            FROM transactions
            ORDER BY id DESC
        """
        return [self._json_ready(row) for row in db.execute(query, fetch="all")]

    def get_by_id(self, transaction_id: int) -> dict | None:
        query = """
            SELECT id, nama, total, created_at, updated_at
            FROM transactions
            WHERE id = %s
        """
        row = db.execute(query, (transaction_id,), fetch="one")
        return self._json_ready(row) if row else None

    def create(self, payload: dict) -> dict:
        data = self._validate(payload)
        # CREATE — dipanggil POST /api/transactions
        query = """
            INSERT INTO transactions (nama, total)
            VALUES (%s, %s)
        """
        result = db.execute(query, (data["nama"], data["total"]))
        return self.get_by_id(result["lastrowid"])

    def update(self, transaction_id: int, payload: dict) -> dict | None:
        data = self._validate(payload)
        # UPDATE — dipanggil PATCH /api/transactions/<id>
        query = """
            UPDATE transactions
            SET nama = %s, total = %s
            WHERE id = %s
        """
        result = db.execute(
            query,
            (data["nama"], data["total"], transaction_id),
        )
        return self.get_by_id(transaction_id) if result["rowcount"] else None

    def delete(self, transaction_id: int) -> bool:
        # DELETE — dipanggil DELETE /api/transactions/<id>
        query = "DELETE FROM transactions WHERE id = %s"
        return db.execute(query, (transaction_id,))["rowcount"] > 0

    @staticmethod
    def _validate(payload: dict) -> dict:
        nama = str(payload.get("nama", "")).strip()
        if not nama or len(nama) > 100:
            raise ValueError("Nama wajib diisi dan maksimal 100 karakter.")
        try:
            total = Decimal(str(payload.get("total", "")))
        except InvalidOperation:
            raise ValueError("Total belanja harus berupa angka.")
        if not total.is_finite() or total < 0:
            raise ValueError("Total belanja harus angka non-negatif.")
        return {
            "nama": nama,
            "total": total.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP),
        }

    @staticmethod
    def _json_ready(row: dict) -> dict:
        return {
            **row,
            "total": float(row["total"]),
            "created_at": row["created_at"].isoformat() if isinstance(row["created_at"], datetime) else row["created_at"],
            "updated_at": row["updated_at"].isoformat() if isinstance(row["updated_at"], datetime) else row["updated_at"],
        }
