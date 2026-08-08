"""Empat operation CRUD dengan query terlihat tepat di dekat use case."""

from decimal import Decimal, InvalidOperation

from database import db


def create(nama: str, total: Decimal) -> int:
    query = """
        INSERT INTO transactions (nama, total)
        VALUES (%s, %s)
    """
    result = db.execute(query, (nama, total))
    return result["lastrowid"]


def read_all() -> list[dict]:
    query = """
        SELECT id, nama, total, created_at
        FROM transactions
        ORDER BY id DESC
    """
    return db.execute(query, fetch="all")


def update_total(id_transaksi: int, total_baru: Decimal) -> bool:
    query = """
        UPDATE transactions
        SET total = %s
        WHERE id = %s
    """
    result = db.execute(query, (total_baru, id_transaksi))
    return result["rowcount"] > 0


def delete(id_transaksi: int) -> bool:
    query = "DELETE FROM transactions WHERE id = %s"
    result = db.execute(query, (id_transaksi,))
    return result["rowcount"] > 0


def print_rows(rows: list[dict]) -> None:
    print("\nID | Nama                 | Total")
    print("---+----------------------+---------------")
    for row in rows:
        print(f"{row['id']:>2} | {row['nama']:<20} | Rp {row['total']:>10,.2f}")


if __name__ == "__main__":
    nama = input("Nama transaksi (contoh: Kopi Susu): ").strip()
    try:
        total = Decimal(input("Total belanja: ").strip())
    except InvalidOperation:
        raise SystemExit("Total belanja harus berupa angka.")

    if not nama or total < 0:
        raise SystemExit("Nama wajib diisi dan total tidak boleh negatif.")

    new_id = create(nama, total)
    print(f"CREATE berhasil, ID baru: {new_id}")
    print_rows(read_all())

    if input("Update total row baru? (y/n): ").lower() == "y":
        total_baru = Decimal(input("Total baru: ").strip())
        print("UPDATE:", "berhasil" if update_total(new_id, total_baru) else "tidak ditemukan")
        print_rows(read_all())

    if input("Delete row baru? (y/n): ").lower() == "y":
        print("DELETE:", "berhasil" if delete(new_id) else "tidak ditemukan")
        print_rows(read_all())
