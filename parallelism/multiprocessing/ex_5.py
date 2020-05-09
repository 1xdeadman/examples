# https://docs.python.org/3/library/multiprocessing.html
'''
multiprocessing is a package that supports spawning processes using an
API similar to the threading module. The multiprocessing package offers
both local and remote concurrency, effectively side-stepping the Global
Interpreter Lock by using subprocesses instead of threads. Due to this,
the multiprocessing module allows the programmer to fully leverage multiple
processors on a given machine. It runs on both Unix and Windows.
'''
import time
import multiprocessing as mp

print("lol will be with proccess")


def proc_func(my_queue: mp.Queue):
    for i in range(10):
        time.sleep(1)
        # put(obj[, block[, timeout]])
        if i <= 4 and not my_queue.full():
            my_queue.put(f"{i}: from {mp.current_process().name}")
        if i == 4:
            my_queue.close()


if __name__ == '__main__':
    my_queue = mp.Queue(maxsize=100)
    prod_1 = mp.Process(
        target=proc_func,
        name="prod 1",
        args=(my_queue, )
    )
    prod_2 = mp.Process(
        target=proc_func,
        name="prod 2",
        args=(my_queue, )
    )

    prod_1.start()
    prod_2.start()

    while my_queue:
        try:
            print("new")
            if not my_queue.empty():
                print(my_queue.get(timeout=1.0))  # [block[, timeout]]
        except Exception as ex:
            print(ex)

    prod_1.join()
    prod_2.join()
    print(f"{prod_1.name} finished")
    print(f"{prod_2.name} finished")

# Listeners and Clients
# SimpleQueue
# JoinableQueue
