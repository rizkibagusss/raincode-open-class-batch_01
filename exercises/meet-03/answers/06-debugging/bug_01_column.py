from database import get_connection

db = get_connection()
cursor = db.cursor(dictionary=True)
try:
    cursor.execute("SELECT id, nama, total FROM transactions ORDER BY id")
    print(cursor.fetchall())
finally:
    cursor.close()
    db.close()
