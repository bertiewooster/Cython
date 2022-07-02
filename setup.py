from distutils.core import setup

from Cython.Build import cythonize

setup(name="Hello world app", ext_modules=cythonize("hello_Cython/hello.pyx", "hello_Cython/fib.pyx"))
