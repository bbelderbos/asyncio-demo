import asyncio


async def task(name, delay):
    """
    Same as before: task with simulated work
    """
    print(f"Starting {name}")
    await asyncio.sleep(delay)  # Simulates some work
    print(f"Finished {name}")
    return name


async def slow_task(name, delay, timeout):
    """
    To prevent a task from running indefinitely, we can use asyncio.wait_for
    to set a timeout. If the task does not complete within the timeout, it
    raises asyncio.TimeoutError which we can catch and handle.
    """
    try:
        return await asyncio.wait_for(task(name, delay), timeout=timeout)
    except asyncio.TimeoutError:
        print(f"{name} timed out!")
        return None


async def main():
    tasks = [slow_task(f"Task {i}", i, timeout=3) for i in range(1, 5)]
    results = await asyncio.gather(*tasks)
    print("Results:", results)


# Run event loop
asyncio.run(main())
