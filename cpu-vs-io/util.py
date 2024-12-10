import time

import asyncio
from functools import wraps


def measure_time(func):
    """
    A decorator to measure the execution time of a function or coroutine.
    Automatically detects whether the target is synchronous or asynchronous.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        # breakpoint()
        if asyncio.iscoroutinefunction(func):
            result = asyncio.run(func(*args, **kwargs))
        else:
            result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"{func.__name__}: {elapsed:.2f} seconds")
        return result

    return wrapper
