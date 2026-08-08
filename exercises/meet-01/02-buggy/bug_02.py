# bug_02.py
# Bug: Kondisi Terbalik

# ============================================================
# MISI KAMU
# ============================================================
# Program ini harusnya:
# - Cetak "Selamat, kamu lulus!" kalau nilai >= 60
# - Cetak "Coba lagi ya." kalau nilai < 60
#
# Tapi outputnya selalu salah. Cari dan perbaiki bugnya.

nilai = 75

if nilai < 60:
    print("Selamat, kamu lulus!")
else:
    print("Coba lagi ya.")

# ---- Petunjuk ----
# Jalankan dulu, perhatikan outputnya.
# Apakah kondisi di "if" sudah benar? BELUM
# Coba tracing manual: nilai = 75, kondisi nilai < 60 itu True atau False? FALSE

# YANG BENAR

nilai = 75

if nilai >= 60:
    print("Selamat, kamu lulus!")
else:
    print("Coba lagi ya.")
