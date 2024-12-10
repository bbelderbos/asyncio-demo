import asyncio


async def say_hello():
    """
    This function shows how to use the `async` and `await` keywords to
    create an asynchronous function.

    The `asyncio.run()` function is used
    to run the asynchronous function

    The fact that world prints right after sleep means that this sleep is
    not blocking the function from continuing to execute.
    """
    print("Hello...")
    await asyncio.sleep(3)  # Simulates waiting (e.g., network call)
    print("...World!")


asyncio.run(say_hello())
