# https://docs.python.org/3/library/stdtypes.html#bytes
# https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range
# https://docs.python.org/3/library/stdtypes.html#binary-sequence-types-bytes-bytearray-memoryview
# https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset
# https://docs.python.org/3/library/stdtypes.html#mapping-types-dict
# https://docs.python.org/3/reference/simple_stmts.html#the-del-statement


# https://pythonworld.ru/tipy-dannyx-v-python/spiski-list-funkcii-i-metody-spiskov.html
# https://pythonworld.ru/tipy-dannyx-v-python/kortezhi-tuple.html
# https://pythonworld.ru/tipy-dannyx-v-python/mnozhestva-set-i-frozenset.html
# https://pythonworld.ru/tipy-dannyx-v-python/slovari-dict-funkcii-i-metody-slovarej.html
# https://pythonworld.ru/tipy-dannyx-v-python/bajty-bytes-i-bytearray.html

# list

list0 = []
list1 = list()
list2 = [1, 2, "text", True, 3.3]
list3 = list(list2)
list4 = [0] * 10
list5 = [x for x in range(50)]

'''
Списки позволяют обратиться к отдельному элементу с
помощью конструкции list_name[index].
index может изменяться от 0 до (количество элементов в списке - 1).
При обращении к list_name[0] - получим самый первый элемент списка.
Так же можно обращаться с отрицательными значениями:
list_name[-1] - получить последний элемент списка
'''
random_var = list3[1]  # обратиться к элементу списка по индексом 1.
random_var = list3[-1]  # получить предпоследний элемент списка
list3[0] = 11  # изменить первый элемент списка на значение 11
list3[0] += 11  # увеличить первый элемент списка на значение 11
list3[-1] = True  # изменить последний элемент списка на значение True
list3[2] += " text"
list3[2] = [10, 11, 12]  # изменить элемент с индексом 2 на список из трёх элементов.
del list3[0]  # удалить элемент из списка

d_ilst = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
d_ilst[0][0] = 123
print(d_ilst)
'''цикл для последовательного чтения всех элементов списка.
Переменная num на каждой итерации будет последовательно хранить значение
0го, 1го, 2го и т.д.
элемента списка.
'''

for num in list3:
    print("    ", type(num), num)
    num = 11
    # num = 11 # не позволяет изменять элемемент списка
for index, num in enumerate(list3):
    print(index, ": ", num)
    # num = 11 # не позволяет изменять элемемент списка
for index in range(len(list3)):
    print(index, ":", list3[index])
    list3[index] = 11

list10 = [1, 2, 3]

list10.append(1)  # добавить новый элемент в конец списка. [1,2,3,1]
list10.insert(2, 11)  # добавить новый элемент в список на позицию под индексом 2. Остальные элементы сдвинутся на +1. [1, 2, 11, 3, 1]
list10.insert(0, 1)  # добавить новый элемент в список на позицию под индексом 2. Остальные элементы сдвинутся на +1. [1, 1, 2, 11, 3, 1]
list10.insert(10, 10)  # Просто добавит элемент в конец списка, если максимальный индекс в списке меньше заданного. [1, 1, 2, 11, 3, 1, 10]
print("count(1):", list10.count(1))  # узать количество чисел 1 в списке
list3.reverse()  # интвертировать список
# list3.clear()  # очистить список
list3.remove(11)  # удалить самый первый элемент зо значением 11
# list2.sort()  # сортировать список. Работает, только если элементы списка поддерживают операцию < между собой

list0 = [0, 0, 0]
list5 = list0.copy()  # полное копирование списка. В ином случае переменные list5 и list0 будут обращаться к одному и тому же списку.
# list5 = list0      # если осуществить простое присваивание
list5[0] = 100000  # при изменении list5[0] изменится и значение list0[0], так как и list5 и list0 ссылаются на один и тот же список
list5 = [1, 2, 3]
list5.extend(list0)  # расширить список значениями из существующего [1,2,3,0,0,0]

# поиск в списке
if 1 in list2:
    print("1 in list2")
else:
    pass
if 1 not in list2:
    print("1 not in list2")


list6 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

list7 = list6[2:]
list7 = list6[:6]
list7 = list6[2:6]
list7 = list6[2:6:2]  # создание списка на основе уже существующего, начиная с 0го элемента, заканчивая 6, с шагом копируемых элементов 2

print(list7)

# dictionary

dict0 = {}
dict0 = dict()
dict0 = {
    0: "data0",
    1: "data1"
}

dict2 = {
    12: "data0",
    "dict": {1: "kek"},
    "list": [1, 2, 3, 4]
}


rand_var = dict0[0]  # обращение к элементу словаря
dict0[0] = 123              # запись в словарь. Как запись в существующий элемент,
dict0["perf_key"] = "data"  # так и создание нового
del dict0["perf_key"]   # удалить элемент словаря

# пробег по словарю
for key in dict2:  # получение ключей
    print(key)
for key in dict2.keys():  # получение ключей
    print(key)
for value in dict2.values():   # получение значений
    print(value)

for item in dict2.items():   # получение ключей и значений
    print(item)
for key, value in dict2.items():   # получение ключей и значений
    print(key, value)

if 'key0' in dict2:  # поиск по ключу словаря
    print('key0 in dict2')

dic10 = dict2.copy()
dict2.clear()
dict2.update(dict0)


# tuple
tuple1 = tuple()
tuple1 = ()
tuple0 = (0, 1, [1, 2, 3], "123123", 4)
print(tuple0.count(0))
tuple0.index(1)
len(tuple0[2])

# set
list0 = [1, 2, 3, 5, 5, 33, 33]
set0 = set(list0)
list0 = list(set0)
set1 = {1, 2, 3, 4, 5, 1, 1}
print("list0:", list0)
print("set0:", set0)
print("set1:", set1)

print(set1.issubset(set0))
print(set0.union(set1))
print(set0.difference(set1))
print(set0.intersection(set1))
set0.update(set1)
print(set0)

set0.remove(33)
print(set0)
tmp_set = set0.copy()
print(tmp_set)
tmp_set.clear()
print(tmp_set)
print(set0)
print(set0.pop())
print(set0)
set0.add(2222)
print(set0)

# bytearray and bytes

byte_array1 = bytearray([1, 2, 3, 4])
print('byte_array1', byte_array1)
byte_array2 = bytearray(10)
print('byte_array2', byte_array2)
byte_array3 = bytearray('text', encoding='utf-8')
print('byte_array3', byte_array3)

byte_array1.insert(1, 10)
tmp_byte_array = byte_array1.copy()
print('insert(1, 10):', byte_array1)
print('hex():', byte_array1.hex())
print('count(1):', byte_array1.count(1))
print('byte_array3.decode:', byte_array3.decode(encoding='utf-8'))
byte_array1.append(2)
print('append(2):', byte_array1)
print('pop:', byte_array1.pop())
tmp_byte_array.clear()
print('clear:', tmp_byte_array)

byte_array1.remove(1)
print('remove(1):', byte_array1)
print('index(2):', byte_array1.index(2))
byte_array1.extend(byte_array3)
print('extend:', byte_array1)
byte_array1.reverse()
print('reverse:', byte_array1)

print(byte_array1[0])
print(byte_array1)
byte_array1[2] = 55
print(byte_array1)