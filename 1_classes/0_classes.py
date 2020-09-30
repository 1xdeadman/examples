"""
Мы можем создавать свои собственные типы объектов, навываемые классами.
Класс - структура данных, формальное описание того,
так объект должен хранить и обрабатывать данные.
Объект класса - отдельный объект, который следует правилам класса.
Например: класс - это общее представление компьютера,
а объект класса - это конкретно ваш компьютер.

В python функции, находящиеся в классе, называются методами, а переменные,
так же входящие в класс - атрибутами.

Мы можем создать для класса:
 - собственные методы,
 - атрибуты,
 - переопределить операнды, н-р =,+,-,*,/, чтобы сообщить интерпретатору,
   как ему следует выполнять подобные операции с объектами класса.
"""


"""
создание класса
"""


class my_random_class_name:
    # определим аттрибут класса и его дефолтное значение
    random_class_attr_1 = "attr data"

    def random_class_method_1(self):
        """
        Метод класса. Мы должны во всех нестатических методах класса указывать
        первым параметром self - ссылку на сам объект класса.
        """
        print("----", "random_class_method_1")
        random_var = 321
        # для работы с атрибутами объекта необходимо использовать self
        self.random_inst_attr_1 = 123 + random_var
        print(self.random_class_attr_1)

    def set_random_class_attr_1(self, rand_param_name):
        print("----", "random_class_method_2")
        self.random_inst_attr_1 = rand_param_name


# создадим объект класса
random_cls_obj_name_1 = my_random_class_name()
print("---- before:", random_cls_obj_name_1.random_class_attr_1)
random_cls_obj_name_1.random_class_method_1()
print("---- after:", random_cls_obj_name_1.random_class_attr_1)

print("\nreference:")
# мы можем создать сколько угодно объектов нашего класса,
# и каждый из них будет хранить свои собственные данные
random_cls_obj_name_2 = my_random_class_name()
random_cls_obj_name_1.random_class_attr_1 = 123
print("\n---- without ref:", random_cls_obj_name_1.random_class_attr_1,
      "!=", random_cls_obj_name_2.random_class_attr_1)
# однако, если сделать так:
random_cls_obj_name_2 = random_cls_obj_name_1
# то random_cls_obj_name_2 будет ссылаться на те же данные,
# что и random_cls_obj_name_1
print("---- before:", random_cls_obj_name_2.random_class_attr_1)
random_cls_obj_name_1.random_class_attr_1 = "puf"
print("---- after:", random_cls_obj_name_2.random_class_attr_1)

# каждая переменная - это ссылка на объект, хранящийся в памяти. Нет разницы,
# одна у нас переменная ссылается на объект, или несколько.
# Для удаления ссылки на объект применяется del
del random_cls_obj_name_1

# на самом деле, в python можно сделать так:
random_cls_obj_name_1 = my_random_class_name()
# добавим аттрибут, которого раньше не было у класса
random_cls_obj_name_1.new_attr = 123
print("\nnew_attr:", random_cls_obj_name_1.new_attr)
