import asyncio
import threading as thr
import time


def print_thread_name(name: str):
    print(f"{name}: {thr.current_thread().getName()}: {thr.get_ident()}")


def task():
    print_thread_name("thread")
    return "thread"


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
    #
    # fut = asyncio.to_thread(task)
    # print(fut)
    # thread_res = await fut
    # print("res:", thread_res)


asyncio.run(main())
