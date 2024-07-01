import logging
import os
from logging.handlers import RotatingFileHandler

# Set log level from environment variable or default to INFO
log_level = os.getenv('LOG_LEVEL', 'INFO').upper()

# Configure logging
logging.basicConfig(
    level=log_level,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler("log.txt", maxBytes=1000000, backupCount=5),
        logging.StreamHandler(),
    ],
)

# Set specific log levels for certain libraries
logging.getLogger("httpx").setLevel(logging.ERROR)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("pytgcalls").setLevel(logging.ERROR)

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
