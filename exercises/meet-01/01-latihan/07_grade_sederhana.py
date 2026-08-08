# 07_grade_sederhana.py
# Topik: if / elif / else — Penentuan Grade Nilai

# ============================================================
# TUGAS
# ============================================================
# Buat program penentu grade berdasarkan nilai ujian.
#
# Aturan gradenya:
#   >= 90        → "A"
#   >= 80        → "B"
#   >= 70        → "C"
#   >= 60        → "D"
#   di bawah 60  → "E"
#
# Nilai sudah disediakan di bawah. Kamu tinggal tulis
# logika if / elif / else-nya.

nilai = 12

# Tulis kode kamu di sini:

if nilai >= 90:
    print("A, Sempurna!")
elif nilai >= 80:
    print ("B")
elif nilai >= 70:
    print("C")
elif nilai >= 60:
    print("D")
else:
    print("E,Ayo belajar lagi!")


# Output yang diharapkan (untuk nilai = 82):
# Grade: B


# ============================================================
# BONUS (opsional)
# ============================================================
# Setelah berhasil, coba tambahkan:
# - Kalau grade A, cetak juga "Sempurna!"
# - Kalau grade E, cetak juga "Ayo belajar lagi!"
