USE raincode_expense;

-- CREATE: sebelum query belum ada Kopi Susu; sesudahnya ada satu row baru.
INSERT INTO transactions (nama, total)
VALUES ('Kopi Susu', 25000.00);

-- READ: mengambil column yang memang dibutuhkan tampilan.
SELECT id, nama, total, created_at
FROM transactions
ORDER BY id DESC;

-- READ satu target. Ganti 1 dengan ID yang benar dari hasil SELECT.
SELECT id, nama, total
FROM transactions
WHERE id = 1;

-- UPDATE: SET adalah nilai baru; WHERE memilih row target.
UPDATE transactions
SET total = 28000.00
WHERE id = 1;

-- Verifikasi perubahan, jangan hanya percaya pesan “query berhasil”.
SELECT id, nama, total
FROM transactions
WHERE id = 1;

-- DELETE: hapus tepat satu target. Jangan hilangkan WHERE.
DELETE FROM transactions
WHERE id = 1;

-- Verifikasi row sudah tidak ada.
SELECT id, nama, total
FROM transactions
ORDER BY id DESC;
