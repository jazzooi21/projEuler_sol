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


def primes_between_ab(a, b):
    p_list = []
    for i in range(a, b):
        if isprime(i):
            p_list.append(i)
    return p_list


primes = primes_between_ab(1, 1000000)
summation = 0
primesum = []

for p in primes:
    summation += p
    if summation in primes:
        print(p, summation)
        primesum.append(summation)
    if summation > 1000000:
        break

print(primesum[-1])print(primesum[-1])print(primesum[-1])print(primesum[-1])print(primesum[-1])print(primesum[-1])print(primesum[-1])print(primesum[-1])print(primesum[-1])print(primesum[-1])print(primesum[-1])print(primesum[-1])print(primesum[-1])print(primesum[-1])print(primesum[-1])print(primesum[-1])print(primesum[-1])print(primesum[-1])print(primesum[-1])print(primesum[-1])print(primesum[-1])print(primesum[-1])print(primesum[-1])print(primesum[-1])print(primesum[-1])print(primesum[-1])print(primesum[-1])print(primesum[-1])print(primesum[-1])print(primesum[-1])print(primesum[-1])print(primesum[-1])print(primesum[-1])print(primesum[-1])print(primesum[-1])print(primesum[-1])