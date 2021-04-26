# https://docs.python.org/3/library/asyncio.html
# https://docs.python.org/3/library/asyncio-task.html
# https://docs.python.org/3/library/asyncio-api-index.html
import asyncio
import time
import threading
import os


def func(x: asyncio.Task):
    print(f"endddd::{x}")


def get_info():
    print("proc:", os.getpid(), " || thread:", threading.get_ident())


async def say_after(delay, what):
    print(f'start {what}')
    get_info()
    await asyncio.sleep(delay)
    print(f'end {what}')


async def main():
    print(f"started at {time.strftime('%X')}")
    get_info()

    task1 = asyncio.create_task(say_after(1, 'hello'), name="TASK 1")
    task2 = asyncio.create_task(say_after(2, 'world'), name="TASK 2")

    task1.add_done_callback(func)

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
