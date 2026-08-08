# 06_if_else.py
# Topik: Percabangan (if / else)

# ============================================================
# BAGIAN 1 — Baca dan tebak output
# ============================================================
# Jangan langsung dijalankan. Baca dulu pelan-pelan,
# telusuri alurnya, baru tulis jawabanmu.

tiket = 50000
ada_diskon = True

if ada_diskon:
    bayar = tiket * 0.8
else:
    bayar = tiket

print("Bayar:", bayar)   # tebak: Bayar 40000.0

# Pertanyaan:
# - Kenapa blok "else" tidak dijalankan? JADI, BLOK ELSE TIDAK DIJALANKAN KARENA KONDISI IF NYA SUDAH TERPENUHI (TRUE)
# - Coba ubah ada_diskon = False, kira-kira hasilnya apa? BERARTI HASIL TEBAKAN PRINT MENJADI "50000"


# ============================================================
# BAGIAN 2 — Lengkapi kondisinya
# ============================================================
# Program ini mau ngecek apakah seseorang boleh masuk bioskop.
# Syaratnya: umur minimal 13 tahun.
# Lengkapi bagian yang rumpang.

umur = 15

if umur >= 13:                          # tulis kondisi yang benar di sini
    print("Boleh masuk.")
else:
    print("Maaf, belum boleh masuk.")

# Hint: pakai operator perbandingan yang sudah kamu pelajari


# ============================================================
# BAGIAN 3 — Tulis sendiri
# ============================================================
# Buat program sederhana:
# - Simpan angka berapa saja ke variabel "suhu"
# - Kalau suhu di atas 30, cetak "Panas banget!"
# - Kalau tidak, cetak "Masih oke."

# Tulis kode kamu di sini:

suhu = 33

if suhu > 30:
    print("Panas banget")
else:
    print("Masih oke")


