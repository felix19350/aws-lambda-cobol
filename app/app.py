import logging
import sys
import os

logger = logging.getLogger(__name__)

logger.setLevel(logging.DEBUG)
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(formatter)
logger.addHandler(handler)

logger.info(f"Python version {sys.version}")


def handler(event, context):
    """A simple echo server lambda function."""
    logger.warning(f"Event: {event}")
    logger.warning(f"Context: {context}")

    stream = os.popen("./cobol-program")
    with stream as s:
        message = s.read()
        logger.info(f"Output from COBOL: {message}")

    return {"message": message}
