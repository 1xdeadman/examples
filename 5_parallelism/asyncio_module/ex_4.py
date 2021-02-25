import asyncio
import threading as thr
import time


def print_thread_name(name: str):
    print(f"{name}:", thr.current_thread().getName())


def task():
    print_thread_name("sync")
    return "sync"


async def async_task():
    print_thread_name("async")
    return "async"


async def main():
    print_thread_name("main")
    res = await asyncio.gather(
        asyncio.to_thread(task),
        async_task()
    )

    print("res:", res)

    fut = asyncio.to_thread(task)
    print(fut)
    res = await fut
    print("res:", res)


asyncio.run(main())
