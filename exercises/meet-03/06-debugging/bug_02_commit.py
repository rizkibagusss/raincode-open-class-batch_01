"""BUG 2: INSERT berjalan tetapi data tidak bertahan."""

from database import get_connection


db = get_connection()
cursor = db.cursor()

try:
    cursor.execute(
        "INSERT INTO transactions (nama, total) VALUES (%s, %s)",
        ("Transport", 15000),
    )
    print("Query dijalankan. ID sementara:", cursor.lastrowid)
finally:
    cursor.close()
    db.close()

# Gejala: setelah program selesai, 05-python-mysql/02_read.py tidak
# menampilkan row baru.
# Bagian mana yang kamu curigai?
# Hint 1: mutation hidup di dalam database transaction.
# Hint 2: apa yang membuat perubahan menjadi permanen?
