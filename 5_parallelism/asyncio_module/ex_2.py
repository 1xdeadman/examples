# https://docs.python.org/3/library/asyncio.html
# https://docs.python.org/3/library/asyncio-task.html
# https://docs.python.org/3/library/asyncio-api-index.html
import asyncio
import time
import threading as thr


async def my_checker():
    for i in range(5):
        await asyncio.sleep(0.5)
        print("all_tasks:", len(asyncio.all_tasks()))
        for task in asyncio.all_tasks():
            print("--", task)
    return True


async def my_sub_func(row: str):
    for i in range(5):
        await asyncio.sleep(0.3)
    print("stop")
    return True


async def my_func(row):
    print(thr.current_thread().getName())
    data = await my_sub_func(row)
    return data


async def main():
    print(f"started at {time.strftime('%X')}")
    task_checker = asyncio.create_task(my_checker())
    task1 = asyncio.create_task(my_func(""))
    task2 = asyncio.create_task(my_func(" "))

    print("done1:", task1.done())
    print("done2:", task2.done())
    await asyncio.sleep(0.3)
    task2.cancel("azaza")
    await task1
    # await task_checker
    print("cancelled1:", task1.cancelled())
    print("result1:", task1.result())
    try:
        await task2
        print("result2:", task2.result())
    except asyncio.CancelledError as ex:
        print("cancelled2:", task2.cancelled())
    print(f"finished at {time.strftime('%X')}")


asyncio.run(main())
# Lock
# Event
# Condition
# Semaphore
# BoundedSemaphore
