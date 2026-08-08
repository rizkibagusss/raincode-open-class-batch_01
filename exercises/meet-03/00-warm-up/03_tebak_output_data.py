"""Enam soal tebak output data. Tulis prediksi sebelum Run."""

transactions = [
    {"id": 1, "nama": "Kopi Susu", "total": 25000},
    {"id": 2, "nama": "Makan Siang", "total": 35000},
]

# SOAL 1
print(len(transactions))  # tebak: ...

# SOAL 2
print(transactions[0]["nama"])  # tebak: ...

# SOAL 3
print(transactions[1]["total"] > 30000)  # tebak: ...

# SOAL 4
total_semua = 0
for transaction in transactions:
    total_semua += transaction["total"]
print(total_semua)  # tebak: ...

# SOAL 5
transactions.append({"id": 3, "nama": "Transport", "total": 15000})
print(len(transactions))  # tebak: ...

# SOAL 6
transactions[0]["total"] = 30000
print(transactions[0])  # tebak: ...

# Expected: program menghasilkan enam baris tanpa error.
# Nilai lengkap tersedia di answers setelah kamu menjalankan dan membandingkan.
