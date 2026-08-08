transactions = [
    {"id": 1, "nama": "Kopi Susu", "total": 25000},
    {"id": 2, "nama": "Makan Siang", "total": 35000},
]

id_target = 1
total_baru = 30000

for transaction in transactions:
    if transaction["id"] == id_target:
        transaction["total"] = total_baru
        break

print(transactions)
