"""
Наследование
"""

class Parent:
    def __init__(self):
        self.val = 123
        self.__priv = "text"
        self._prot = "kek"

    def parent_method(self):
        print("my method")

class Child(Parent):
    def method(self):
        print(self._prot)
        # print(self._Parent__priv )
        print(self.val)

obj1 = Child()
obj1.method()
obj1.val = 123
obj1.parent_method()


class ChildNext(Parent):
    def __init__(self):
        super().__init__()
        self.kek = 1

obj1 = ChildNext()
print(obj1.val)
