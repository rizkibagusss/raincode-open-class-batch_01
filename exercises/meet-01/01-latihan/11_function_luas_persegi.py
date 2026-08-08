# 11_function_luas_persegi.py
# Topik: Fungsi dengan Kalkulasi & Return Value

# ============================================================
# TUGAS 1 — Luas Persegi
# ============================================================
# Buat fungsi bernama "luas_persegi" yang:
# - Menerima satu parameter: sisi
# - Mengembalikan hasil sisi * sisi

# Tulis fungsinya di sini:

def luas_persegi(sisi):
    luas = sisi * sisi
    return (f"Luas persegi adalah {luas}")


# Setelah selesai, uji dengan beberapa nilai:
# print(luas_persegi(4))   # harusnya: 16
# print(luas_persegi(7))   # harusnya: 49
# print(luas_persegi(10))  # harusnya: 100

print(luas_persegi(4))
print(luas_persegi(7))
print(luas_persegi(10))

# ============================================================
# TUGAS 2 — Keliling Persegi
# ============================================================
# Buat fungsi bernama "keliling_persegi" yang:
# - Menerima satu parameter: sisi
# - Mengembalikan hasil 4 * sisi

# Tulis fungsinya di sini:

def keliling_persegi(sisi):
    keliling = 4 * sisi
    return (f"Keliling Persegi adalah {keliling}")

# Uji:
# print(keliling_persegi(5))   # harusnya: 20
# print(keliling_persegi(3))   # harusnya: 12
print(keliling_persegi(5))
print(keliling_persegi(3))




# ============================================================
# TUGAS 3 — Gabungkan keduanya
# ============================================================
# Gunakan kedua fungsi yang sudah kamu buat untuk mencetak:
# "Persegi dengan sisi 6: luas = 36, keliling = 24"
#
# Hint: pakai f-string atau concatenation

sisi = 6

# Tulis kode kamu di sini:
print(f"Persegi dengan sisi {sisi}: {luas_persegi(sisi)}, {keliling_persegi(sisi)}")