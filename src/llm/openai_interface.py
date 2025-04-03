# ------------------------------------------------------------------------------
# openai_interface.py
# ------------------------------------------------------------------------------
# This module wraps access to an LLM (e.g., OpenAI, Claude, Mistral).
# It provides a clean abstraction so the rest of the codebase does not
# depend on specific API logic, making it easy to swap or mock during testing.
#
# You can later extend this to support multiple providers or models.
# ------------------------------------------------------------------------------

import os
import openai
from config.settings import get_settings
from src.utils.helpers import logger

settings = get_settings()

openai.api_key = settings.OPENAI_API_KEY

def call_llm(prompt: str, temperature: float = 0.3) -> str:
    """
    Sends a prompt to OpenAI and returns the response as text.

    Args:
        prompt (str): The prompt to send to the model.
        temperature (float): Sampling temperature.

    Returns:
        str: The model's response text.
    """
    logger.info("Calling OpenAI LLM...")

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature
        )
        return response.choices[0].message["content"].strip()
    except Exception as e:
        logger.error(f"OpenAI call failed: {e}")
        return "Error: Could not get a response from LLM."
