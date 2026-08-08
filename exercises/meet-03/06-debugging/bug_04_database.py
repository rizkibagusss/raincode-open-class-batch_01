"""BUG 4: nama database pada konfigurasi salah."""

import os
from pathlib import Path

import mysql.connector
from dotenv import load_dotenv


load_dotenv(Path(__file__).resolve().parents[1] / ".env")

db = mysql.connector.connect(
    host=os.getenv("DB_HOST", "localhost"),
    port=int(os.getenv("DB_PORT", "3306")),
    user=os.getenv("DB_USER", "root"),
    password=os.getenv("DB_PASSWORD", ""),
    database="raincode_expenses",
)

print("Connected:", db.is_connected())
db.close()

# Gejala: Unknown database 'raincode_expenses'.
# Bagian mana yang kamu curigai?
# Hint 1: lihat nama database pada setup.sql.
# Hint 2: perhatikan huruf terakhirnya.
