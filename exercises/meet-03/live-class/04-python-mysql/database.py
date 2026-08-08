"""Satu pintu untuk menjalankan query MySQL sebelum memakai Flask."""

import os
from typing import Any, Literal, Optional

import mysql.connector
from dotenv import load_dotenv
from mysql.connector import Error

load_dotenv()

FetchMode = Optional[Literal["one", "all"]]


class Database:
    def get_connection(self):
        return mysql.connector.connect(
            host=os.getenv("DB_HOST", "127.0.0.1"),
            port=int(os.getenv("DB_PORT", "3306")),
            user=os.getenv("DB_USER", "expense_app"),
            password=os.getenv("DB_PASSWORD", ""),
            database=os.getenv("DB_NAME", "raincode_expense"),
            time_zone=os.getenv("DB_TIME_ZONE", "+07:00"),
            charset="utf8mb4",
            connection_timeout=10,
            autocommit=False,
        )

    def execute(
        self,
        query: str,
        params: tuple | list = (),
        fetch: FetchMode = None,
    ) -> Any:
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

            result = {"lastrowid": cursor.lastrowid, "rowcount": cursor.rowcount}
            connection.commit()
            return result
        except Error:
            if connection is not None:
                connection.rollback()
            raise
        finally:
            try:
                if cursor is not None:
                    cursor.close()
            finally:
                if connection is not None and connection.is_connected():
                    connection.close()


db = Database()
