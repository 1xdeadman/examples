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
show("uniform:", rnd.uniform, 10.0, 11.0)  # [A,B]
show("randrange:", rnd.randrange, 10, 60) # нижняя граница < верхней
show("randint:", rnd.randint, 10, 60) # нижняя граница <= верхней
show("getrandbits:", rnd.getrandbits, 100)  #
show("choice:", rnd.choice, [-10, -10, -20])  #
show("choices:", rnd.choices, population=list(range(1, -100, -2)), k=3)  #
show("sample:", rnd.sample, [1,2,3,4,5,6], k=6)  # k <= len(list)
show("shuffle:", my_shuffle, [1,2,3,4,5,6])
show("gauss:", rnd.gauss, mu=10, sigma=60) 
show("lognormvariate:", rnd.lognormvariate, mu=10, sigma=60)  
show("normalvariate:", rnd.normalvariate, mu=10, sigma=1) 
show("vonmisesvariate:", rnd.vonmisesvariate, mu=10, kappa=60) 
show("paretovariate:", rnd.paretovariate, alpha=10) 
show("weibullvariate:", rnd.weibullvariate, alpha=10, beta=60) 

import os

if(os.path.isdir("mem") == False):
    os.mkdir("mem")
print(os.path.isfile("files.py"))
os.rmdir("mem")
open("test","w") 
os.remove("test")