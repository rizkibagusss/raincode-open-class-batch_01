# bug_01.py
# Bug: Tipe Data Salah

# ============================================================
# MISI KAMU
# ============================================================
# Kode di bawah ini harusnya mencetak:
# "Nama: Rafi, Umur: 19 tahun"
#
# Tapi kalau dijalankan, ada error.
# Cari tahu errornya apa, lalu perbaiki.

nama = "Rafi"
umur = 19

print("Nama: " + nama + ", Umur: " + str(umur) + " tahun")

# ---- Petunjuk ----
# Baca pesan error-nya dengan teliti.
# Error apa yang muncul? Di baris berapa? ERROR CONCATENATE STRING. ERROR YANG MUNCUL DI BARIS 16
# Cek tipe data masing-masing variabel — apakah bisa digabung langsung? TIDAK BISA, HARUS DICONVERT DULU UNTUK INTEGERNYA KE STRING
