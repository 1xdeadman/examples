# func decorators
# learning python, 5th edition, chapter 39
# https://tproger.ru/translations/demystifying-decorators-in-python/
# https://habr.com/ru/post/141411/
import time
from functools import wraps, update_wrapper


class cls_decorator:
    def __init__(self, func):
        self.calls = 0
        self.stored_func = func
        print("init")

    def __call__(self, *args, **kwargs):
        self.calls += 1
        print("count:", self.calls)
        return self.stored_func(*args, **kwargs)


def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print("time:", end - start)
        return res
    return wrapper


# @my_decorator
@cls_decorator
def my_func(kek, lol):
    print("my_func():", kek, lol)
    time.sleep(1.0)


# my_func = my_decorator(my_func)

my_func(11, 22)
my_func(11, 33)


class csl_dec(object):
    @classmethod
    def my_dec(cls, decorated):
        @wraps(decorated)
        def wrapper(*args, **kwargs):
            start = time.time()
            print("before:")
            res = decorated(*args, **kwargs)
            print("after")
            end = time.time()
            print("time:", end - start)
            return res
        return wrapper


class kek:
    @csl_dec.my_dec
    def keko(self):
        print("keklo")


@csl_dec.my_dec
def ff(kek, lol):
    print("my_func():", kek, lol)


ff(1, 2)

kk = kek()
kk.keko()
kk.keko()
