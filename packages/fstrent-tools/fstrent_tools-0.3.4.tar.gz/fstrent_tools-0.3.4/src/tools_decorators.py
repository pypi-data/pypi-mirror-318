import functools
import time
from datetime import datetime
from typing import Any, Dict, Type, TypeVar
from fstrent_colors import cp

T = TypeVar('T')

__all__ = [
    # Class decorators
    'timing_class',
    'debug_class',
    'log_class',
    'singleton',
    # Function decorators
    'time_it'
]

def timing_class(cls: Type[T]) -> Type[T]:
    """Class decorator that adds timing functionality to all methods."""
    original_new = cls.__new__
    original_init = cls.__init__

    class TimingWrapper:
        def __init__(self):
            self.timing_stats: Dict[str, Dict[str, float]] = {}
            if original_new is object.__new__:
                self.instance = original_new(cls)
            else:
                self.instance = original_new(cls)
            if original_init is not None:
                original_init(self.instance)
        
        def __getattr__(self, name: str) -> Any:
            attr = getattr(self.instance, name)
            if not callable(attr):
                return attr
            
            @functools.wraps(attr)
            def wrapper(*args: Any, **kwargs: Any) -> Any:
                start_time = time.time()
                result = attr(*args, **kwargs)
                elapsed = time.time() - start_time
                
                if name not in self.timing_stats:
                    self.timing_stats[name] = {'total_time': 0.0, 'calls': 0}
                self.timing_stats[name]['total_time'] += elapsed
                self.timing_stats[name]['calls'] += 1
                
                return result
            
            return wrapper
        
        def get_timing_stats(self) -> Dict[str, Dict[str, float]]:
            return self.timing_stats
        
        def print_timing_stats(self) -> None:
            for name, stats in self.timing_stats.items():
                avg_time = stats['total_time'] / stats['calls'] if stats['calls'] > 0 else 0
                print(f"{name}: {stats['calls']} calls, total {stats['total_time']:.3f}s, avg {avg_time:.3f}s")
    
    return type(cls.__name__, (TimingWrapper,), {})

def debug_class(cls: Type[T]) -> Type[T]:
    """Class decorator that adds debug logging to all methods."""
    original_new = cls.__new__
    original_init = cls.__init__

    class DebugWrapper:
        def __init__(self):
            if original_new is object.__new__:
                self.instance = original_new(cls)
            else:
                self.instance = original_new(cls)
            if original_init is not None:
                original_init(self.instance)
        
        def __getattr__(self, name: str) -> Any:
            attr = getattr(self.instance, name)
            if not callable(attr):
                return attr
            
            @functools.wraps(attr)
            def wrapper(*args: Any, **kwargs: Any) -> Any:
                try:
                    print(f"[DEBUG] Calling {name} with args={args}, kwargs={kwargs}")
                    result = attr(*args, **kwargs)
                    print(f"[DEBUG] {name} returned {result}")
                    return result
                except Exception as e:
                    print(f"[DEBUG] Exception in {cls.__name__}.{name}: {str(e)}")
                    raise
            
            return wrapper
    
    return type(cls.__name__, (DebugWrapper,), {})

def log_class(cls):
    """Class decorator that adds logging functionality to all methods."""
    class LoggedClass(cls):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self._logs = {}

        def __getattribute__(self, name):
            attr = super().__getattribute__(name)
            if name in ['_logs', 'get_log', 'clear_log'] or not callable(attr) or name.startswith('_'):
                return attr

            def wrapper(*args, **kwargs):
                if name not in self._logs:
                    self._logs[name] = []
                try:
                    result = attr(*args, **kwargs)
                    self._logs[name].append({
                        'timestamp': time.time(),
                        'args': args,
                        'kwargs': kwargs,
                        'status': 'SUCCESS',
                        'result': result
                    })
                    return result
                except Exception as e:
                    self._logs[name].append({
                        'timestamp': time.time(),
                        'args': args,
                        'kwargs': kwargs,
                        'status': f'ERROR: {str(e)}',
                        'error': e
                    })
                    raise
            return wrapper

        def get_log(self):
            """Get all logs."""
            return self._logs

        def clear_log(self):
            """Clear all logs."""
            self._logs.clear()

    return LoggedClass

def singleton(cls: Type[T]) -> Type[T]:
    """Class decorator that ensures only one instance is created."""
    instances: Dict[Type[T], T] = {}
    
    @functools.wraps(cls)
    def get_instance(*args: Any, **kwargs: Any) -> T:
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    
    return get_instance

def time_it(secs_max: float = 0.33):
    """
    Decorator that times function execution and logs if it exceeds maximum time.

    Args:
        secs_max (float): Maximum expected execution time in seconds
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Start timing
            t0 = time.perf_counter()
            strt_dttm = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            # Execute function
            result = func(*args, **kwargs)

            # End timing
            end_dttm = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            secs = round(time.perf_counter() - t0, 3)

            # Log if execution time exceeds maximum
            if secs_max >= 0 and secs > secs_max:
                msg = f"{func.__name__:<35} began at {strt_dttm} completed at {end_dttm}, taking {secs} seconds... max : {secs_max} * {func.__qualname__}"
                cp(msg, font_clr='white', bg_clr='red')

            return result
        return wrapper
    return decorator

