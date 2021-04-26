# https://docs.python.org/3/library/multiprocessing.html
import multiprocessing as mp
import time


def proc_func(locker):
    for i in range(10000):
        if locker.acquire(timeout=1):
            print(f'{i}: {mp.current_process().name}')
            locker.release()


if __name__ == '__main__':
    my_locker = mp.Lock()

    # my_rec_locker = mp.RLock()
    new_process = mp.Process(
        target=proc_func,
        name="new_process",
        kwargs={"locker": my_locker}
    )
    new_process.start()

    proc_func(my_locker)

    new_process.join()
    print(f"{new_process.name} finished")
