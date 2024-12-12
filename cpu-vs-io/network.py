"""
Similar as prior demo, but now we use `asyncio.gather` to fetch all URLs concurrently.
"""
import asyncio

import requests  # blocking library
import aiohttp

from util import measure_time

urls = """
https://pybit.es/articles/a-practical-example-of-the-pipeline-pattern-in-python/
https://pybit.es/articles/from-python-script-to-web-app-and-product/
https://pybit.es/articles/introducing-exact-rag-the-ultimate-local-multimodal-rag/
https://pybit.es/articles/repository-pattern-in-python/
https://pybit.es/articles/learn-python-from-scratch-with-our-50-newbie-bite-exercises/
https://pybit.es/articles/fastapi-app-as-azure-function-howto/
https://pybit.es/articles/openstreetmaps-overpass-api-and-python/
https://pybit.es/articles/adventures-in-import-land-part-ii/
https://pybit.es/articles/python-f-string-codes-i-use-every-day/
https://pybit.es/articles/a-better-place-to-put-your-python-virtual-environments/
""".strip().splitlines()


@measure_time
def sequential_fetch_url():
    results = []
    for url in urls:
        response = requests.get(url)
        results.append(len(response.content))
    return results


async def _async_fetch_url(url):
    loop = asyncio.get_running_loop()
    return await loop.run_in_executor(None, requests.get, url)


@measure_time
async def async_network_io():
    tasks = [_async_fetch_url(url) for url in urls]
    responses = await asyncio.gather(*tasks)
    return [len(response.content) for response in responses]


async def _aiohttp_fetch_url(session, url):
    async with session.get(url) as response:
        return await response.text()


@measure_time
async def async_aiohttp():
    async with aiohttp.ClientSession() as session:
        tasks = [_aiohttp_fetch_url(session, url) for url in urls]
        responses = await asyncio.gather(*tasks)
        return [len(response) for response in responses]
