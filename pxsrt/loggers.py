# type: ignore
import logging
import time
from functools import wraps


def init_logger():
    """
    Initialize a logger (logger, file, format, handler)
    """
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        '%(asctime)s - %(levelname)s: %(name)s: %(message)s',
    )

    file_handler = logging.FileHandler('logging.log')
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    return logger


logger = init_logger()


def exception(logger):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception:
                exc = 'exception in ' + func.__name__ + '\n'
                exc = exc + ('=' * 79) + '\n'
                logger.exception(exc)
                raise
        return wrapper
    return decorator


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f'{func.__module__}, {func.__name__}: {end-start} seconds')
        return result
    return wrapper
