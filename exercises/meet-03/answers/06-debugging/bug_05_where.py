from database import get_connection

id_transaksi = 1
total_baru = 32000
db = get_connection()
cursor = db.cursor()
try:
    cursor.execute(
        "UPDATE transactions SET total = %s WHERE id = %s",
        (total_baru, id_transaksi),
    )
    db.commit()
    print("Row berubah:", cursor.rowcount)
finally:
    cursor.close()
    db.close()
