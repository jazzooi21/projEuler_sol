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


primes = primes_between_ab(1, 10**6)
primesum = []

sol = ['len','p']

max_len = 0

for j in range(len(primes)-1):
    print('j =',j)
    sum_prime = 0
    for i,p in enumerate(primes[j:]):

        #turns out j=3 is alr the biggest lol
        if j>3:
            quit()

        sum_prime += p
        if sum_prime >= 10**6:
            break
        if sum_prime in primes and (i+1) > max_len:
            print(p, sum_prime)
            max_len = i+1
            sol = [max_len,sum_prime]


