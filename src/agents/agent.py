# ------------------------------------------------------------------------------
# agent.py
# ------------------------------------------------------------------------------
# Default LLM - Based Agent 
# This file contains the core logic for a generalized AI agent.
# The agent takes user input, constructs a prompt, sends it to an LLM,
# and returns the structured response.
#
# This agent could be used for planning, summarizing, retrieval, reasoning,
# or any other task depending on the input and prompt used.
# ------------------------------------------------------------------------------

#from config.prompts.prompts import load_prompt  # Optional utility for templating
from src.llm.openai_interface import call_llm   # Generic interface to LLM
from src.utils.helpers import logger            # Logging utility

def run_agent(user_input: str = "What should I know about agentic AI?") -> dict:
    """
    Runs the generalized agent logic.

    Args:
        user_input (str): The user's request, instruction, or query.

    Returns:
        dict: A structured response from the agent.
    """
    logger.info("Running AI agent...")

    # Load a predefined prompt and combine it with user input
    #prompt = f"{load_prompt()}\nUser: {user_input}"
    #response = call_llm(prompt)

    # logger.info("Agent completed response.")
    # return {
    #     "input": user_input,
    #     "output": response
    # }
