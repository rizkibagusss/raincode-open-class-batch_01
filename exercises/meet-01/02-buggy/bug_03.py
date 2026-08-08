# bug_03.py
# Bug: Fungsi Tidak Mengembalikan Nilai

# ============================================================
# MISI KAMU
# ============================================================
# Fungsi "hitung_diskon" harusnya mengembalikan harga setelah diskon.
# Tapi hasilnya selalu "None". Ada yang kurang — cari dan perbaiki.

def hitung_diskon(harga, persen_diskon):
    diskon = harga * (persen_diskon / 100)
    harga_akhir = harga - diskon
    # seharusnya ada sesuatu di sini...
    return harga_akhir


harga_sepatu = 200000
harga_bayar = hitung_diskon(harga_sepatu, 20)

print("Harga setelah diskon:", harga_bayar)

# Output yang seharusnya:
# Harga setelah diskon: 160000.0

# ---- Petunjuk ----
# Fungsi sudah menghitung harga_akhir dengan benar.
# Tapi nilainya tidak keluar dari fungsi.
# Apa kata kunci yang diperlukan untuk mengembalikan nilai? KATA KUNCI NYA ADALAH RETURN
