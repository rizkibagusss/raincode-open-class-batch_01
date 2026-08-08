"""DELETE satu transaksi berdasarkan ID."""

from database import get_connection


id_transaksi = 3

db = get_connection()
cursor = db.cursor()

try:
    # TODO 1: isi query DELETE yang mempunyai WHERE id = %s.
    query = _____

    # TODO 2: kirim id_transaksi sebagai tuple satu item.
    params = _____

    cursor.execute(query, params)
    db.commit()

    print("Row terhapus:", cursor.rowcount)
finally:
    cursor.close()
    db.close()

# Hint 1: DELETE FROM transactions WHERE id = %s
# Hint 2: tuple satu item memerlukan koma.
# Hint 3: (id_transaksi,)
