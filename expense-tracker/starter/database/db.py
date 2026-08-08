"""Helper database sederhana untuk versi starter.

Service cukup mengimpor satu object:

    from database.db import db
    rows = db.execute("SELECT ...", params, fetch="all")

Object `db` dipakai bersama, tetapi koneksi MySQL fisik dibuat per operasi agar
tidak ada transaksi atau cursor yang tercampur antar-request Flask.
"""

from typing import Any, Literal, Optional

import mysql.connector
from mysql.connector import Error

from config import config
from utils.logger import get_logger

logger = get_logger(__name__)

FetchMode = Optional[Literal["one", "all"]]

_CREATE_EXPENSES_TABLE = """
CREATE TABLE IF NOT EXISTS expenses (
    id          BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    title       VARCHAR(200)    NOT NULL,
    amount      DECIMAL(15, 2)  NOT NULL,
    category    VARCHAR(100)    NOT NULL DEFAULT 'Other',
    notes       TEXT            NOT NULL,
    created_at  DATETIME        NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at  DATETIME        NOT NULL DEFAULT CURRENT_TIMESTAMP
                                            ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    INDEX idx_expenses_created_at (created_at),
    INDEX idx_expenses_category (category)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci
"""


class Database:
    """Menyediakan satu pintu untuk menjalankan seluruh query MySQL."""

    def get_connection(self):
        """Buka koneksi baru menggunakan konfigurasi dari `.env`."""
        return mysql.connector.connect(
            host=config.DB_HOST,
            port=config.DB_PORT,
            user=config.DB_USER,
            password=config.DB_PASSWORD,
            database=config.DB_NAME,
            charset=config.DB_CHARSET,
            time_zone=config.DB_TIME_ZONE,
            connection_timeout=config.DB_CONNECT_TIMEOUT,
            autocommit=False,
        )

    def execute(
        self,
        query: str,
        params: tuple | list = (),
        fetch: FetchMode = None,
    ) -> Any:
        """Jalankan satu query dan selalu bersihkan cursor serta koneksi.

        Args:
            query: SQL dengan placeholder MySQL `%s`.
            params: Value untuk placeholder, terpisah dari string SQL.
            fetch: `"one"` untuk satu dict, `"all"` untuk list[dict], atau
                `None` untuk INSERT/UPDATE/DELETE/DDL.

        Returns:
            Untuk SELECT: dict, list[dict], atau None.
            Untuk mutation: dict berisi `lastrowid` dan `rowcount`.
        """
        if fetch not in (None, "one", "all"):
            raise ValueError("fetch harus None, 'one', atau 'all'")

        connection = None
        cursor = None

        try:
            connection = self.get_connection()
            cursor = connection.cursor(dictionary=True)
            cursor.execute(query, tuple(params))

            if fetch == "one":
                return cursor.fetchone()
            if fetch == "all":
                return cursor.fetchall()

            result = {
                "lastrowid": cursor.lastrowid,
                "rowcount": cursor.rowcount,
            }
            connection.commit()
            return result
        except Error as exc:
            if connection is not None:
                connection.rollback()
            logger.error("MySQL query failed | %s", exc)
            raise
        finally:
            try:
                if cursor is not None:
                    cursor.close()
            finally:
                if connection is not None and connection.is_connected():
                    connection.close()

    def init_schema(self) -> None:
        """Buat tabel yang dibutuhkan aplikasi jika belum tersedia."""
        self.execute(_CREATE_EXPENSES_TABLE)
        logger.info(
            "Database initialized | host=%s | database=%s",
            config.DB_HOST,
            config.DB_NAME,
        )


# Satu object yang diimpor dan dipakai oleh semua Service.
db = Database()


def init_db() -> None:
    """Compatibility function yang dipanggil saat app.py melakukan startup."""
    db.init_schema()
