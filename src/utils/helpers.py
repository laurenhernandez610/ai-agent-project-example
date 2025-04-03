# ------------------------------------------------------------------------------
# helpers.py
# ------------------------------------------------------------------------------
# Shared utility functions that don't fit neatly into other modules.
# This is where logging setup, time formatting, or general-purpose tools go.
# ------------------------------------------------------------------------------

import logging
from datetime import datetime

# ------------------------------------------------------------------------------
# LOGGER SETUP
# ------------------------------------------------------------------------------

logging.basicConfig(
    filename="logs/run.log",
    filemode="a",
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=logging.INFO
)

logger = logging.getLogger(__name__)

# ------------------------------------------------------------------------------
# GENERAL UTILITIES
# ------------------------------------------------------------------------------

def timestamp_now() -> str:
    """Returns current timestamp in readable format."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def print_banner(text: str):
    """Prints a banner for CLI output clarity."""
    print("\n" + "="*50)
    print(f"{text}")
    print("="*50 + "\n")
