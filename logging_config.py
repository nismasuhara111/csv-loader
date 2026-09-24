import logging
import json
from datetime import datetime


class JSONFormatter(logging.Formatter):
    """Formats log records as JSON."""

    def format(self, record):
        log_data = {
            "timestamp": datetime.now().isoformat(),
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
        }

        if record.exc_info:
            log_data["exception"] = self.formatException(record.exc_info)

        return json.dumps(log_data)


def setup_logging(log_file="pipeline.log"):
    """Configure centralized application logging."""

    logger = logging.getLogger("pipeline")
    logger.setLevel(logging.INFO)

    # Prevent duplicate handlers
    if logger.handlers:
        logger.handlers.clear()

    formatter = JSONFormatter()

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    file_handler = logging.FileHandler(log_file, mode="a", encoding="utf-8")
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger