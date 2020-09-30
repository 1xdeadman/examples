# instance/static/class methods


class MyClass:
    def __init__(self, x=100):
        if isinstance(x, int):
            self.x = x

    def imeth(self, x):
        print("instance:", [self, x])

    @staticmethod
    def smeth(x):
        print("static:", [x])
        if isinstance(x, str):
            try:
                x = int(x)
                return MyClass(x)
            except Exception as ex:
                print(ex)
        else:
            raise TypeError("x must be str")

    @classmethod
    def cmeth(cls, x):
        print("class:", [cls, x])
        if isinstance(x, str):
            try:
                x = int(x)
                return cls(x)
            except Exception as ex:
                print(ex)
        else:
            raise TypeError("x must be str")


print("\ninstance")
instance = MyClass()
instance.imeth(12)
instance.smeth("11")
instance.cmeth("13")
print("\nMyClass")
MyClass.imeth(instance, 1)
MyClass.smeth("3")
MyClass.cmeth("2")


class SubClass(MyClass):
    pass


print("\nSubClass")
print("static method:", SubClass.smeth("123"))
print("class method:", SubClass.cmeth("123"))
