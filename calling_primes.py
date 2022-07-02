import pyximport; pyximport.install()
from hello_Cython import primes

print(primes.primes(10))
