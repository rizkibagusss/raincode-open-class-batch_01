# 09_baca_kode_02.py
# Topik: Baca Kode — Ada Fungsi & Kondisi

# ============================================================
# CARA MAIN
# ============================================================
# Kali ini ada fungsi. Telusuri dari bawah (dari pemanggilan)
# ke atas (ke definisi fungsinya), bukan sebaliknya.
# Jawab semua pertanyaan sebelum menjalankan kode.

# ---- Kodenya ----

def cek_kelulusan(nilai, kehadiran):
    if kehadiran < 75:
        return "Tidak Lulus — kehadiran kurang"
    if nilai >= 60:
        return "Lulus"
    else:
        return "Tidak Lulus — nilai kurang"


hasil1 = cek_kelulusan(70, 80)
hasil2 = cek_kelulusan(55, 90)
hasil3 = cek_kelulusan(80, 60)

print(hasil1)   # pertanyaan 1: LULUS
print(hasil2)   # pertanyaan 2: TIDAK LULUS - NILAI KURAMG
print(hasil3)   # pertanyaan 3: TIDAK LULUS - KEHADIRAN KURANG

# ---- Pertanyaan ----
# 1. Apa yang dicetak untuk hasil1? Kenapa?
#    Jawab: LULUS, KARENA BARIS KEDUA KETIKA PENGECEKAN NILAI MEMENUHI
#
# 2. Apa yang dicetak untuk hasil2? Kenapa?
#    Jawab: TIDAK LULUS - NILAI KURANG, KARENA BARIS KETIGA KETIKA PENGECEKAN MEMENUHI
#
# 3. Apa yang dicetak untuk hasil3? Kenapa?
#    Jawab: TIDAK LULUS - KEHADIRAN KURANG, SAAT PENGECEKAN GARIS PERTAMA ANGKA MEMENUHI SYARAT TERSEBUT.
#
# 4. Kondisi mana yang dicek lebih dulu — kehadiran atau nilai?
#    Kenapa urutan itu penting?
#    Jawab: URUTAN INI PENTING KARENA RETURN LANGSUNG MENGHENTIKAN FUNGSI. BAYANGKAN KALAU NILAI >= 60 DITARUH PALING ATAS. UNTUK MURID DI HASIL3 (NILAI 80, TAPI KEHADIRAN CUMA 60), PROGRAM AKAN MELIHAT NILAI 80, LANGSUNG ME-RETURN "LULUS", DAN BERHENTI SAAT ITU JUGA. PROGRAM TIDAK AKAN SADAR KALAU MURID ITU SERING BOLOS! ITULAH KENAPA SYARAT KEHADIRAN YANG KETAT HARUS DITARUH PALING ATAS SEBAGAI "PENYARING" PERTAMA.
