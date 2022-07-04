from distutils.core import setup

from Cython.Build import cythonize

setup(name="Hello world app", ext_modules=cythonize(["hello_Cython/hello.pyx", "hello_Cython/fib.pyx", 
"hello_Cython/primes.pyx", # Cython code file with primes() function
"example_py_cy.py", # Python code file with primes_python_compiled() function
"primes_c++.pyx" # C++ vector code
 ], annotate=True))
