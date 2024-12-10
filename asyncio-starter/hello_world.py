import asyncio


async def say_hello():
    """
    Demonstrates how to use the `async` and `await` keywords to create an asynchronous function.

    - The `async` keyword defines this function as a coroutine, which can be paused and resumed.
    - The `await` keyword pauses the execution of this coroutine until the awaited operation (e.g., `asyncio.sleep`) completes.

    Note:
    - The `await asyncio.sleep(3)` simulates an asynchronous wait but only blocks this coroutine,
      not the entire event loop. If there are other tasks running concurrently, they can continue
      executing while this coroutine is paused.
    """
    print("Hello...")
    await asyncio.sleep(3)
    print("...World!")


asyncio.run(say_hello())
