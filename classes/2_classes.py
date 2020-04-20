"""
важное уточнение - есть два типа атрибутов:
1) атрибуты класса
2) атрибуты объекта
Атрибуты класса изначально разделяются между всеми объектами класса.
Атрибуты объекта изначально уникальны для каждого из объектов класса.

Вспомним про списки:
"""


class my_random_class:
    class_attr_1 = []  # атрибут класса

    def __init__(self):
        self.random_inst_attr_1 = []  # атрибут объекта


# создадим два объекта класса
obj1 = my_random_class()
obj2 = my_random_class()

# изменим значения в первом
obj1.class_attr_1.append(1)
obj1.random_inst_attr_1.append(1)

# выведем значения второго
print(obj2.class_attr_1)  # [1]
print(obj2.random_inst_attr_1)  # []

# однако если атрибуту class_attr_1 первого
# объекта присвоить новый список:
obj1.class_attr_1 = [1, 2, 3]
obj1.class_attr_1.append(4)

# снова выведем значения второго
print(obj2.class_attr_1)  # все еще [1]
