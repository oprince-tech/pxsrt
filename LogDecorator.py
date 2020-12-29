import logging
from functools import wraps

def init_logger():
    """
    Initialize a logger (logger, file, format, handler)
    """
    logger = logging.getLogger('exception_logger')
    logger.setLevel(logging.ERROR)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s: %(name)s: %(message)s')

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
            except:
                exc = "exception in " + func.__name__ + "\n"
                exc = exc + ("-" * 79) + "\n"
                logger.exception(exc)
            raise
        return wrapper
    return decorator

# def info(logger):
#     def decorator(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             logger.info(func)
#             return func(*args, **kwargs)
#         return wrapper
#     return decorator
