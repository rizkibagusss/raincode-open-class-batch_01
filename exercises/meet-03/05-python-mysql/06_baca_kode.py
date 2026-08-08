"""Jangan coding dulu. Baca alur query sampai menjadi Python object."""

from database import get_connection


db = get_connection()
cursor = db.cursor(dictionary=True)

try:
    cursor.execute(
        "SELECT nama, total FROM transactions ORDER BY id"
    )
    data = cursor.fetchall()

    for item in data:
        print(item["nama"])
finally:
    cursor.close()
    db.close()

# Jawab sebelum menjalankan:
# 1. Object apa yang mengirim query dari Python?
# 2. Siapa yang memproses SELECT?
# 3. Apa isi dan tipe data setelah fetchall()?
# 4. Bagian mana yang berasal dari materi list/dictionary?
# 5. Mengapa connection dan cursor ditutup?
