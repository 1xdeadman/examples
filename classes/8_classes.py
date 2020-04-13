#abstract nethods
# learning python, 5th edition, chapter 29
# https://www.python.org/dev/peps/pep-3119/S
# https://docs.python.org/3/library/abc.html


from abc import ABC, abstractmethod, abstractclassmethod

class MyAbstractClass(ABC):
    @abstractmethod
    def method(self):
        print("method")

    @classmethod
    @abstractmethod
    def class_method(cls):
        print("class_method")

class SubClass(MyAbstractClass):
    def method(self):
        print("method")

    @classmethod
    def class_method(cls):
        print("class_method")

#obj = MyAbstractClass()
obj = SubClass()
