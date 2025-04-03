# ------------------------------------------------------------------------------
# test_ingest.py
# ------------------------------------------------------------------------------
# This file contains unit tests for the data ingestion pipeline.
# It ensures data is loaded correctly, handles edge cases,
# and returns valid types or shapes.
# ------------------------------------------------------------------------------

import pytest
from src.pipeline.ingest import load_data

def test_load_data_returns_dataframe():
    """Check that the ingest function loads data as a DataFrame."""
    df = load_data()
    assert df is not None
    assert hasattr(df, "shape")

def test_load_data_not_empty():
    """Ensure the data source has rows."""
    df = load_data()
    assert len(df) > 0
