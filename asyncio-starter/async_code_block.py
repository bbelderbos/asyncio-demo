import asyncio


async def task(name, delay):
    """
    The async keyword before def makes this function a coroutine.
    A coroutine is a function that can be paused and resumed.
    The await keyword is used to pause the execution of the coroutine until the awaited coroutine (or awaitable) completes.
    This is conceptually similar to how yield pauses a generator, but await is specifically for asynchronous programming.
    """
    print(f"Starting {name}")
    await asyncio.sleep(delay)  # Simulates some work
    print(f"Finished {name}")


async def main():
    """
    In this implementation, tasks are run sequentially, not concurrently.
    The first task takes 2 seconds to complete, and only after it finishes does the second task (which takes 1 second) begin.
    This is because each await pauses the execution of the main coroutine until the awaited task completes.
    """
    await task("Task 1", 2)
    await task("Task 2", 1)


"""
We use asyncio.run() to run the main() coroutine.
This executes the main coroutine within an event loop.
Although this is asynchronous code, it does not run concurrently because the tasks in main() are awaited sequentially.
True concurrency requires running multiple coroutines simultaneously, which can
be achieved with asyncio.gather or asyncio.create_task (next ...)
"""
asyncio.run(main())
