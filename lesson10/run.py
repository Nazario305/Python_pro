import threading
import random
from typing import List

shared_list = []

lock = threading.Lock()
list_filled = threading.Event()

# Thread T1
def fill_list():
    global shared_list
    with lock:
        shared_list = [random.randint(1, 1000) for _ in range(10_000)]
        print("List filled with random numbers.")
    list_filled.set()

# Thread T2
def calculate_sum():
    list_filled.wait()
    with lock:
        total_sum = sum(shared_list)
        print(f"Sum of list elements: {total_sum}")

# Thread T3
def calculate_average():
    list_filled.wait()
    with lock:
        avg = sum(shared_list) / len(shared_list) if shared_list else 0
        print(f"Arithmetic average of list elements: {avg}")


def get_primes_amount(numbers: List[int]) -> int:
    def is_prime(n: int) -> bool:
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    result = 0
    def count_primes(num_chunk):
        nonlocal result
        result += sum(1 for num in num_chunk if is_prime(num))


    chunk_size = len(numbers) // 4
    chunks = [numbers[i:i + chunk_size] for i in range(0, len(numbers), chunk_size)]

    threads = []
    for chunk in chunks:
        thread = threading.Thread(target=count_primes, args=(chunk,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return result


def main():
    # Start threads
    t1 = threading.Thread(target=fill_list)
    t2 = threading.Thread(target=calculate_sum)
    t3 = threading.Thread(target=calculate_average)

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    # Test get_primes_amount
    numbers = [40000, 400, 1000000, 700]
    primes_count = get_primes_amount(numbers)
    print(f"Number of primes: {primes_count}")

if __name__ == "__main__":
    main()
