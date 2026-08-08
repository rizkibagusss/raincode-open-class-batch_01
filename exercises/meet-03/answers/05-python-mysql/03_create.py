from database import get_connection


nama = "Transport"
total = 15000

db = get_connection()
cursor = db.cursor()

try:
    cursor.execute(
        "INSERT INTO transactions (nama, total) VALUES (%s, %s)",
        (nama, total),
    )
    db.commit()
    print("ID baru:", cursor.lastrowid)
finally:
    cursor.close()
    db.close()
