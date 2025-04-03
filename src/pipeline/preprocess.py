# ------------------------------------------------------------------------------
# preprocess.py
# ------------------------------------------------------------------------------
# This module handles data cleaning, feature engineering, and transformations.
# You might:
# - Clean missing values
# - Normalize text
# - Generate features (e.g., embeddings)
# ------------------------------------------------------------------------------

import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans and transforms the raw input data.

    Args:
        df (pd.DataFrame): Raw input dataframe.

    Returns:
        pd.DataFrame: Preprocessed dataframe.
    """
    df = df.copy()
    df.dropna(inplace=True)
    df.columns = [col.strip().lower() for col in df.columns]
    return df
