"""
Циклы предназначены для выполнения повторяющихся
последовательностей команд.
"""

for i in range(10):
    print(i, end=' ')
print()
for i in range(1, 10):
    print(i, end=' ')
print()

for i in range(1, 10, 3):
    print(i, end=' ')
print()

for i in range(-10, 10, 1):
    print(i)

val_1 = 1
while val_1 < 10:
    val_1 += 1
    if val_1 == 2:
        continue
    str_val_1 = str(val_1)
    print(str_val_1 + ": ", "while")  # преобразование числа в строку
