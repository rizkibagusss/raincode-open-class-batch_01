USE raincode_expense;

SELECT * FROM transactions;

INSERT INTO transactions (nama, total)
VALUES ('Kopi Susu', 25000);

SELECT id, nama, total
FROM transactions
ORDER BY id;
