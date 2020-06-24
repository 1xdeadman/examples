# distutils: language=c++
# cython: language_level=3

from libcpp.vector cimport vector
from cython.parallel import prange, threadid

def start(int count):
    cdef int i
    cdef vector[long] res

    for i in prange(count, nogil=True):
        # res[i] = i ** 2
        res.push_back(i ** 2) 

    for i in range(res.size()):
        print(res[i])