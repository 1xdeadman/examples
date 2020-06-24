# distutils: language=c++
# cython: language_level=3

from libcpp.vector cimport vector
from libc.math cimport sin

from libcpp.string cimport string
import json

cpdef double double_sin(double x):
    return sin(x * x)


#def save(char* filename, int val):
def save(string filename, int val):
    with open(filename, 'w') as file2:
        # file2.write(str(val))
        json.dump( {"val": val}, file2)


def func(int size):
    cdef vector[long] vec
    vec.resize(size)
    cdef int i
    for i in range(size):
        vec[i] = i + 2
    vec.push_back(0)
    print(vec.size())
    return vec

cdef struct MyStruct:
    int val_1
    float val_2

cpdef cppclass MyClass:
    int val
    MyClass(int new_val):
        val = new_val
    int get_val():
        return val


cdef class MyClass2:
    cdef int val

    def __init__(self, int new_val):
        self.val = new_val

    cpdef int get_val(self):
        return self.val

