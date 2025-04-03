# ------------------------------------------------------------------------------
# ingest.py
# ------------------------------------------------------------------------------
# This module handles data ingestion — loading datasets from local files,
# cloud storage, databases, APIs, or external tools.
#
# It's the first step in your AI system and should be modular and extensible.
# ------------------------------------------------------------------------------

import pandas as pd
from src.utils.helpers import logger

def load_data(path: str = "data/raw/sample.csv") -> pd.DataFrame:
    """
    Loads data from a CSV or other source into a DataFrame.

    Args:
        path (str): Path to the data file.

    Returns:
        pd.DataFrame: Loaded dataset.
    """
    logger.info(f"Loading data from {path}")
    try:
        df = pd.read_csv(path)
        logger.info(f"Data loaded successfully: {df.shape[0]} rows")
        return df
    except FileNotFoundError:
        logger.error("File not found.")
        return pd.DataFrame()
