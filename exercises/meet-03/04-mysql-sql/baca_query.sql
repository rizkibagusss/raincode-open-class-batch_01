USE raincode_expense;

-- JANGAN RUN DULU. BACA DAN PREDIKSI.
SELECT nama, total
FROM transactions
WHERE total > 20000;

-- Jawab sebelum menjalankan:
-- 1. Table mana yang dibaca?
-- 2. Column apa yang akan ditampilkan?
-- 3. Row mana yang lolos kondisi?
-- 4. Apakah Transport Rp15000 akan muncul? Mengapa?
--
-- Prediksi output:
-- ______________________________

-- Setelah menjawab, jalankan query dan bandingkan dengan prediksimu.

-- MODIFIKASI:
-- 1. Ubah kondisi menjadi total >= 30000.
-- 2. Ubah SELECT agar hanya menampilkan nama.
-- 3. Tambahkan ORDER BY total DESC, lalu amati urutannya.
