from database import get_connection

db = get_connection()
try:
    print("Connected:", db.is_connected())
finally:
    db.close()
