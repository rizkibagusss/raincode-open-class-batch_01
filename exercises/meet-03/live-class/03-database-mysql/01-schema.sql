-- Kerangka database dibuat saat setup, bukan pada setiap request pengguna.
CREATE DATABASE IF NOT EXISTS raincode_expense
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

USE raincode_expense;

CREATE TABLE IF NOT EXISTS transactions (
    id              BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    nama            VARCHAR(100)    NOT NULL,
    total           DECIMAL(15, 2)  NOT NULL,
    created_at      DATETIME        NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at      DATETIME        NOT NULL DEFAULT CURRENT_TIMESTAMP
                                            ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    CONSTRAINT chk_transactions_total_non_negative CHECK (total >= 0)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
