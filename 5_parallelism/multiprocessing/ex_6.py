import multiprocessing as mp
import time


def proc_func(kek=None, lol=None):
    for i in range(5):
        time.sleep(1)
        print(f'{i}: {kek}: {lol}: {mp.current_process().name}')
    return "DATA"


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

        # single task
        # print(my_pool.apply(proc_func, args=(110,)))
        # print(my_pool.apply(proc_func, args=(111,)))

        # start async single task
        # use callback and errorcallback
        '''
        async_res1 = my_pool.apply_async(proc_func, args=(1,), callback=res_callback)
        async_res2 = my_pool.apply_async(proc_func, args=(2,), callback=res_callback)
        async_res3 = my_pool.apply_async(proc_func, args=(3,), callback=res_callback)
        print("main!")
        async_res1.wait()  # [timeout]
        async_res2.wait()
        async_res3.wait()
        print("async_res:", async_res1.get())  # [timeout]
        '''

        '''
        # start few tasks
        res = my_pool.map(proc_func, iterable=[1, 2, 3])
        print(res)
        async_res = my_pool.map_async(
            proc_func,
            iterable=[(1, 2), (2, 3), (3, 4)],
            callback=res_callback)
        async_res.wait()
        '''
        # start tasks with few params
        async_res = my_pool.starmap_async(
            proc_func,
            iterable=[[1, 2], [2, 3], [3, 4]],
            callback=res_callback
            )  # errorcallback
        async_res.wait()
        print("async_res:", async_res.get())

    print(f"{my_pool} finished")


# Manager
