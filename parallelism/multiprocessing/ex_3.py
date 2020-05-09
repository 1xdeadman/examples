# https://docs.python.org/3/library/threading.html

import multiprocessing as mp
import time


def wait_condition(cv, flag):
    with cv:
        cv.wait_for(predicate=lambda: flag.value)
    print("YESYESYES!!!")


def notify_condition(cv, flag):
    with cv:
        time.sleep(1)
        flag.value = True
        print("notify!!")
        cv.notify(1)


def ex_3():
    print("ex_3")
    cv = mp.Condition(lock=None)
    flag = mp.Value(typecode_or_type='b')
    # (typecode_or_type, *args, lock=True)
    waiter = mp.Process(
        target=wait_condition,
        name="waiter",
        kwargs={"cv": cv, "flag": flag}
    )
    notifier = mp.Process(
        target=notify_condition,
        name="notifier",
        kwargs={"cv": cv, "flag": flag}
    )
    waiter.start()
    notifier.start()

    waiter.join()
    notifier.join()


if __name__ == "__main__":
    ex_3()

# semaphore
# event object
# timer object
# barrier object
# Array
