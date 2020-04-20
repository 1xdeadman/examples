# https://docs.python.org/3/library/math.html
# https://metanit.com/python/tutorial/6.2.php
# https://habr.com/ru/post/337260/
# https://habr.com/ru/post/112953/
import math


num = 8
float_num = 2.5
power = 8
rad = 0.5
grad = 90
n = 16
n10 = 1000
base = 2

print("math.pow:", math.pow(num, power))  # проблема точности после 16го знака
print("pow:", pow(num, power))
print("pow:", pow(num, power, 100))

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
