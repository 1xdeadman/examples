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
    global my_locker
    my_locker.acquire()
    print(message)
    my_locker.release()


def l_print_nonblocking(message: str):
    global my_locker
    if my_locker.acquire(blocking=False) is True:
        time.sleep(0.2)
        print(message)
        my_locker.release()
    else:
        return False
    return True


def l_print_timeout(message: str):
    global my_locker
    if my_locker.acquire(blocking=True, timeout=0.1) is True:
        time.sleep(0.2)
        print(message)

        my_locker.release()
    else:
        return False
    return True


def l_print_common_data(message: str):
    global my_locker
    global common_data
    my_locker.acquire()
    common_data += ' ' + message
    print(common_data.x)
    my_locker.release()


def l_print_noncommon_data(message: str):
    global my_locker
    global thread_local_data
    if 'x' not in thread_local_data.__dict__:
        thread_local_data.x = "non common"
    my_locker.acquire()
    thread_local_data.x += ' ' + message
    local_var = 42
    print(thread_local_data.x)
    my_locker.release()


def thread_func(lol: str):
    for i in range(10):
        time.sleep(1)
        l_print_blocking(f"{i}: {threading.get_ident()}")


def create_new_thread(thread_name=None):
    new_thread = threading.Thread(
        target=thread_func,
        name=thread_name,
        kwargs={"lol": "asd"}
    )
    return new_thread


def ex_2():
    print("ex_2")
    # show_cur_thread_info()
    thread_lol = create_new_thread("lol")
    thread_kek = create_new_thread("kek")
    print(f"thread_lol is started: {thread_lol.is_alive()}")
    thread_lol.start()
    thread_kek.start()
    print(f"thread_lol is started: {thread_lol.is_alive()}")
    print(f"thread_lol native_id is: {thread_lol.native_id}")
    show_threads_info()
    thread_lol.join()
    thread_kek.join()


if __name__ == "__main__":
    ex_2()
