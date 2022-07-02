import pyximport; pyximport.install()
from hello_Cython import fib

fib.fib(2000)
