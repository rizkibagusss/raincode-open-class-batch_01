transactions = [
    {"id": 1, "nama": "Kopi Susu", "total": 25000},
    {"id": 2, "nama": "Makan Siang", "total": 35000},
    {"id": 3, "nama": "Transport", "total": 15000},
]

print("=== DAFTAR TRANSAKSI ===")
for transaction in transactions:
    print(f"{transaction['id']} | {transaction['nama']} | Rp{transaction['total']}")

print("Jumlah transaksi:", len(transactions))
