def func_name():
    print('func_name()')

def func_2(param_1:int, param_2=123):
    print(param_1)
    print(param_2)
    return 1, 12, 33, "asdsa"


def func_3(param_1):
    print('func_3')
    result = 'идет ' + param_1 + " на комиссию"
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


if __name__ == "__main__":
    ff(1,2,3,5)
    ff_kw(aza=1,lol=2,kek=3,bup=5)