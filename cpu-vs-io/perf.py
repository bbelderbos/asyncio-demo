from cpu import sequential_prime_count, threaded_prime_count
from network import sequential_fetch_url, async_network_io, async_aiohttp

# for free-threading: uv run --python 3.13t perf.py

print("=" * 50)
print("CPU-Bound Task (Prime Calculation):")
sequential_prime_count()
threaded_prime_count()

print("\n" + "=" * 50)
print("IO-Bound Task (Network Fetching):")
sequential_fetch_url()
async_network_io()
async_aiohttp()
print("=" * 50)
