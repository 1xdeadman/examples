'''
off docs - https://docs.python.org/3/library/pickle.html
quick guide - https://pythonworld.ru/moduli/modul-pickle.html
'''

import pickle


pickle.HIGHEST_PROTOCOL
pickle.DEFAULT_PROTOCOL


class MyClass:
    def __init__(self, lol=123, kek={1: "1", 2: "2"}):
        self.lol = lol
        self.kek = kek


def write_data():
    with open("TestData/db.pickle", 'wb') as file:
        obj = MyClass(lol=1)
        obj2 = MyClass(lol='asd')
        pickle.dump(obj, file, protocol=5)
        pickle.dump(obj2, file, protocol=5)


def read_data():
    with open("TestData/db.pickle", 'rb') as file:
        obj1 = pickle.load(file)
        obj2 = pickle.load(file)
    print(obj1.lol)
    print(obj2.lol)


def write_data_2():
    with open("TestData/db.pickle", 'wb') as file:
        obj = MyClass()
        pickler = pickle.Pickler(file)
        pickler.dump(obj)
        pickler.dump(obj)


def read_data_2():
    with open("TestData/db.pickle", 'rb') as file:
        pickler = pickle.Unpickler(file)
        print(pickler.load().__dict__)
        print(pickler.load().__dict__)
        # print(pickler.load().__dict__)


write_data_2()
read_data_2()

# pickle.PickleError
# pickle.PicklingError
# pickle.UnpicklingError
