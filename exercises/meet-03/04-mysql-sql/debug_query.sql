USE raincode_expense;

-- File ini SENGAJA berisi query rusak.
-- Jangan menjalankan seluruh file sekaligus. Perbaiki satu challenge,
-- sorot query tersebut, lalu jalankan selection saja.

-- BUG 1 — gejala: syntax error dekat FROM.
-- Misi: tampilkan seluruh transaksi.
SELEC * FROM transactions;

-- BUG 2 — gejala: Unknown column 'nominal'.
-- Misi: tambahkan Kopi Susu Rp25000.
INSERT INTO transactions (nama, nominal)
VALUES ('Kopi Susu', 25000);

-- Pertanyaan untuk setiap bug:
-- 1. Kata atau nama mana yang kamu curigai?
-- 2. Apa bukti dari pesan error?
-- 3. Apa perubahan minimum yang diperlukan?
-- 4. Query verifikasi apa yang akan kamu jalankan?
