# learning python, 5th edition, chapter 16


def func_1(elem: int) -> int:
    print('func_name()1')
    return "as"


def func_2(param_1: int, param_2=123):
    print(param_1)
    print(param_2)
    return 1, 12, 33, "asdsa"


def func_3(param_1):
    print('func_3')
    result = param_1 + ' идет на комиссию'
    return result


def func_4():
    print('func_4')
    result = 'asdasd'
    return result, 123, "asd"


def ff(*args):
    for arg in args:
        print(arg)


def ff_kw(**kwargs):
    print(kwargs['aza'])
    for arg in kwargs.items():
        print(arg)


def ff_all(*args, **kwargs):
    for arg in args:
        print(arg)
    for arg in kwargs.items():
        print(arg)


my_elem = 0


def global_var_func():
    global my_elem
    my_elem = 4


if __name__ == "__main__":
    print(func_1(1))
    # ff(1,2,3,5)
    # ff_kw(aza=1,lol=2,kek=3,bup=5)
    ff_all(1, 2, 3, 4, aza=123)
    global_var_func()
    print(my_elem)
