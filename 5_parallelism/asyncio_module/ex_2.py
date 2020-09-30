# https://docs.python.org/3/library/asyncio.html
# https://docs.python.org/3/library/asyncio-task.html
# https://docs.python.org/3/library/asyncio-api-index.html
import asyncio
import time


async def my_checker():
    for i in range(10):
        await asyncio.sleep(1)
        print("all_tasks:", len(asyncio.all_tasks()))
        # for task in asyncio.all_tasks():
        #    print("--", task)
    return True


async def my_sub_func(row: str):
    for i in range(10):
        await asyncio.sleep(0.3)
        # print(row+str(i))
    print("stop")
    return True


async def my_func(row):
    data = await my_sub_func(row)
    return data


async def main():
    task_checker = asyncio.create_task(my_checker())
    task1 = asyncio.create_task(my_func(""))
    task2 = asyncio.create_task(my_func(" "))

    print(f"started at {time.strftime('%X')}")

    # Wait until both tasks are completed (should take
    # around 2 seconds.)
    print("done:", task1.done())
    await task1
    await task2
    await task_checker
    print("done:", task1.done())
    print("cancelled:", task1.done())
    print("cancelled:", task1.done())
    print("result:", task1.result())

    print(f"finished at {time.strftime('%X')}")


asyncio.run(main())
# Lock
# Event
# Condition
# Semaphore
# BoundedSemaphore
