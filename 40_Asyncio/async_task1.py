import asyncio
import time

async def fib(n):
    start = time.time()
    first = 0
    second = 1
    res = 0
    for _ in range(2, n + 1):
        await asyncio.sleep(0.5)
        res = first + second
        first, second = second, res
    end = time.time()
    print(f"Task Fib: fib({n}) = {res}, computed in {end - start} seconds")
    return res

async def fact(n):
    start = time.time()
    res = 1
    for i in range(2, n + 1):
        await asyncio.sleep(1)
        res *= i
    end = time.time()
    print(f"Task Factorial: factorial({n}) = {res}, computed in {end - start} seconds")
    return res
        

async def cubic(n):
    start = time.time()
    await asyncio.sleep(4)
    res = n ** 3
    end = time.time()
    print(f"Task Cubic: Computed cubic {n} = {res}, computed in {end - start} seconds")
    return res

async def square(n):
    start = time.time()
    await asyncio.sleep(5)
    res = n ** 2
    end = time.time()
    print(f"Task Square: Computed square {n} = {res}, computed in {end - start} seconds")
    return res

async def main(n):
    start = time.time()
    print(await asyncio.gather(fib(n), fact(n), cubic(n), square(n)))
    end = time.time()
    print(f'All done in {int(end - start)} seconds')

asyncio.run(main(9))