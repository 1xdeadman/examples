import asyncio


async def task():
    print("before")
    await asyncio.sleep(4)
    print("after")


async def main():
    await asyncio.sleep(1)

    # task1 = asyncio.create_task(task())
    task1 = asyncio.shield(task())
    await asyncio.sleep(0.5)
    
    task1.cancel()
    await task1


asyncio.run(main())
