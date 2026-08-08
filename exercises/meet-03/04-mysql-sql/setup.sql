-- Setup awal RainCode Expense Tracker.
-- Query kerangka diberikan sebagai starter; baca setiap baris sebelum Run.

CREATE DATABASE IF NOT EXISTS raincode_expense
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

USE raincode_expense;

CREATE TABLE IF NOT EXISTS transactions (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    nama VARCHAR(100) NOT NULL,
    total DECIMAL(12, 2) NOT NULL,
    PRIMARY KEY (id)
);

-- Amati struktur table melalui panel Schemas atau jalankan:
DESCRIBE transactions;

-- Pertanyaan:
-- 1. Column mana yang menjadi identitas unik?
-- 2. Mengapa nama memakai VARCHAR?
-- 3. Mengapa total tidak memakai VARCHAR?
-- 4. Apa yang dilakukan AUTO_INCREMENT?
