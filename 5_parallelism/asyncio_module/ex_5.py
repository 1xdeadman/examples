import asyncio
import concurrent.futures
import threading
import os


def get_info():
    print("proc:", os.getpid(), " || thread:", threading.get_ident())


def read_file():
    get_info()
    with open(r"D:\projects\studies\examples\TestData\text.txt", 'rb') as file:
        return file.read(100)


def cpu_bound():
    get_info()
    res = sum(i * i for i in range(10 ** 7))
    return res


async def main():
    get_info()

    loop = asyncio.get_running_loop()

    result = await loop.run_in_executor(
        None, read_file)
    print('default thread pool', result)

    with concurrent.futures.ThreadPoolExecutor() as pool:
        result = await loop.run_in_executor(
            pool, read_file)
        print('custom thread pool', result)

    with concurrent.futures.ProcessPoolExecutor() as pool:
        result = await loop.run_in_executor(
            pool, cpu_bound)
        print('custom process pool', result)


if __name__ == '__main__':
    asyncio.run(main())
