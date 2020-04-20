print("hello")
flag = True
while flag:
    val_1 = int(input("input val_1:"))
    val_2 = int(input("input val_1:"))

    command = input("input command:")

    if command == "+":
        print(val_1, "+", val_2, "=", val_1 + val_2)
    elif command == "*":
        print(val_1, "*", val_2, "=", val_1 * val_2)
    elif command == "-":
        print(val_1, "-", val_2, "=", val_1 - val_2)
    elif command == "/":
        print(val_1, "/", val_2, "=", val_1 / val_2)

    for i in range(3):
        command = input("Continue?(Y/N)")
        if command == 'N':
            flag = False
            break
        elif command == 'Y':
            flag = True
            break
        if i == 2:
            print("Команда была три раза введена неверно!\
                   Выполняется выход из программы...")
            flag = False
        print("Введена неправильная команда!")
print("exit")
