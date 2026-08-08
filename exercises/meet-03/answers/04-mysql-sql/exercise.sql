USE raincode_expense;

INSERT INTO transactions (nama, total) VALUES ('Kopi Susu', 25000);
INSERT INTO transactions (nama, total) VALUES ('Makan Siang', 35000);
INSERT INTO transactions (nama, total) VALUES ('Transport', 15000);

SELECT id, nama, total
FROM transactions
ORDER BY id;

SELECT id, nama, total
FROM transactions
WHERE total > 20000
ORDER BY id;

-- Ganti 1 jika ID Kopi Susu berbeda pada database lokalmu.
SELECT id, nama, total FROM transactions WHERE id = 1;
UPDATE transactions SET total = 30000 WHERE id = 1;
SELECT id, nama, total FROM transactions WHERE id = 1;

-- Ganti 3 jika ID Transport berbeda pada database lokalmu.
SELECT id, nama, total FROM transactions WHERE id = 3;
DELETE FROM transactions WHERE id = 3;
SELECT id, nama, total FROM transactions ORDER BY id;
