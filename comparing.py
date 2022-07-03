import pyximport; pyximport.install()
from time import time

from hello_Cython.example_py_cy import primes_python_compiled
from hello_Cython.primes import primes
from hello_Cython.primes_python import primes_python


def timer(function):
    def wrapper(*args, **kwargs):
        start = time()
        function(*args, **kwargs)
        end = time()
        print(f'It took {(end-start):.3f} seconds')

    return wrapper

@timer
def call_pp():
    pp = primes_python(1000)
    print(f" {sum(pp)=}")

@timer
def call_p():
    p = primes(1000)
    print(f"  {sum(p)=}")

@timer
def call_ppc():
    ppc = primes_python_compiled(1000)
    print(f"{sum(ppc)=}")

call_pp()
call_p()
call_ppc()
