from database import get_connection

id_transaksi = 1
db = get_connection()
cursor = db.cursor(dictionary=True)
try:
    cursor.execute(
        "SELECT id, nama, total FROM transactions WHERE id = %s",
        (id_transaksi,),
    )
    print(cursor.fetchone())
finally:
    cursor.close()
    db.close()
