import logging
import os

# Set up logging configuration
def get_logger():
    level = "DEBUG" if os.getenv("DEBUG") == "1" else "WARNING"
    logging.basicConfig(level=level)
    return logging.getLogger(__name__)

logger = get_logger()