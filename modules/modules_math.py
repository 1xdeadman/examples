# https://docs.python.org/3/library/math.html
# https://metanit.com/python/tutorial/6.2.php
# https://habr.com/ru/post/337260/
# https://habr.com/ru/post/112953/
import math
from colorama import Fore, Style


def compare(in_value_1, in_value_2):
    value_1 = str(in_value_1)
    value_2 = str(in_value_2)
    res_1 = ""
    res_2 = ""
    len_1 = len(value_1)
    len_2 = len(value_2)
    min_len = min(len_1, len_2)
    color = None
    for i in range(0, min_len):
        n = value_1[i]
        m = value_2[i]
        if n != m and color != Fore.RED:
            res_1 += Fore.RED
            res_2 += Fore.RED
            color = Fore.RED
        elif n == m and color != Fore.GREEN:
            res_1 += Fore.GREEN
            res_2 += Fore.GREEN
            color = Fore.GREEN
        res_1 += n
        res_2 += m

    print(res_1)
    print(res_2)
    print(Style.RESET_ALL)


num = 8
float_num = 2.5
power = 8
rad = 0.5
grad = 90
n = 16
n10 = 1000
base = 2

print("math.pow:", math.pow(num, power))
print("pow:", pow(num, power))
print("pow:", pow(num, power, 100))
elem = math.pow(131, 8)
compare(int(elem), int(131 ** 8))
compare(int(math.pow(45245, 12)), int(45245 ** 12))
compare(int(math.pow(452451, 12)), int(452451 ** 12))

# аналог a%b, но подходит для float
print("fmod:", math.fmod(5, 3))
print("fmod:", math.fmod(-1e-100, 1e100))
print("%:", -1e-100 % 1e100)

print("exp:", math.exp(n))  # e ** n

print("gcd:", math.gcd(n, grad))
print("abs:", math.fabs(-num))
print("sqrt:", math.sqrt(num))
print("ceil:", math.ceil(float_num))
print("floor:", math.floor(float_num))
print("factorial:", math.factorial(num))
print("degrees:", math.degrees(rad))
print("radians:", math.radians(grad))
print("cos:", math.cos(rad))
print("sin:", math.sin(rad))
print("tan:", math.tan(rad))
print("acos:", math.acos(rad))
print("asin:", math.asin(rad))
print("atan:", math.atan(rad))
print("log:", math.log(n, base))
print("log2:", math.log2(n))
print("log10:", math.log10(n10))
