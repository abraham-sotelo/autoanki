import logging
import os

# Set up logging configuration
def get_logger():
    level = os.getenv("DEBUG", "WARNING").upper()
    logging.basicConfig(level=level)
    return logging.getLogger(__name__)

logger = get_logger()