import math
import numpy as np

def isprime(p):
    if p == 1 or p <= 0:
        return False
    elif p == 2:
        return True
    for i in range(2, int(math.sqrt(p))+1):
        if p%i == 0:
            return False
    return True


def return_primes_under_n(n):
    primes = []
    for i in range(1, n):
        if isprime(i):
            primes.append(i)
    return primes


def factors(num):
    fac = set()
    fac.add(1)
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            fac.add(i)
            fac.add(int(num / i))
    return fac
