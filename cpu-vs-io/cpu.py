"""
Using threading to parallelize CPU-bound tasks

This is not efficient because of the Global Interpreter Lock (GIL)

The GIL allows only one thread to execute Python bytecode at a time.
Thus, even though multiple threads are created, they are not truly parallel,
and the performance gain is limited (or non-existent) compared to sequential execution.

But we can compare free-threading 3.13 ...
Or use multiprocessing instead of threading (to be continued)
"""
from queue import Queue
from threading import Thread

from util import measure_time

ranges = [(10**6, 10**6 + 10000), (10**6 + 10000, 10**6 + 20000)]

def is_prime(n):
    """
    Function to check if a number is prime
    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def count_primes_in_range(start, end):
    return sum(1 for n in range(start, end) if is_prime(n))


@measure_time
def sequential_prime_count():
    results = []
    for start, end in ranges:
        results.append(count_primes_in_range(start, end))
    return results


# shared results list, not safe
# use a queue instead
"""
def threaded_prime_count():
    results = []
    def count_and_store(start, end):
        results.append(count_primes_in_range(start, end))

    # Create and start threads (note: this is memory-inefficient)
    threads = []
    for start, end in ranges:
        t = Thread(target=count_and_store, args=(start, end))
        threads.append(t)
        t.start()

    # Wait for all threads to finish
    for t in threads:
        t.join()

    return results
"""


@measure_time
def threaded_prime_count():
    """
    Count primes using threads.

    A thread-safe Queue is used to store results because appending to a shared list
    could lead to race conditions when accessed by multiple threads.
    """
    results = Queue()

    def count_and_store(start, end):
        results.put(count_primes_in_range(start, end))

    threads = []
    for start, end in ranges:
        t = Thread(target=count_and_store, args=(start, end))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    # Collect results from the queue
    return [results.get() for _ in ranges]
