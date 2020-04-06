class MyClass:
    def __init__(self):
        self.pub_attr = 123
        # скрываем атрибут извне этого класса
        self.__val = 0  
        # скрываем атрибут извне этого класса и его потомков
        self._val = 0  

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

obj.val = "123"
obj.val = 123
print(obj.val)