import asyncio


async def task(name, delay):
    """
    Same as before: define a coroutine with `async def`
    This function simulates some work by pausing for `delay` seconds.
    """
    print(f"Starting {name}")
    await asyncio.sleep(delay)  # Simulates some work
    print(f"Finished {name}")


async def main():
    """
    Now we use `asyncio.gather` to run multiple tasks concurrently.
    Each task starts and can pause (await) independently of the others.
    The event loop ensures that all tasks progress concurrently.
    """
    tasks = [task(f"Task {i}", i) for i in range(1, 5)]
    await asyncio.gather(*tasks)


# Run the main coroutine in an event loop:
asyncio.run(main())
