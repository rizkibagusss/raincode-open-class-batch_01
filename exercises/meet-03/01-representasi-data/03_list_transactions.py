"""Menyimpan banyak transaksi sebagai list of dictionaries."""

transactions = [
    {"nama": "Kopi Susu", "total": 25000},
    {"nama": "Makan Siang", "total": 35000},
]

# TODO 1: tampilkan seluruh dictionary transaksi pertama.
# print(_____)

# TODO 2: tampilkan hanya nama transaksi kedua.
# print(_____)

# TODO 3: tambahkan Transport Rp15000 menggunakan append().
# transactions.append({_____})

# TODO 4: loop semua transaksi dan tampilkan nama serta total.
for transaction in transactions:
    print(f"{_____} | Rp{_____}")

# Expected akhir:
# Kopi Susu | Rp25000
# Makan Siang | Rp35000
# Transport | Rp15000

# Pertanyaan:
# - Apa tipe variable transactions?
# - Apa tipe setiap item di dalam transactions?
