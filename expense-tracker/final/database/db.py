"""
database/db.py - MySQL Connection & Initialization
===================================================

This module is the only place that knows how to connect to MySQL. Repository
classes request connections through get_connection(), while the rest of the
application remains independent of the database driver.

The database itself and its application user must already exist. init_db()
creates the expenses table and indexes when the Flask application starts.
"""

import mysql.connector
from mysql.connector import Error
from mysql.connector.connection import MySQLConnection

from config import config
from utils.logger import get_logger

logger = get_logger(__name__)

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


def get_connection() -> MySQLConnection:
    """Open and return a configured MySQL connection."""
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


def init_db() -> None:
    """Create the expenses table when it does not already exist."""
    connection = None
    cursor = None

    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(_CREATE_EXPENSES_TABLE)
        connection.commit()
        logger.info(
            "Database initialized | host=%s | database=%s",
            config.DB_HOST,
            config.DB_NAME,
        )
    except Error as exc:
        if connection is not None:
            connection.rollback()
        logger.critical("Database initialization failed: %s", exc)
        raise
    finally:
        try:
            if cursor is not None:
                cursor.close()
        finally:
            if connection is not None and connection.is_connected():
                connection.close()
