# bug_04.py
# Bug: Logika Grade Bertingkat Salah

# ============================================================
# MISI KAMU
# ============================================================
# Program penentu grade di bawah ini punya bug logika.
# Untuk nilai = 85, harusnya muncul "B".
# Tapi coba jalankan — apakah hasilnya benar?
#
# Kalau tidak, cari di mana logikanya salah.

nilai = 85

if nilai >= 90:
    grade = "A"
elif nilai >= 80:
    grade = "B"
elif nilai >= 70:
    grade = "C"
elif nilai >= 60:
    grade = "D"
else:
    grade = "E"

print("Grade:", grade)

# ---- Petunjuk ----
# Python mengevaluasi kondisi if/elif dari atas ke bawah.
# Begitu satu kondisi True, yang lain dilewati.
# Coba tanya diri sendiri: nilai 85 >= 60 itu True atau False? HARUSNYA TRUE
# Terus apa yang terjadi setelah kondisi pertama True? DIA PRINT GRADE D KARENA MEMANG DI PYTHON KALAU BARIS PERTAMA SUDAH MEMENUHI MAKA ITU HASILNYA
