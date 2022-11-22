import concurrent.futures
from math import sqrt
import time

NUMBERS = [
   2,  # prime
   1099726899285419,
   1570341764013157,  # prime
   1637027521802551,  # prime
   1880450821379411,  # prime
   1893530391196711,  # prime
   2447109360961063,  # prime
   3,  # prime
   2772290760589219,  # prime
   3033700317376073,  # prime
   4350190374376723,
   4350190491008389,  # prime
   4350190491008390,
   4350222956688319,
   2447120421950803,
   5,  # prime
]

def is_prime(number):
    if number in [1, 2, 3, 5]:
        return f'{number} is prime'
    if not number % 2:
        return f'{number} is not prime - divided by 2'
    for num in range(3, int(sqrt(number)) + 1, 2):
        if not number % num:
            return f'{number} is not prime - divided by {num}'
    return f'{number} is prime'

def main():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for num in NUMBERS:
            futures.append(executor.submit(is_prime, number=num))
        for future in concurrent.futures.as_completed(futures):
            print(future.result())

if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print(f'Ended in {end - start} seconds')