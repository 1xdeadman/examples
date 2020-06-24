# python setup.py install
# pip install Cython
# https://cython.readthedocs.io/
# http://docs.cython.org/en/latest/src/tutorial/appendix.html
# python setup.py build_ext --inplace

from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize("ex_2.pyx")
)
