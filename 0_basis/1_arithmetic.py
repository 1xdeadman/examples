# основы арифметические операций
# https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex
# https://metanit.com/python/tutorial/2.3.php


# основные арифметические операци над числами (int/float)
print("Числа")
val_1 = 1
val_2 = 2

print(val_1, "+", val_2, "=", val_1 + val_2)  # операция сложения двух чисел
print(val_1, "-", val_2, "=", val_1 - val_2)  # операция вычитания двух чисел
print(val_1, "*", val_2, "=", val_1 * val_2)  # операция умножения двух чисел
print(val_1, "/", val_2, "=", val_1 / val_2)  # деление двух чисел
print(val_1, "//", val_2, "=", val_1 // val_2)  # целочисленное деление
print(val_1, "**", val_2, "=", val_1 ** val_2)  # возведение числа val_1 в степень val_2
print(val_1, "%", val_2, "=", val_1 % val_2)  # остаток от деления числа val_1 на число val_2
# etc...

# результат операции можно записывать в другую переменную:
val_3 = val_1 + val_2
print("val_3:", val_3)

# операции можно производить и над литералами:
val_3 = 1 + 2

# операции можно производить над литералами и переменными:
val_3 = val_1 + 2

# можно строить цепочки из операций
val_3 = 1 + 2 + 3 + val_1 * 4 / 6

# для определения специфической последовательности операций используются скобки ()
val_3 = (1 + 2) * (1 + 2)

# сокращенные операции
val_3 += 1  # прибавление 1 к val_3 и запись в val_3. Аналог val_3 = val_3 + 1
val_3 -= 1  # вычитание 1 из val_3 и запись в val_3. Аналог val_3 = val_3 - 1
val_3 *= 1  # etc ...
val_3 /= 1
val_3 *= 1
val_3 //= 1
val_3 **= 1
val_3 %= 1

print(val_1, "<", val_2, "=", val_1 < val_2)
print(val_1, ">", val_2, "=",  val_1 > val_2)
print(val_1, "==", val_2, "=", val_1 == val_2)
print(val_1, ">=", val_2, "=", val_1 >= val_2)
print(val_1, "<=", val_2, "=", val_1 <= val_2)
print(val_1, "!=", val_2, "=", val_1 != val_2)


print('\n\nоперации над строками (string)')
# операции над строками (string)

# Для строк также определены некоторые операции, но имеющие несколько
# иной смысл, отдаленно похожый по смыслу на изначальный

val_1 = "left"
val_2 = "right"

print(val_1, "+", val_2, "=", val_1 + val_2)
print('"', val_1, '" *', 8, "=", (" " + val_1 + " ") * 8)

print(val_1, "<", val_2, "=", val_1 < val_2)
print(val_1, ">", val_2, "=",  val_1 > val_2)
print(val_1, "==", val_2, "=", val_1 == val_2)
print(val_1, ">=", val_2, "=", val_1 >= val_2)
print(val_1, "<=", val_2, "=", val_1 <= val_2)
print(val_1, "!=", val_2, "=", val_1 != val_2)
