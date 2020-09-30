"""
конструкторы/деструкторы
Мы можем определить специальные методы,
которые будут вызываться каждый раз при создании/удалении объекта.
Конструктор создается как метод с именем __init__
Деструктор - как метод с названием __del__
"""


class ConstructionCls:

    def __init__(self):
        """
        вызывается в момент создания объекта класса.
        Мы можем создавать конструкторы с произвольным количеством параметров:
        def __init__(self, param_1, random_param_1):
            pass
        но тогда при создании объекта необходимо передавать аргументы
        в его конструктор:
        rand_name_1 = ConstructionCls("text", 123)
        """
        print("----:", "construction")
        # мы можем определить атрибут класса прямо в конструкторе
        self.random_attr_1 = 123

    def __del__(self):
        """
        вызывается в момент уничтожения объекта класса.
        Объект класса уничтожается в тот момент, когда объект класса более
        недостижим из кода программы.
        """
        print("----:", "destructor")


def easy():
    rand_name_1 = ConstructionCls()
    print("kek")
    print(rand_name_1.random_attr_1)


def normal():
    rand_name_1 = ConstructionCls()
    del rand_name_1  # удалим ссылку на объект
    print("kek")


def hard():
    rand_name_1 = ConstructionCls()
    rand_name_2 = rand_name_1
    del rand_name_1
    # del rand_name_2
    print("random text")
    # print(rand_name_2.random_attr_1)


def decor(text, func):
    print("\n" + text)
    print("###before###")
    func()
    print("###after###")


decor("easy", easy)
decor("normal", normal)
decor("hard", hard)
