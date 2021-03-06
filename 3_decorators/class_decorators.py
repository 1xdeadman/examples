# class decorators
# learning python, 5th edition, chapter 39


def my_decorator(cls):
    class Wrapper:
        def __init__(self, *args):
            print("Wrapper.init")
            self.wrapped = cls(*args)

        def my_move(self):
            print("Wrapper.my_move")
            return self.wrapped.my_move()
    return Wrapper


@my_decorator
class C:
    def __init__(self, x, y):
        print("C.__init__")
        self.attr = 'spam'

    def my_move(self):
        print("C.my_move")
        return 1


x1 = C(6, 7)
x2 = C(11, 12)
print(x1.attr)
print(x2.attr)

print(type(x1))
print(x1.my_move())
