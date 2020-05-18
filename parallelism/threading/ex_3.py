# https://docs.python.org/3/library/threading.html

import threading
import time


# condition vars
cv = threading.Condition(lock=None)
flag = False


def is_flag():
    global flag
    return flag


def wait_condition():
    global cv
    global flag
    print("Wait!!!")
    # cv.acquire()
    # cv.release()
    with cv:
        # while not flag:
        #     cv.wait()
        # or
        cv.wait_for(predicate=is_flag)
    print("YESYESYES!!!")


def notify_condition():
    global cv
    global flag
    with cv:
        time.sleep(1)
        flag = True
        print("notify!!")
        cv.notify(2)
        # cv.notify_all()


def ex_3():
    print("ex_3")
    thread_waiter = threading.Thread(
        target=wait_condition,
        name="waiter"
    )
    thread_waiter_2 = threading.Thread(
        target=wait_condition,
        name="waiter"
    )
    thread_notifier = threading.Thread(
        target=notify_condition,
        name="notifier"
    )
    thread_waiter.start()
    thread_waiter_2.start()
    thread_notifier.start()

    thread_waiter.join()
    thread_waiter_2.join()
    thread_notifier.join()


if __name__ == "__main__":
    ex_3()

# semaphore
# event object
# timer object
# barrier object
