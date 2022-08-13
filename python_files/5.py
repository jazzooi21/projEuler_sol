import numpy as np

prod = 1

def isprime(p):
    if p <= 1:
        return False
    elif p == 2 or p == 3:
        return True

    for i in range(2, int(np.sqrt(p))):
        if p%i == 0:
            return False
    return True



for i in range(1, 20):
    if isprime(i):
        prod *= i


prod *= 2**3
prod *= 3

print(prod)



