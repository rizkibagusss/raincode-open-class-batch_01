"""Langkah pertama: buktikan Python dapat terhubung ke MySQL."""

from database import get_connection


db = None

try:
    db = get_connection()
    print("Connected:", db.is_connected())
finally:
    if db is not None and db.is_connected():
        db.close()

# Expected:
# Connected: True

# Eksperimen satu per satu, lalu kembalikan seperti semula:
# 1. Apa pesan error jika DB_NAME salah?
# 2. Apa pesan error jika password salah?
# 3. Apa pesan error jika MySQL Server berhenti?
