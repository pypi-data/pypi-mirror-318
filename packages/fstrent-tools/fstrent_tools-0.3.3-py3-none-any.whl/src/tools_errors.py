import traceback

def format_exception(e: Exception) -> str:
    """Format exception with traceback for logging."""
    return ''.join(traceback.format_exception(type(e), e, e.__traceback__))
