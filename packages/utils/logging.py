import logging
import sys
from typing import Optional


def initiate_logger(
    name: str = __name__,
    level: int = logging.INFO,
    log_to_console: bool = True,
    log_to_file: Optional[str] = None,
    fmt: str = "[%(asctime)s] [%(levelname)s] %(name)s: %(message)s",
    datefmt: str = "%Y-%m-%d %H:%M:%S",
) -> logging.Logger:
    """
    Initialize and return a logger with optional console and file output.

    Args:
        name (str): Name of the logger (usually __name__).
        level (int): Logging level (e.g., logging.INFO, logging.DEBUG).
        log_to_console (bool): Whether to log to console (stdout).
        log_to_file (str or None): If set, logs will also be written to file.
        fmt (str): Log format string.
        datefmt (str): Format for timestamps.

    Returns:
        logging.Logger: Configured logger instance.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.propagate = False  # Prevent duplicate logs if root logger is configured

    formatter = logging.Formatter(fmt=fmt, datefmt=datefmt)

    if log_to_console:
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    if log_to_file:
        file_handler = logging.FileHandler(log_to_file)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger
