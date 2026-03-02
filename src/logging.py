import logging
import os

from pathlib import Path
from functools import wraps
from datetime import datetime



LOG_DIR = Path(__file__).parent.parent / "logs"
LOG_FILE = LOG_DIR / f"suci_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"

_loggers: dict[str, logging.Logger] = {}


#########################################################
def setup_logging(level: int = logging.DEBUG):
    LOG_DIR.mkdir(exist_ok=True)
    
    logging.basicConfig(
        level=level,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler(LOG_FILE),
            logging.StreamHandler()
        ]
    )


def get_logger(name: str) -> logging.Logger:
    if name not in _loggers:
        _loggers[name] = logging.getLogger(name)
    return _loggers[name]


def log_calls(logger: logging.Logger | None = None):
    def decorator(func):
        nonlocal logger
        if logger is None:
            logger = get_logger("sucurindex")
        
        @wraps(func)
        def wrapper(*args, **kwargs):
            logger.info(f"CALL {func.__name__}(args={args}, kwargs={kwargs})")
            try:
                result = func(*args, **kwargs)
                logger.info(f"RETURN {func.__name__} -> {result}")
                return result
            except Exception as e:
                logger.error(f"EXCEPTION {func.__name__}: {e}")
                raise
        
        return wrapper
    return decorator



def main_with_logging(main_func=None):
    import sys
    setup_logging()
    logger = get_logger("sucurindex")
    logger.info(f"CLI started: {' '.join(sys.argv)}")
    try:
        if main_func:
            main_func()
        else:
            main()
        logger.info("CLI finished successfully")
    except Exception as e:
        logger.error(f"CLI failed: {type(e).__name__}: {e}")
        raise


#########################################################
def main():
    pass
