# 05_boolean.py
# Topik: Boolean & Operator Perbandingan

# ============================================================
# BAGIAN 1 — Tebak dulu, baru jalankan
# ============================================================
# Aturannya: tulis tebakan kamu di bagian "???"
# baru setelah itu jalankan untuk ngecek.
#
# Ingat: hasil boolean cuma dua pilihan — True atau False

print("=============== BAGIAN 1 - TEBAK DULU, BARU JALANKAN ====================")
umur = 17

print(umur >= 18)        # tebak: FALSE
print(umur == 17)        # tebak: TRUE
print(umur != 20)        # tebak: TRUE
print(not (umur >= 18))  # tebak: TRUE

# Coba jawab dulu sebelum jalankan:
# - Kenapa baris pertama hasilnya False? KARENA 17 LEBIH KECIL DARI 18.
# - Apa perbedaan == dengan >=? KALAU == MENCARI VALUE DAN TYPE DATA YANG SAMA, KALAU >= MENCARI YANG LEBIH BESAR TAPI VALUENYA BOLEH SAMA
# - Apa yang dilakukan "not" terhadap hasil boolean? MERUBAH HASIL DARI BOOLEAN


# ============================================================
# BAGIAN 2 — Lengkapi kodenya
# ============================================================
# Ganti setiap None dengan ekspresi boolean yang benar.
# Kalau output-nya masih None, berarti belum kamu ganti.

print("======================= BAGIAN 2 - LENGKAPI KODENYA ====================")
nilai = 75

# Apakah nilai lebih besar atau sama dengan 60?
lulus = True         # ganti ini

# Apakah nilai kurang dari 75?
butuh_remedial = False  # ganti ini

print("Lulus:", lulus)
print("Perlu remedial:", butuh_remedial)

# Output yang seharusnya muncul:
# Lulus: True
# Perlu remedial: False
