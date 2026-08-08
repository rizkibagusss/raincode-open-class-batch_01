"""
utils/logger.py - Application Logging System
=============================================

WHY DO COMPANIES USE LOGS?

    Imagine your app is running in production at 3 AM.
    A customer calls: "The app is broken!"

    Without logs:  You have NO idea what happened. You're blind.
    With logs:     You open app.log and read exactly what happened, step by step.
                   "2024-01-15 03:42:11 | ERROR | services.expense | Database timeout"

    Logs are your application's "flight recorder" — like the black box on a plane.
    Airlines study the flight recorder after a crash to understand what went wrong.
    Developers study logs after an incident to understand and fix the problem.

LOG LEVELS (from least severe to most severe):

    Level       When to Use                         Example
    ─────────── ─────────────────────────────────── ──────────────────────────────────
    DEBUG       Very detailed, dev only             "Executing SQL: SELECT * FROM..."
    INFO        Normal operations                   "Expense created: id=15, amt=25000"
    WARNING     Unexpected, but app still works     "Invalid amount entered by user"
    ERROR       Something failed, app continues     "Database write failed, retrying..."
    CRITICAL    App is about to crash               "Cannot connect to database at all"

REAL-WORLD LOG EXAMPLES:
    INFO  | Expense created successfully | expense_id=15 category=Food amount=25000
    WARN  | Invalid amount entered | amount=-500 | user_ip=192.168.1.1
    ERROR | Database connection failed | host=127.0.0.1 database=expense_tracker
    INFO  | Application started | env=production | version=1.0.0

HOW TO USE THIS IN OTHER FILES:
    from utils.logger import get_logger
    logger = get_logger(__name__)

    logger.info("Expense created successfully")
    logger.warning("Invalid amount entered")
    logger.error(f"Database error: {error}")
"""

import logging
import os
from config import config


def setup_logger() -> None:
    """
    Configure the root logger once at application startup.

    Creates two "handlers" (output destinations):
    1. Console handler → you see logs in your terminal
    2. File handler   → logs are saved to logs/app.log permanently

    WHY TWO HANDLERS?
    - During development: you see logs instantly in the terminal
    - In production: logs are stored in files for later analysis
    - Log management tools (Datadog, Splunk) read from files
    """

    # Ensure the logs/ directory exists before creating the log file
    log_dir = os.path.dirname(config.LOG_FILE)
    if log_dir and not os.path.exists(log_dir):
        os.makedirs(log_dir, exist_ok=True)

    # Convert "INFO" string → logging.INFO integer (Python requires the number)
    numeric_level = getattr(logging, config.LOG_LEVEL.upper(), logging.INFO)

    # ── Log Format ─────────────────────────────────────────────────────────────
    # What each log line looks like:
    # 2024-01-15 14:30:25 | INFO     | services.expense_service  | Expense created
    log_format = (
        "%(asctime)s | %(levelname)-8s | %(name)-32s | %(message)s"
    )
    date_format = "%Y-%m-%d %H:%M:%S"
    formatter = logging.Formatter(fmt=log_format, datefmt=date_format)

    # ── Root Logger ────────────────────────────────────────────────────────────
    # The root logger is the "parent" — all other loggers inherit from it
    root_logger = logging.getLogger()
    root_logger.setLevel(numeric_level)

    # Avoid adding duplicate handlers if setup_logger() is called twice
    if root_logger.handlers:
        return

    # ── Console Handler ────────────────────────────────────────────────────────
    # Prints logs to your terminal (stdout)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(numeric_level)
    console_handler.setFormatter(formatter)
    root_logger.addHandler(console_handler)

    # ── File Handler ───────────────────────────────────────────────────────────
    # Writes logs to logs/app.log
    # mode='a' = "append" mode → never overwrites existing logs
    # encoding='utf-8' → supports all characters (important for internationalization)
    file_handler = logging.FileHandler(
        filename=config.LOG_FILE,
        mode="a",
        encoding="utf-8",
    )
    file_handler.setLevel(numeric_level)
    file_handler.setFormatter(formatter)
    root_logger.addHandler(file_handler)

    # ── Silence Noisy Libraries ────────────────────────────────────────────────
    # Flask's internal server (werkzeug) logs every HTTP request by default.
    # We reduce that noise so our own logs are easier to read.
    logging.getLogger("werkzeug").setLevel(logging.WARNING)


def get_logger(name: str) -> logging.Logger:
    """
    Get a named logger for a specific module.

    WHY NAMED LOGGERS?
    Named loggers include the module name in the log output, so you instantly
    know WHERE in the code a log message came from:

        2024-01-15 14:30:25 | INFO | services.expense_service | Expense created

    USAGE — always put this at the top of each Python file:
        from utils.logger import get_logger
        logger = get_logger(__name__)

    __name__ is Python's built-in variable that holds the current module's name.
    In services/expense_service.py, __name__ = "services.expense_service"

    Args:
        name: Module name (always pass __name__ for automatic naming)

    Returns:
        logging.Logger: A configured logger ready to use
    """
    return logging.getLogger(name)


# ── Auto-setup ─────────────────────────────────────────────────────────────────
# This runs automatically when any file does: from utils.logger import get_logger
# So logging is configured before the first log message is written.
setup_logger()
