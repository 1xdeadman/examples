# публичные и непубличные атрибуты
# свойства и сеттеры

class MyClass:
    def __init__(self):
        self.pub_attr = 123
        # 'скрываем' атрибут извне этого класса и его потомков
        self.__val = 1
        # 'скрываем' атрибут извне этого класса. Все еще доступны.
        self._val = 2

    def set_method(self, new_val):
        if type(new_val) is int:
            self.__val = new_val

    def get_method(self):
        return self.__val

    @property
    def val(self):
        """
        реализуем свойство для получения значения из объекта
        """
        return self.__val

    @val.setter
    def val(self, new_val):
        """
        реализуем сеттер для записи значения в объекта
        """
        if type(new_val) is int:
            self.__val = new_val
        else:
            print("Недопустимый тип")


rnd = MyClass()
rnd.set_method(1)
rnd.get_method()

obj = MyClass()

print('exemple 1')
obj.val = "qwe"
obj.val = 22
print(obj.val)

print('exemple 2')
"""в python нет модификаторов доступа в привычном для c++, C#, Java и
других языков смысле. Здесь они скорее соглашения между разработчиками,
что эти данные ограничены для использования. Однако мы все еще можем их
использовать!
"""
print(obj.pub_attr)
print(obj._MyClass__val)
print(obj._val)
