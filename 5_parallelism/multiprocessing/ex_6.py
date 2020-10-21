import multiprocessing as mp
import time


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
    # my_pool.join()

    with mp.Pool(processes=2, initializer=default_task) as my_pool:
        pass

        # # single task
        # print(my_pool.apply(proc_func, args=(110,)))
        # print(my_pool.apply(proc_func, args=(111,)))

        # start async single task
        # use callback and errorcallback
        # async_res = my_pool.apply_async(proc_func, callback=res_callback)
        # async_res = my_pool.apply_async(proc_func, callback=res_callback)
        # async_res = my_pool.apply_async(proc_func, callback=res_callback)
        # async_res.wait()  # [timeout]
        # print("async_res:", async_res.get())  # [timeout]

        # start few tasks
        # print(my_pool.map(proc_func, iterable=[1, 2, 3]))
        async_res = my_pool.map_async(
            proc_func,
            iterable=[1, 2, 3],
            callback=res_callback)
        async_res.wait()
        # # start tasks with few params
        # async_res = my_pool.starmap_async(
        #     proc_func_2d,
        #     iterable=[[1, 2], [2, 3], [3, 4]],
        #     callback=res_callback
        #     )  # errorcallback
        # # async_res.wait()
        # print("async_res:", async_res.get())

    print(f"{my_pool} finished")


# Manager
