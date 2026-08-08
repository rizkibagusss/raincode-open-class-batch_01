"""BUG 5: UPDATE tidak menunjuk ID yang diminta task."""

from database import get_connection


id_transaksi = 1
total_baru = 32000

db = get_connection()
cursor = db.cursor()

try:
    cursor.execute(
        "UPDATE transactions SET total = %s WHERE id = %s",
        (total_baru, 999),
    )
    db.commit()
    print("Row berubah:", cursor.rowcount)
finally:
    cursor.close()
    db.close()

# Gejala: output Row berubah: 0, padahal task meminta update ID 1.
# Bagian mana yang kamu curigai?
# Hint 1: cocokkan urutan params dengan urutan %s.
# Hint 2: variable id_transaksi sudah tersedia tetapi belum dipakai.
