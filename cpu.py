from threading import Thread

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_primes_in_range(start, end):
    return sum(1 for n in range(start, end) if is_prime(n))

def sequential_prime_count():
    ranges = [(10**6, 10**6 + 10000), (10**6 + 10000, 10**6 + 20000)]
    results = []
    for start, end in ranges:
        results.append(count_primes_in_range(start, end))
    return results

def threaded_prime_count():
    ranges = [(10**6, 10**6 + 10000), (10**6 + 10000, 10**6 + 20000)]
    results = []

    def count_and_store(start, end):
        results.append(count_primes_in_range(start, end))

    threads = []
    for start, end in ranges:
        t = Thread(target=count_and_store, args=(start, end))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
    return results
