from logging import FileHandler, Formatter, Logger, getLogger

from rich import pretty, traceback
from rich.logging import RichHandler
from utils.settings import settings

pretty.install()
_ = traceback.install()


def get_logger(name: str, file_name: str | None = None) -> Logger:
    """Get a logger with a custom formatter."""
    debug_level = settings.get("LOG_LEVEL", "INFO")
    logger = getLogger(name)
    logger.setLevel(debug_level)
    logger.handlers = [RichHandler(rich_tracebacks=True, tracebacks_show_locals=True)]

    if file_name is not None:
        file_handler = FileHandler(filename=f"{file_name.split('.', 1)[0]}.log")
        file_handler.setFormatter(
            Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s"),
        )
        logger.addHandler(file_handler)

    return logger
