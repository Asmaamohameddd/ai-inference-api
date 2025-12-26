# utils.py
import logging

logging.basicConfig(
    filename="token_usage.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

def log_token_usage(prompt: str, output: str, tokens: dict):
    logging.info(f"Prompt: {prompt}")
    logging.info(f"Output: {output}")
    logging.info(f"Tokens: {tokens}")
