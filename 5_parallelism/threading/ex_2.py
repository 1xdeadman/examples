# https://docs.python.org/3/library/threading.html

import threading
import time


def show_threads_info():
    print(f"active threads: {threading.active_count()}")
    print(f"main thread: {threading.main_thread()}")
    print("threads list: ")
    for thread in threading.enumerate():
        print("--", thread)
    print()
    print("stack_size: ", threading.stack_size())


def show_cur_thread_info():
    print(f"current_thread: {threading.current_thread()}")
    print(f"cur_thread_id: {threading.get_ident()}")


my_locker = threading.Lock()
my_rec_locker = threading.RLock()
# create local thread's variable
thread_local_data = threading.local()

common_data = "common"


def l_print_blocking(message: str):
    my_locker.acquire()
    print(message)
    my_locker.release()


def l_print_nonblocking(message: str):
    time.sleep(0.2)
    if my_locker.acquire(blocking=False) is True:
        print(message)
        my_locker.release()
    else:
        return False
    return True


def l_print_timeout(message: str):
    time.sleep(0.2)
    if my_locker.acquire(blocking=True, timeout=0.1) is True:
        print(message)

        my_locker.release()
    else:
        return False
    return True


def l_print_common_data(message: str):
    global common_data
    my_locker.acquire()
    time.sleep(1)
    common_data += ' ' + message
    print(common_data)
    my_locker.release()
    time.sleep(0.01)


def l_print_noncommon_data(message: str):
    global thread_local_data
    time.sleep(1)
    if 'x' not in thread_local_data.__dict__:
        thread_local_data.x = "non common"
    thread_local_data.x += ' ' + message
    local_var = 42
    my_locker.acquire()
    print(thread_local_data.x)
    my_locker.release()


def r_print_common_data(message: str):
    global common_data

    my_rec_locker.acquire()

    time.sleep(1)
    common_data += ' ' + message
    print(common_data)

    my_rec_locker.acquire()
    print("internal lock!")
    my_rec_locker.release()

    my_rec_locker.release()
    time.sleep(0.01)


def thread_func(func, iter_count, lol: str):
    for i in range(iter_count):
        # time.sleep(1)
        func(f"{i}: {threading.get_ident()}")


def create_new_thread(func, count, thread_name=None):
    new_thread = threading.Thread(
        target=thread_func,
        name=thread_name,
        args=(func, count),
        kwargs={"lol": "asd"}
    )
    return new_thread


def ex_2():
    print("ex_2")
    # show_cur_thread_info()
    thread_lol = create_new_thread(l_print_noncommon_data, 10, "lol")
    thread_kek = create_new_thread(l_print_noncommon_data, 10, "kek")
    # print(f"thread_lol is started: {thread_lol.is_alive()}")
    thread_lol.start()
    thread_kek.start()
    # print(f"thread_lol is started: {thread_lol.is_alive()}")
    # print(f"thread_lol native_id is: {thread_lol.native_id}")
    # show_threads_info()
    thread_lol.join()
    thread_kek.join()


if __name__ == "__main__":
    ex_2()
