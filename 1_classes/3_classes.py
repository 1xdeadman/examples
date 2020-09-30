"""
перегрузка операторов.
Для каждого класса можно перегрузить отдельный оператор.
Например, можно определить реультат выполнения сложения экземпляра
вашего класса с другим экземпляром. Или вычитания. Или сравнения. И так далее.
Другим экземпляром может быть как экземпляр этого класса, так и другого.
"""


class MyClass:
    def __init__(self, value=0):
        self.data = value

    def __add__(self, other):
        # 123 + 321
        # MyClass + X
        return MyClass(self.data + other.data)

    def __sub__(self, other):
        # MyClass - X
        return MyClass(self.data - other.data)

    def __mul__(self, other):
        # MyClass * X
        return MyClass(self.data * other.data)

    def __truediv__(self, other):
        # MyClass / X
        return MyClass(self.data / other.data)

    def __floordiv__(self, other):
        # MyClass // X
        return MyClass(self.data // other.data)

    def __mod__(self, other):
        return MyClass(self.data % other.data)

    def __str__(self):
        # str(MyClass)
        return '[MyClass: {0}]'.format(self.data)

    def __lt__(self, other):
        # MyClass < X
        return self.data < other.data


rand_1 = MyClass(2)
rand_2 = MyClass(4)
rand_3 = rand_1 / rand_2

print(rand_3)
print(rand_1 < rand_2)
