"""BUG 1: query memakai nama column yang tidak ada."""

from database import get_connection


db = get_connection()
cursor = db.cursor(dictionary=True)

try:
    cursor.execute(
        "SELECT id, nama, nominal FROM transactions ORDER BY id"
    )
    print(cursor.fetchall())
finally:
    cursor.close()
    db.close()

# Gejala: Unknown column 'nominal'.
# Misi: tampilkan id, nama, dan total.
# Bagian mana yang kamu curigai?
# Hint 1: buka kembali 04-mysql-sql/setup.sql.
# Hint 2: bandingkan nama column huruf demi huruf.
