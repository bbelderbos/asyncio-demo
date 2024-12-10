"""
This script fetches multiple URLs asynchronously, demonstrating the use of `asyncio.create_task`
to run multiple coroutines concurrently.
"""
import asyncio
import time

import requests

urls = [
    "https://httpbin.org/delay/2",
    "https://httpbin.org/delay/3",
    "https://httpbin.org/delay/1",
    "https://httpbin.org/status/500",
]


def get_url(url):
    """
    A wrapper around `requests.get` to handle common HTTP errors.
    This function raises an exception if the response status is not 2xx.
    """
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for 4xx/5xx status codes
    return response


async def fetch_url(url):
    """
    Fetches a URL using the `requests` library, which is a blocking library
    (demo purposes only; in production, you might want to check out `aiohttp` or `httpx`
    for fully asynchronous HTTP requests).

    To integrate this blocking library with `asyncio`, we use `run_in_executor` to offload the
    blocking operation to a separate thread. This allows the event loop to remain responsive
    and process other tasks while the HTTP request is in progress.

    Key points:
    - `get_running_loop` retrieves the current asyncio event loop.
    - `run_in_executor(None, ...)` schedules the blocking `get_url` call.
    """
    loop = asyncio.get_running_loop()
    response = await loop.run_in_executor(None, get_url, url)
    print(f"Fetched {url}: {response.status_code}")


async def main():
    """
    Creates tasks for fetching multiple URLs concurrently.

    - Explicitly awaiting each task ensures we handle exceptions on a per-task basis.
    - This approach provides fine-grained control compared to `asyncio.gather`.
    """
    tasks = [asyncio.create_task(fetch_url(url)) for url in urls]
    for task in tasks:
        try:
            await task
        except requests.exceptions.RequestException as e:
            print(f"Task failed with error: {e}")


if __name__ == "__main__":
    start_time = time.perf_counter()
    asyncio.run(main())
    print(f"Async version took: {time.perf_counter() - start_time:.2f} seconds")
