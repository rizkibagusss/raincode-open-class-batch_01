from database import get_connection


id_transaksi = 3

db = get_connection()
cursor = db.cursor()

try:
    query = "DELETE FROM transactions WHERE id = %s"
    params = (id_transaksi,)
    cursor.execute(query, params)
    db.commit()
    print("Row terhapus:", cursor.rowcount)
finally:
    cursor.close()
    db.close()
