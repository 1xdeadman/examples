"""
Организовываете взаимодействие с пользователем в этом модуле.
Пример программы.
Пример не имеет с вашим заданием ничего общего. =P
"""
import db
import notes
import security


key = b''


def gen_new_key():
    global key
    key = security.gen_secret_key()
    print("ключ сгенерирован: {0}".format(key))


def encrypt_text():
    global key
    text = input("Введите шифруемый текст: ")
    ciphertext = security.encrypt(text.encode(encoding='utf-8'), key)
    print("шифротекст:", "'{0}'".format(ciphertext))


commands = [
    ["Сгенерировать новый ключ:", "gen", gen_new_key],
    ["Зашифровать текст:", "enc", encrypt_text]
]


def use_command(command: str):
    global commands
    for com in commands:
        if command in com:
            com[2]()
            return
    print("Не найдена команда!")


def show_menu():
    print()
    print("выберите команду:")
    for com in commands:
        print("   ", com[0], com[1])


if __name__ == "__main__":
    while True:
        show_menu()
        user_input = input("Ваш выбор: ")
        use_command(user_input)
