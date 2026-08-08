"""CRUD Memory — UPDATE berdasarkan ID."""

transactions = [
    {"id": 1, "nama": "Kopi Susu", "total": 25000},
    {"id": 2, "nama": "Makan Siang", "total": 35000},
]

id_target = 1
total_baru = 30000

for transaction in transactions:
    if transaction["id"] == id_target:
        # TODO: ubah total transaction menjadi total_baru.
        pass

print(transactions)

# Expected: Kopi Susu mempunyai total 30000.
# Jangan memakai transactions[0]. Kita sedang belajar mencari identity dengan ID.
