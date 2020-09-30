# Cython style
# python -m cython -a .\ex_2.pyx



# variables
def func(double x):
    return x ** 2


def powm(double value, int pow_v, int mod):
    cdef int i
    for i in range(pow_v - 1):
        value *= value
        value %= mod
    return value


# functions
cdef double f(double x):
    return x ** 2 - x

cpdef double ff(double x):
    return x ** 2 - x


cpdef int return_val(int val):
    return val

cpdef int return_sum(int val_1, int val_2):
    return val_1 + val_2