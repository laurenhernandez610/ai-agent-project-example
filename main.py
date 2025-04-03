# ------------------------------------------------------------------------------
# main.py
# ------------------------------------------------------------------------------
# This is the main command-line interface (CLI) entrypoint for the project.
#
# Purpose:
# - Launches the AI assistant or its supporting logic from your local machine
# - Loads all runtime configurations from `settings.py` (.env file)
# - Handles orchestration: choosing the agent type, loading data, processing, etc.
#
# In production, this file is often replaced by:
# - an API layer (e.g., FastAPI, Flask)
# - a scheduled workflow (e.g., Airflow, cron)
# - or an external trigger (e.g., Slack bot, REST call)
#
# Usage (from root directory):
#   $ python main.py
#
# Future expansion: add CLI flags for input type, agent mode, data paths, etc.
# ------------------------------------------------------------------------------

from config.settings import get_settings
from src.utils.helpers import logger, print_banner
from src.agents.agent import run_agent
from src.agents.langchain_agent import run_langchain_agent
from src.pipeline.ingest import load_data
from src.pipeline.preprocess import clean_data
from src.pipeline.postprocess import format_output
# from src.model.fine_tune import train_dummy_model      # Optional: Classical model
# from src.llm.openai_interface import call_llm          # Optional: raw LLM interface

# Optional imports for working with inputs
# from pathlib import Path
# import argparse


def main():
    print_banner("Launching AI Agentic Assistant")

    # Load configuration
    settings = get_settings()
    logger.info(f"Environment: {settings.ENV}")
    logger.info(f"Using LangChain: {settings.USE_LANGCHAIN}")

    # -------------------------
    # 1. Ingest Data (Optional)
    # -------------------------
    logger.info("Loading sample data...")
    data = load_data("data/raw/sample.csv")
    if data.empty:
        logger.warning("No data loaded. Proceeding without dataset.")

    # -------------------------
    # 2. Preprocess (Optional)
    # -------------------------
    clean_df = clean_data(data)

    # -------------------------
    # 3. Agent Call (Main Task)
    # -------------------------
    user_input = "What is the future of AI in healthcare?"  # You can replace this

    if settings.USE_LANGCHAIN:
        logger.info("Running LangChain agent...")
        result = run_langchain_agent(user_input)
    else:
        logger.info("Running basic LLM agent...")
        result = run_agent(user_input)

    # -------------------------
    # 4. Postprocess Result
    # -------------------------
    final_output = format_output(result)

    # -------------------------
    # 5. (Optional) Train or Score Local Models
    # -------------------------
    # X = clean_df.drop("target", axis=1)
    # y = clean_df["target"]
    # model = train_dummy_model(X, y)

    # -------------------------
    # 6. Output the Final Result
    # -------------------------
    logger.info("Agent response:")
    print("\n=== Agent Output ===")
    print(final_output)

    # Optional: write result to file or return to another system
    # with open("logs/last_response.json", "w") as f:
    #     json.dump(final_output, f, indent=2)


if __name__ == "__main__":
    main()
