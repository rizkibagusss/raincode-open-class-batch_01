"""Membaca, menambah, dan mengubah value dictionary."""

transaction = {
    "nama": "Kopi Susu",
    "total": 25000,
}

# Jangan jalankan dulu. Prediksi output kedua baris ini.
print(transaction["nama"])   # tebak: ...
print(transaction["total"])  # tebak: ...

# TODO 1: tambahkan kategori dengan value "Makanan".
# transaction[_____] = _____

# TODO 2: ubah total menjadi 30000.
# transaction[_____] = _____

print(transaction)

# Expected akhir:
# {'nama': 'Kopi Susu', 'total': 30000, 'kategori': 'Makanan'}
