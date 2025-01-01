import importlib
import logging

LOG_FORMAT = "%(asctime)s %(levelname)s %(message)s"
LOG_FILE = "search.log"


def setup_logger(name: str = "global", level: int = logging.DEBUG) -> logging.Logger:
    logger = logging.getLogger(name)
    if not logger.handlers:
        logger.setLevel(level)

        try:
            file_handler = logging.FileHandler(LOG_FILE, mode='w')
            file_handler.setLevel(logging.DEBUG)
            file_handler.setFormatter(logging.Formatter(LOG_FORMAT))
            logger.addHandler(file_handler)
        except Exception as e:
            print(f"Failed to set up file handler: {e}")

        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.INFO)
        logger.addHandler(stream_handler)

    return logger


log = setup_logger()

AniSearch = importlib.import_module('.AniSearch', package=__name__).AniSearch
print("\033[91m请使用新的项目: animag\033[0m")
print("\033[91mPlease use the new project: animag\033[0m")
