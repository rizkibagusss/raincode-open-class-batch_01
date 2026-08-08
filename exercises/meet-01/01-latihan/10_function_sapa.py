# 10_function_sapa.py
# Topik: Fungsi — Definisi & Pemanggilan

# ============================================================
# BAGIAN 1 — Baca dulu contohnya
# ============================================================
# Ini contoh fungsi yang sudah jadi. Jalankan dan amati.

def sapa_formal(nama):
    return "Selamat datang, " + nama + "!"

pesan = sapa_formal("Budi")
print(pesan)

# Perhatikan:
# - "def" = mendefinisikan fungsi
# - "nama" = parameter (kotak kosong yang diisi saat dipanggil)
# - "return" = nilai yang dikembalikan fungsi


# ============================================================
# BAGIAN 2 — Tugas
# ============================================================
# Buat fungsi bernama "sapa" yang:
# - Menerima satu parameter: nama
# - Mengembalikan string: "Halo, <nama>! Apa kabar?"
#
# Setelah selesai, panggil fungsinya dengan tiga nama berbeda
# dan cetak hasilnya.

# Tulis fungsinya di sini:

def sapa(nama, kota):
    return (f"Halo, {nama}! Apa Kabar?\nHalo, {nama} dari {kota}")


# Panggil fungsinya di sini (contoh):
# print(sapa("Andi"))
# print(sapa("Sari"))
# print(sapa("Dika"))

print(sapa("Andi", "Malang"))
print(sapa("Sari","Yogyakarta"))
print(sapa("Dika", "Tangerang"))


# ============================================================
# BONUS (opsional)
# ============================================================
# Modifikasi fungsi "sapa" agar bisa menerima dua parameter:
# nama dan kota, lalu hasilkan:
# "Halo, <nama> dari <kota>!"
