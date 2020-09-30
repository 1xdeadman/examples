# https://docs.python.org/3/library/threading.html
'''
The Thread class represents an activity that isrun in a separate thread of control.
There are two ways to specify the activity:
by passing a callable object to the constructor, or by overriding the run() method in a subclass.
No other methods (except for the constructor) should be overridden in a subclass.
In other words, only override the __init__() and run() methods of this class.
'''


import threading
import time

print("lol will be with proccess")


def show_threads_info():
    print(f"active threads: {threading.active_count()}")
    print(f"main thread: {threading.main_thread()}")
    print("threads list: ")
    for thread in threading.enumerate():
        print("--", thread)
    print()


def show_cur_thread_info():
    print(f"current_thread: {threading.current_thread()}")
    print(f"cur_thread_id: {threading.get_ident()}")


def thread_func(lol: str):
    for i in range(10):
        time.sleep(1)
        print(f"{i}: {threading.get_ident()}")


def ex_1():
    print("ex_1")
    thread_lol = threading.Thread(
        target=thread_func,
        name="lol",
        kwargs={"lol": "kek"}
    )
    print(f"thread_lol is started: {thread_lol.is_alive()}")
    thread_lol.start()
    print(f"thread_lol is started: {thread_lol.is_alive()}")
    thread_lol.join()
    print("exit")
    # or
    # thread_lol.join(5.0)
    # print(f"thread_lol is started: {thread_lol.is_alive()}")


if __name__ == "__main__":
    ex_1()
