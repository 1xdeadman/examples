def func_name():
    print('func_name()')


def func_2(param_1, param_2):
    print(param_1)
    print(param_2)


def func_3(param_1):
    print('func_3')
    result = 'идет ' + param_1 + " на комиссию"
    return result
    
def func_4():
    print('func_4')
    result = 'asdasd'
    return result, 123, "asd"

res = func_3("Михаил")
print(res)

res, res_2, kek = func_4()
print(res)
print(res_2)
print(kek)
