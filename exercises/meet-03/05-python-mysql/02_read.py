"""READ terlebih dahulu: query aman yang tidak mengubah data."""

from database import get_connection


db = get_connection()
cursor = db.cursor(dictionary=True)

try:
    cursor.execute(
        "SELECT id, nama, total FROM transactions ORDER BY id"
    )
    transactions = cursor.fetchall()

    print("=== DAFTAR TRANSAKSI ===")

    # TODO: loop transactions dan tampilkan id, nama, total.
    # Expected satu baris:
    # 1 | Kopi Susu | Rp25000

    print("Jumlah transaksi:", len(transactions))
finally:
    cursor.close()
    db.close()

# Pertanyaan:
# 1. Apa tipe transactions?
# 2. Apa tipe setiap item?
# 3. Mengapa cursor dibuat dengan dictionary=True?
