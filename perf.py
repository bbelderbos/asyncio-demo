import asyncio
import time

from cpu import sequential_prime_count, threaded_prime_count
from network import sequential_fetch_url, async_network_io, async_network_io_httpx


def measure_time(func, *args):
    start = time.perf_counter()
    func(*args)
    elapsed = time.perf_counter() - start
    print(f"{func.__name__}: {elapsed:.2f} seconds")


def measure_async_time(coro, *args):
    start = time.perf_counter()
    asyncio.run(coro(*args))
    elapsed = time.perf_counter() - start
    print(f"{coro.__name__}: {elapsed:.2f} seconds")


if __name__ == "__main__":
    print("=" * 50)
    print("CPU-Bound Task (Prime Calculation):")
    measure_time(sequential_prime_count)
    measure_time(threaded_prime_count)

    print("\n" + "=" * 50)
    print("IO-Bound Task (Network Fetching):")
    measure_time(sequential_fetch_url)
    measure_async_time(async_network_io)
    measure_async_time(async_network_io_httpx)
    print("=" * 50)
