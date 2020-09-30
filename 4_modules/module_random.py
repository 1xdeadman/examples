# https://docs.python.org/3/library/random.html

import random as rnd


def show(message, func, *args, **kvarg):
    print(message)
    for _ in range(20):
        print(func(*args, **kvarg), end=" ")
    print("\n\n")


def my_shuffle(my_list):
    rnd.shuffle(my_list)
    return my_list


show("random:", rnd.random)  # [0,1]
show("uniform:", rnd.uniform, 10.0, 20.0)  # [A,B]
show("randrange:", rnd.randrange, 10, 60)  # нижняя граница < верхней
show("randint:", rnd.randint, 10, 60)  # нижняя граница <= верхней
show("getrandbits:", rnd.getrandbits, 100)  # сгенерировать случайные 100 бит
show("choice:", rnd.choice, [-10, -10, -20])  # выбрать случайный элемент
show("choices:", rnd.choices, population=[1, 2, 3, 4, 5, 6, 7, 8, 9, 0], k=3)
show("sample:", rnd.sample, [1, 2, 3, 4, 5, 6], k=6)  # k <= len(list)
show("shuffle:", my_shuffle, [1, 2, 3, 4, 5, 6])
show("gauss:", rnd.gauss, mu=10, sigma=60)
show("lognormvariate:", rnd.lognormvariate, mu=10, sigma=60)
show("normalvariate:", rnd.normalvariate, mu=10, sigma=20)
show("vonmisesvariate:", rnd.vonmisesvariate, mu=10, kappa=60)
show("paretovariate:", rnd.paretovariate, alpha=10)
show("weibullvariate:", rnd.weibullvariate, alpha=10, beta=60)


def gen_key_1(key_len):
    key = [i for i in range(1, key_len + 1)]
    rnd.shuffle(key)
    return key


def gen_key_2(key_len):
    key = []
    key_values = []
    for i in range(1, key_len + 1):
        key_values.append(i)
    while(True):
        key_id = rnd.randrange(0, len(key_values))
        key_elem = key_values[key_id]
        if key_elem not in key:
            del key_values[key_id]
            key.append(key_elem)
            if len(key) == key_len:
                break
        else:
            print("error!")
    return key


print(gen_key_2(10))
