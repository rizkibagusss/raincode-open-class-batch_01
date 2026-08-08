USE raincode_expense;

-- ============================================================
-- CHALLENGE 1 — CREATE DATA
-- ============================================================
-- Tambahkan tiga row berikut:
-- Kopi Susu   | 25000
-- Makan Siang | 35000
-- Transport   | 15000
--
-- Hint 1: CREATE data memakai INSERT INTO.
-- Hint 2: sebutkan column nama dan total.
-- Hint 3: INSERT INTO transactions (nama, total) VALUES (..., ...);

-- TODO: tulis tiga INSERT di bawah komentar ini.


-- ============================================================
-- CHALLENGE 2 — READ SEMUA DATA
-- ============================================================
-- Tampilkan id, nama, dan total dari seluruh transactions.
-- Expected: tiga row yang baru ditambahkan.

-- TODO: tulis SELECT.


-- ============================================================
-- CHALLENGE 3 — READ DENGAN KONDISI
-- ============================================================
-- Prediksi dahulu: data mana yang totalnya lebih dari 20000?
-- Setelah menulis prediksi, tampilkan data tersebut dengan WHERE.

-- TODO: SELECT ... WHERE total > ...


-- ============================================================
-- CHALLENGE 4 — UPDATE
-- ============================================================
-- Ubah total Kopi Susu dari 25000 menjadi 30000 berdasarkan ID.
-- Jalankan SELECT lebih dahulu untuk memastikan ID target.

-- TODO: SELECT target.
-- TODO: UPDATE transactions SET ... WHERE id = ...;
-- TODO: SELECT kembali untuk verifikasi.


-- ============================================================
-- CHALLENGE 5 — DELETE
-- ============================================================
-- Hapus Transport berdasarkan ID.
-- Jangan menjalankan DELETE sebelum SELECT dengan WHERE yang sama
-- menunjukkan tepat satu target.

-- TODO: SELECT target.
-- TODO: DELETE FROM transactions WHERE id = ...;
-- TODO: SELECT seluruh data untuk verifikasi.


-- CHECKPOINT:
-- [ ] INSERT menambah row.
-- [ ] SELECT membaca row.
-- [ ] UPDATE hanya mengubah satu ID.
-- [ ] DELETE hanya menghapus satu ID.
-- [ ] Semua perubahan dibuktikan dengan SELECT.
