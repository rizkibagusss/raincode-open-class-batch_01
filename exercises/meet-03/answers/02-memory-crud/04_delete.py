transactions = [
    {"id": 1, "nama": "Kopi Susu", "total": 30000},
    {"id": 2, "nama": "Makan Siang", "total": 35000},
    {"id": 3, "nama": "Transport", "total": 15000},
]

id_target = 2
transactions = [
    transaction
    for transaction in transactions
    if transaction["id"] != id_target
]

print(transactions)
