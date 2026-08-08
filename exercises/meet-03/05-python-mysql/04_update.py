"""UPDATE berdasarkan ID menggunakan parameter query."""

from database import get_connection


id_transaksi = 1
total_baru = 32000

db = get_connection()
cursor = db.cursor()

try:
    cursor.execute(
        """
        UPDATE transactions
        SET total = %s
        WHERE id = %s
        """,
        (_____, _____),  # TODO: isi sesuai urutan %s pada query
    )
    db.commit()

    print("Row berubah:", cursor.rowcount)
finally:
    cursor.close()
    db.close()

# Expected jika ID 1 tersedia:
# Row berubah: 1
# Setelah itu, 02_read.py menampilkan Kopi Susu | Rp32000.
