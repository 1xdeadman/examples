# learning python, 5th edition, chapter 14
# https://docs.python.org/3/tutorial/classes.html#iterators
# https://habr.com/ru/post/337314/
# https://docs.python.org/3/library/collections.abc.html

from collections.abc import Iterable, Iterator

string = "abc"
print("for loop:")
for symbol in enumerate(string):
    print(symbol)

print("iterators")
iterator1 = iter(string)  # string.__iter__()
iterator2 = iter(string)
print("iterator1:", iterator1)
print("iterator2:", iterator2)
print("next(1):", next(iterator1))  # iterator1.__next__()
print("next(1):", next(iterator1))
print("next(2):", next(iterator2))
print("next(2):", next(iterator2))
print("next(2):", next(iterator2))
print("next(1):", next(iterator1))


class MyData(Iterator, Iterable):
    def __init__(self, data):
        self._data = data
        self._index = -1

    def __iter__(self):
        return MyClassEvenIndexIterator(self._data)  # self

    def __next__(self):
        if self._index + 1 == len(self._data):
            self._index = -1
            raise StopIteration
        self._index = self._index + 1
        return self._data[self._index]

    def __getitem__(self, index):
        return self._data[index]

    def __setitem__(self, index, value):
        self._data[index] = value


class MyClassEvenIndexIterator(Iterator):
    def __init__(self, data):
        self._data = data
        self._index = -1

    def __next__(self):
        if self._index + 1 == len(self._data):
            self._index = -1
            raise StopIteration
        self._index = self._index + 1
        return self._data[self._index]


data = MyData([1, 2, 3, 4, 10, 20, 30, 40])

for elem in data:
    print(elem)
for elem in data:
    print(elem)

iterator = iter(data)
data[0] = 1010
print(next(iterator))
