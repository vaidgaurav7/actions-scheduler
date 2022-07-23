import logging
import logging.handlers
import os

import requests

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger_file_handler = logging.handlers.RotatingFileHandler(
    "status.log",
    maxBytes=1024 * 1024,
    backupCount=1,
    encoding="utf8",
)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger_file_handler.setFormatter(formatter)
logger.addHandler(logger_file_handler)

try:
    SOME_SECRET = os.environ["SOME_SECRET"]
except KeyError:
    SOME_SECRET = "Token missing from environment!"


if __name__ == "__main__":
    logger.info(f"Here's Token value: {SOME_SECRET}")

    r = requests.get('https://random-words-api.vercel.app/word')
    if r.status_code == 200:
        data = r.json()
        word = data[0]["word"]
        defination = data[0]["definition"]
        logger.info(f"""Today's word of the day: "{word}", Definition: {defination}""")