class MyException(Exception):

    def __init__(self, message):
        self.message = message


def func(param):
    if type(param) is int:
        raise MyException("my message")


def test():
    try:
        raise MyException("lolkek")
    except MyException as ex:
        print(ex.message)


print(__name__)
if __name__ == "__main__":
    test()
