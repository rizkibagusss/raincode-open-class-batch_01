transactions = [
    {"nama": "Kopi Susu", "total": 25000},
    {"nama": "Makan Siang", "total": 35000},
]

print(transactions[0])
print(transactions[1]["nama"])

transactions.append({"nama": "Transport", "total": 15000})

for transaction in transactions:
    print(f"{transaction['nama']} | Rp{transaction['total']}")
