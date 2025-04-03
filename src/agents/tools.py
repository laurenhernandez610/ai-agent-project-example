# ------------------------------------------------------------------------------
# tools.py
# ------------------------------------------------------------------------------
# This module defines auxiliary functions that the agent may use.
# Tools can be APIs, utilities, formatters, or callable skills.
#
# These can be routed dynamically by the agent or called manually.
# ------------------------------------------------------------------------------

import datetime

def get_current_time() -> str:
    """Returns the current time in HH:MM:SS format."""
    return datetime.datetime.now().strftime("%H:%M:%S")

def summarize_text(text: str) -> str:
    """
    Dummy summarization tool.
    In production, this could route through an LLM or extractive model.
    """
    return text[:100] + "..." if len(text) > 100 else text

def reverse_string(text: str) -> str:
    """A simple string reversal tool for demonstration."""
    return text[::-1]
