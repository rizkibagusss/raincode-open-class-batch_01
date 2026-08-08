from database import get_connection

db = get_connection()
cursor = db.cursor()
try:
    cursor.execute(
        "INSERT INTO transactions (nama, total) VALUES (%s, %s)",
        ("Transport", 15000),
    )
    db.commit()
    print("ID tersimpan:", cursor.lastrowid)
finally:
    cursor.close()
    db.close()
