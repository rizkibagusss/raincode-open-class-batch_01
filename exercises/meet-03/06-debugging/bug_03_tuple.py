"""BUG 3: parameter satu item bukan tuple."""

from database import get_connection


id_transaksi = 1
db = get_connection()
cursor = db.cursor(dictionary=True)

try:
    cursor.execute(
        "SELECT id, nama, total FROM transactions WHERE id = %s",
        (id_transaksi),
    )
    print(cursor.fetchone())
finally:
    cursor.close()
    db.close()

# Gejala: connector menolak atau salah membaca params.
# Bagian mana yang kamu curigai?
# Hint 1: tanda kurung saja belum selalu menghasilkan tuple.
# Hint 2: bandingkan (1) dengan (1,).
