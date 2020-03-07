#print("123", "456", 789, sep="|")

print("123", end='\n')
print("456", end='|')
print("789")

for i in range(10):
    print(i, end=' ')
print()
for i in range(1, 10):
    print(i, end=' ')
print()

for i in range(1, 10, 3):
    print(i, end=' ')
print()


val_1 = 1
while val_1 < 10:
    val_1 += 1
    str_val_1 = str(val_1)
    print(str_val_1 + ": ", "while") # преобразование числа в строку

