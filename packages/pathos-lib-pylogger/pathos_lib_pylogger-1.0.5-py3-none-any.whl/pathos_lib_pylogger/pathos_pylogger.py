import logging
import json
import socket
from datetime import datetime
from pathlib import Path
from logging.handlers import TimedRotatingFileHandler
import os

class JsonFormatter(logging.Formatter):
    def format(self, record):
        log_entry = {
            "container_id": socket.gethostname(),
            "file": f"{Path(record.pathname).as_posix()}:{record.lineno}",
            "level": record.levelname.lower(),
            "msg": record.getMessage(),
            "time": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
        }
        return json.dumps(log_entry)

def get_logger(
    name="custom_logger",
    level=logging.INFO,
    log_dir="logs",
    file_name="app.log",
    console_logging=True,
    file_logging=True,
    backup_count=7,
):
    """
    Get a pre-configured logger.

    :param name: Name of the logger.
    :param level: Logging level.
    :param log_dir: Directory to store log files.
    :param console_logging: Whether to log to console.
    :param file_logging: Whether to log to a file.
    :param backup_count: Number of rotated log files to retain.
    :return: Configured logger instance.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Prevent duplicate handlers
    if logger.hasHandlers():
        logger.handlers.clear()

    # Create logs directory if it doesn't exist
    if file_logging:
        log_dir_path = Path(log_dir)
        log_dir_path.mkdir(exist_ok=True)

    # Console Handler
    if console_logging:
        console_handler = logging.StreamHandler()
        console_handler.setLevel(level)
        console_handler.setFormatter(JsonFormatter())
        logger.addHandler(console_handler)

    # File Handler with daily rotation
    if file_logging:
        file_handler = TimedRotatingFileHandler(
            filename=log_dir_path / file_name,
            when="midnight",
            interval=1,
            backupCount=backup_count,
            encoding="utf-8",
        )
        file_handler.setLevel(level)
        file_handler.setFormatter(JsonFormatter())

        # Set log files to compress after rotation
        file_handler.namer = lambda name: name + ".zip"
        file_handler.rotator = lambda source, dest: os.rename(source, dest)

        logger.addHandler(file_handler)

    return logger
