from database import get_connection


db = get_connection()
cursor = db.cursor(dictionary=True)

try:
    cursor.execute("SELECT id, nama, total FROM transactions ORDER BY id")
    transactions = cursor.fetchall()

    print("=== DAFTAR TRANSAKSI ===")
    for transaction in transactions:
        print(f"{transaction['id']} | {transaction['nama']} | Rp{transaction['total']:.0f}")
    print("Jumlah transaksi:", len(transactions))
finally:
    cursor.close()
    db.close()
