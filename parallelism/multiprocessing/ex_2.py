# https://docs.python.org/3/library/multiprocessing.html
'''
multiprocessing is a package that supports spawning processes using an
API similar to the threading module. The multiprocessing package offers
both local and remote concurrency, effectively side-stepping the Global
Interpreter Lock by using subprocesses instead of threads. Due to this,
the multiprocessing module allows the programmer to fully leverage multiple
processors on a given machine. It runs on both Unix and Windows.
'''
import multiprocessing as mp


def proc_func(locker):
    for i in range(100):
        with locker:
            print(f'{i}: {mp.current_process().name}')


if __name__ == '__main__':
    mp.freeze_support()
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
