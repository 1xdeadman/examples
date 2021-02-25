# https://docs.python.org/3/library/asyncio.html
# https://docs.python.org/3/library/asyncio-task.html
# https://docs.python.org/3/library/asyncio-api-index.html
import asyncio
import time


async def say_after(delay, what):
    print(f'before {what}')
    await asyncio.sleep(delay)
    print(f'after {what}')


async def main():
    print(f"started at {time.strftime('%X')}")

    task1 = asyncio.create_task(say_after(1, 'hello'))
    task2 = asyncio.create_task(say_after(2, 'world'))

    print('before main')
    # time.sleep(5)
    await asyncio.sleep(5)
    print('after main')

    await task1
    await task2

    # await say_after(1, 'hello')
    # await say_after(2, 'world')

    print(f"finished at {time.strftime('%X')}")


asyncio.run(main())


