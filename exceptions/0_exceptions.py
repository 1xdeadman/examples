str_number = input("input number:")

try:
    number = int(str_number)
    print("ok!")
except ValueError as err:
    print("ValueError:", err)
except TypeError as err:
    print("TypeError:", err)
except Exception as err:
    print("Exception:", err)
finally:
    print("Завершение блока try...except")
print("ok!")

'''
try:
    number = int("-10")
    if number < 0:
        raise Exception("Число не должно быть отрицальным")
except ValueError as err:
    print("ValueError:", err)
except Exception as err:
    print("Exception:", err)
'''
