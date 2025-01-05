import json
import time
import traceback
from functools import wraps
from typing import Any, Dict, Optional, Callable

__all__ = [
    'debug_print',
    'func_begin',
    'func_end',
    'func_timer',
    'print_stack',
    'print_traceback'
]

def debug_print(*args: Any, level: int = 1, **kwargs: Any) -> None:
    """Print debug information with specified level."""
    if level >= 1:  # Adjust based on global debug level
        print(*args, **kwargs, flush=True)

# Store function timing data
_func_timing: Dict[str, float] = {}


def func_begin(func_name: str) -> None:
    """Mark the beginning of a function for timing."""
    _func_timing[func_name] = time.time()

def func_end(func_name: str) -> Optional[float]:
    """Mark the end of a function and return elapsed time."""
    if func_name in _func_timing:
        elapsed = time.time() - _func_timing[func_name]
        del _func_timing[func_name]
        return elapsed
    return None

def func_timer(func: Callable) -> Callable:
    """Decorator to time function execution."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start_time
        print(f"{func.__name__} took {elapsed:.3f} seconds")
        return result
    return wrapper

def print_stack() -> None:
    """Print the current stack trace."""
    print(''.join(traceback.format_stack()), end='', flush=True)

def print_traceback() -> None:
    """Print the current exception traceback."""
    print(''.join(traceback.format_exc()), end='', flush=True)

