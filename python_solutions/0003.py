import numpy as np

sol = 0

num = 600851475143

def isprime(p):
    if p == 1:
        return False
    elif p == 2:
        return True

    for i in range(2, int(np.sqrt(p))):
        if p%i == 0:
            return False

    return True



for fac in range(int(np.sqrt(num)+1), 1, -2): #checking factors; since primes are odd, step size 2

    if num%fac == 0 and fac%2 != 0: #ignore even numbers since theyre not prime (except 2)
        if isprime(fac):
            print(fac)
            break
