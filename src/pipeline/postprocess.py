# ------------------------------------------------------------------------------
# postprocess.py
# ------------------------------------------------------------------------------
# This module handles final formatting and output shaping before returning
# data to the user or storing it.
#
# Examples:
# - Convert model output to JSON
# - Clean up agent responses
# - Add metadata or confidence scores
# ------------------------------------------------------------------------------

def format_output(result: dict) -> dict:
    """
    Formats the final output from the agent or model.

    Args:
        result (dict): Raw result.

    Returns:
        dict: Cleaned, structured output.
    """
    return {
        "status": "success",
        "data": result
    }
