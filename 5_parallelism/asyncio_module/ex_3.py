import asyncio


async def task():
    print("before")
    await asyncio.sleep(2)
    print("after")


async def main():
    await asyncio.gather(
        task(),
        task()
    )


asyncio.run(main())
