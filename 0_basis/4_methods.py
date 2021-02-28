"""
https://docs.python.org/3/library/stdtypes.html
https://pythonworld.ru/tipy-dannyx-v-python/chisla-int-float-complex.html
https://pythonworld.ru/tipy-dannyx-v-python/stroki-funkcii-i-metody-strok.html
https://metanit.com/python/tutorial/5.2.php
Каждый объект имеет свои собственные методы, которые можно назвать функциями, привязанными к конкретному объекту.
Эти методы вызываются через символ . после имени объекта, и имеют доступ к внутреннему состоянию этого объекта.
"""


# int
value = 1
print(value.bit_length())  # число бит, используемых для для редставления числа,без знака и впередиидущих 0
print(value.to_bytes(10, byteorder='big'))  # возвращает байтовое представление числа, записанное в 10 байт
print(int.from_bytes(value.to_bytes(10, byteorder='big'), byteorder='big'))  # возвращает число из массива байт


# bool
value = True
print('bool:', value.bit_length())
print('bool:', value.to_bytes(length=1, byteorder='big'))


# str
str_row = "   tExT TeXt tExT   "

print(str_row[3])

new_str = str_row.lower()
new_str = str_row.upper()

new_str = str_row.strip(" t")
new_str = str_row.split("ExT")
new_str = str_row.replace(" ", "|")
str_row = "asdasd12312312"
print("isspace:", str_row.isspace())
print("isnumeric:", str_row.isnumeric())
print("isalpha:", str_row.isalpha())
print("capitalize:", str_row.capitalize())
print("find:", str_row.find('123'))
byte_row = str_row.encode(encoding='utf-8')
print("encode:", byte_row)
print("decode:", byte_row.decode(encoding='utf-8'))

val = 123
