"""Gabungkan empat CRUD operation terhadap data di memory."""

transactions = [
    {"id": 1, "nama": "Kopi Susu", "total": 25000},
    {"id": 2, "nama": "Makan Siang", "total": 35000},
]


def tambah_transaksi(transaction_id, nama, total):
    # TODO: append dictionary baru.
    pass


def lihat_transaksi():
    # TODO: loop dan print semua transaksi.
    pass


def ubah_total(transaction_id, total_baru):
    # TODO: cari ID, ubah total, lalu return True.
    # Return False jika ID tidak ditemukan.
    pass


def hapus_transaksi(transaction_id):
    # TODO: hapus target dan return True.
    # Return False jika ID tidak ditemukan.
    pass


tambah_transaksi(3, "Transport", 15000)
ubah_total(1, 30000)
hapus_transaksi(2)
lihat_transaksi()

# Expected:
# 1 | Kopi Susu | Rp30000
# 3 | Transport | Rp15000

# AHA MOMENT:
# Hentikan program, jalankan lagi, dan perhatikan kondisi awalnya.
# Mengapa perubahan sebelumnya tidak bertahan?
