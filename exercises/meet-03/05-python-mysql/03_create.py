"""CREATE dari Python dan amati peran commit."""

from database import get_connection


nama = "Transport"
total = 15000

db = get_connection()
cursor = db.cursor()

try:
    cursor.execute(
        """
        INSERT INTO transactions (nama, total)
        VALUES (%s, %s)
        """,
        (nama, total),
    )

    # TODO: simpan perubahan secara permanen.
    # Hint 1: execute baru menjalankan query dalam transaction.
    # Hint 2: gunakan method commit milik connection.
    # Hint 3: db.commit()

    print("ID baru:", cursor.lastrowid)
    print("CREATE selesai. Jalankan 02_read.py untuk verifikasi.")
finally:
    cursor.close()
    db.close()

# Pertanyaan: mengapa value nama dan total dikirim terpisah melalui %s?
