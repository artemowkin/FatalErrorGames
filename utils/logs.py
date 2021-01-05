import logging


logger = logging.getLogger('filelogger')


def handle_services_exceptions(func):
    """Decorator that handle exceptions in services functions"""

    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logger.error(
                f"An error `{e.__class__.__name__}` occurred in the function "
                f"`{func.__name__}` with arguments: {args} and keyword "
                f"arguments: {kwargs}"
            )
            raise

    return wrapper
