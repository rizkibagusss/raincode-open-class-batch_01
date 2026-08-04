# 04_tipe_data.py
# Topik: Tipe Data — int, float, str, bool

# ============================================================
# BAGIAN 1 — Tebak tipe datanya
# ============================================================
# Sebelum dijalankan, tebak tipe data apa yang akan muncul.
# Pilihan: <class 'int'>, <class 'float'>, <class 'str'>, <class 'bool'>

print("========= BAGIAN 1 - TEBAK TIPE DATANYA ==========")

nama      = "Sari"
umur      = 21
tinggi    = 160.5
mahasiswa = True

print(type(nama))        # tebak: STRING
print(type(umur))        # tebak: INTEGER
print(type(tinggi))      # tebak: FLOAT
print(type(mahasiswa))   # tebak: BOOLEAN

# Pertanyaan:
# - Kenapa 160.5 bukan int? KARENA MENGANDUNG KOMA DIBELAKANG ANGKA 0
# - Kenapa "21" berbeda dengan 21 di Python? KARENA "21" DIANGGAP STRING KARENA ADA TANDA "", SEMENTARA 21 ITU MURNI INTEGER


# ============================================================
# BAGIAN 2 — Jebakan tipe data
# ============================================================
# Tebak tipe data dari variabel-variabel ini.
# Hati-hati, beberapa tidak sesederhana kelihatannya.

print("========= BAGIAN 2 - JEBAKAN TIPE DATA ==========")

a = "100"       # tebak: STRING
b = 100         # tebak: INTEGER
c = 100.0       # tebak: FLOAT
d = True        # tebak: BOOLEAN
e = "True"      # tebak: STRING
f = 3 + 2       # tebak: INTEGER
g = 3 + 2.0     # tebak: FLOAT

print(type(a), type(b), type(c))
print(type(d), type(e))
print(type(f), type(g))

# Pertanyaan:
# - Apakah a dan b bisa dijumlahkan langsung? Kenapa? TIDAK BISA, KARENA HARUS SAMA TYPE DATANYA
# - Apa perbedaan d dan e? D ITU BOOLEAN, E ITU STRING
# - Kenapa g berbeda dengan f padahal angkanya hampir sama? KARENA G INTEGER + FLOAT, SEHINGGA HASIL AKHIR FLOAT. KALAU F ITU MURNI INTEGER + INTEGER


# ============================================================
# BAGIAN 3 — Isi yang benar
# ============================================================
# Ganti None dengan nilai yang sesuai tipe datanya.
# Jangan pakai tipe data yang salah!

print("========= BAGIAN 3 - ISI YANG BENAR ==========")


# Butuh integer (angka tahun):
tahun_lahir = 2000   # ganti dengan angka tahun lahirmu

# Butuh float (nilai IPK):
ipk = 3.65           # ganti dengan angka desimal, contoh: 3.75

# Butuh string (nama kota):
kota = "Jakarta"         # ganti dengan nama kotamu dalam tanda kutip

# Butuh boolean (apakah sudah makan siang?):
sudah_makan = True   # ganti dengan True atau False

print(tahun_lahir, ipk, kota, sudah_makan)
