import multiprocessing as mp
import time
import os


def proc_func(kek=None, lol=None):
    for i in range(5):
        time.sleep(1)
        print(f'{i}: {kek}: {lol}: {mp.current_process().name}')
    return "OK"


def default_task():
    print('lol')


def res_callback(result):
    print("res_callback:", result)


if __name__ == '__main__':
    # my_pool = mp.Pool(processes=2, initializer=default_task)
    # ...
    # my_pool.close()
    # with mp.Pool(processes=2, initializer=default_task) as my_pool:

    my_pool = mp.Pool(processes=2, initializer=default_task)
    '''
    # print(my_pool.apply(proc_func, args=(110,)))
    # callback and errorcallback
    async_res = my_pool.apply_async(proc_func, callback=res_callback)

    async_res.wait()
    print("async_res:", async_res.get())
    '''
    '''
    # print(my_pool.map(proc_func, iterable=[1, 2, 3]))
    async_res = my_pool.starmap_async(
        proc_func,
        iterable=[[1, 2], [2, 3], [3, 4]],
        callback=res_callback
        )  # errorcallback

    async_res.wait()
    print("async_res:", async_res.get())
    '''

    my_pool.close()
    my_pool.join()

    print(f"{my_pool} finished")


# Manager
