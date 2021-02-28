"""
 https://docs.python.org/3/reference/compound_stmts.html#the-for-statement
 https://docs.python.org/3/reference/compound_stmts.html#the-while-statement
 https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops
 https://docs.python.org/3/reference/simple_stmts.html#the-break-statement
 https://docs.python.org/3/reference/simple_stmts.html#the-continue-statement
 https://pythonworld.ru/osnovy/cikly-for-i-while-operatory-break-i-continue-volshebnoe-slovo-else.html
Циклы предназначены для выполнения повторяющихся
последовательностей команд.
"""
# циклы for
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

for i in range(10):
    print(i, end=' ')
    break

for i in range(10):
    print(i, end=' ')
    break
else:
    print('without break')

# циклы while
val_1 = 1
while val_1 < 10:
    val_1 += 1
    if val_1 == 2:
        continue
    str_val_1 = str(val_1)
    print(str_val_1 + ": ", "while")  # преобразование числа в строку



