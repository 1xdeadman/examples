class MyException(Exception):

    def __init__(self, message):
        self.message = message


def func(param):
    if type(param) is int:
        raise MyException("my exception's message")


def test():
    try:
        func(123)
    except MyException as ex:
        print(ex.message)


print("hello world")
test()
