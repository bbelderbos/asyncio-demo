"""
This script fetches multiple URLs synchronously.
"""
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
    response.raise_for_status()
    return response


def fetch_url_sync(url):
    response = get_url(url)
    print(f"Fetched {url}: {response.status_code}")


def main():
    for url in urls:
        try:
            fetch_url_sync(url)
        except requests.exceptions.RequestException as e:
            print(f"Error fetching {url}: {e}")


if __name__ == "__main__":
    start_time = time.perf_counter()
    main()
    print(f"Sync version took: {time.perf_counter() - start_time:.2f} seconds")
