import logging
import os
from typing import Dict
from colorama import Fore, Style, init

init(autoreset=True)

class LoggerManager:
    def __init__(self, config: Dict):
        """Initialize LoggerManager with the path to the default log directory."""
        self.config = config

        # Set default values for logging configuration if not found
        self.log_level = self._get_log_level(self.config.get("log_level"))
        self.log_path = os.path.abspath(os.path.expanduser(self.config.get("log_path")))
        self.log_file = self.config.get("log_file")

    def _get_log_level(self, level: str) -> int:
        """Convert log level string to logging level constant."""
        log_levels = {
            "INFO": logging.INFO,
            "WARNING": logging.WARNING,
            "ERROR": logging.ERROR,
            "FATAL": logging.FATAL,
            "DEBUG": logging.DEBUG,
        }
        # Default to FATAL if an invalid level is specified
        return log_levels.get(level.upper())

    def configure_logging(self) -> None:
        """Configure logging based on provided configuration."""
        # Ensure the log path exists
        os.makedirs(self.log_path, exist_ok=True)

        log_file_path = os.path.join(self.log_path, self.log_file)

        # Setup the file handler for logging
        file_handler = logging.FileHandler(log_file_path, mode="a")
        file_handler.setLevel(self.log_level)
        file_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        file_handler.setFormatter(file_formatter)

        # Setup the stream handler for console logging with colors
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(self.log_level)
        stream_handler.setFormatter(self._get_colored_formatter())

        logger = logging.getLogger()
        logger.setLevel(self.log_level)

        # Remove any existing handlers
        logger.handlers = []

        # Add both file and stream handlers
        logger.addHandler(file_handler)
        logger.addHandler(stream_handler)

        logging.info(f"Logging configured with FileHandler at {log_file_path}")

    def _get_colored_formatter(self) -> logging.Formatter:
        """Create a formatter that adds color to log messages."""
        class ColoredFormatter(logging.Formatter):
            COLORS = {
                logging.DEBUG: Fore.BLUE,
                logging.INFO: Fore.GREEN,
                logging.WARNING: Fore.YELLOW,
                logging.ERROR: Fore.RED,
                logging.CRITICAL: f"{Fore.RED}{Style.BRIGHT}",
            }

            def format(self, record):
                color = self.COLORS.get(record.levelno, "")
                message = super().format(record)
                return f"{color}{message}{Style.RESET_ALL}"

        return ColoredFormatter("%(asctime)s - %(levelname)s - %(message)s")