# https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
# https://docs.python.org/3/tutorial/inputoutput.html#methods-of-file-objects
# https://docs.python.org/3/reference/compound_stmts.html#the-with-statement
# https://docs.python.org/3/library/functions.html#open
# https://pythonworld.ru/tipy-dannyx-v-python/fajly-rabota-s-fajlami.html


"""
режимы открытия файла:
'r'  - только чтение (default)
'w'  - только запись, существующий файл очищается
'x'  - только содание файла
'a'  - только дозапись в конец файла
'b'  - двоичный режим: 'rb', 'wb'
't'  - текстовый режим (стандартный)
'+'  - для чтения и записи : 'w+', 'w+b' | 'r+', 'r+b'
"""
# открытие файла, аргументы - путь до файла, режимы открытия, кодировка файла
file = open("../TestData/test", "r", encoding="utf-8")
print(file.read())  # читать весь файл целиком
# освобождаем ресурсы
file.close()

file = open("../TestData/test", "r", encoding="utf-8")
print(file.read(2))  # читать 2 символа
line = file.readline()  # считать строку файла до символа переноса строки(\n)
print(line)
lines = file.readlines()  # считать весь файл построчно
print(lines)
file.close()

with open("../TestData/test", "r") as file:
    print(file.read())

# чтение файла циклами

file = open("../TestData/test", "r")
line = file.readline()
while line:
    print(line)
    line = file.readline()
file.close()

file = open("../TestData/test", "r")
for line in file:
    print(line)
file.close()

# запись в файл
with open("../TestData/newtest", "w") as file:
    file.write("row1")
    file.write("row1")
    file.write("row1\n")
    file.writelines(["row2\n", "row3\n"])

# дозапись в файл
with open("../TestData/newtest", "a") as file:
    file.write("row1\n")
    file.write("row1\n")
    file.writelines(["row2\n", "row3\n"])

file = open("../TestData/test", "rb")
print(file.tell())
print(file.name)
print(file.seek(-2, 2))  # whence = Tuple[0, 1, 2]
file.close()
