"""CRUD Memory — DELETE berdasarkan ID."""

transactions = [
    {"id": 1, "nama": "Kopi Susu", "total": 30000},
    {"id": 2, "nama": "Makan Siang", "total": 35000},
    {"id": 3, "nama": "Transport", "total": 15000},
]

id_target = 2

# TODO: buat list baru yang hanya berisi transaksi selain id_target.
# transactions = [
#     transaction
#     for transaction in transactions
#     if ______________________________
# ]

print(transactions)

# Expected: hanya ID 1 dan ID 3 yang tersisa.
# Hint 1: pertahankan item yang ID-nya tidak sama dengan target.
# Hint 2: gunakan operator !=.
