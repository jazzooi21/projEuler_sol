import numpy as np
def isprime(p):
    if p <= 1:
        return False
    elif p == 2 or p == 3:
        return True


    for i in range(2, int(np.sqrt(p))+1):
        if p%i == 0:
            return False
    return True


primes = []
index = 0



while len(primes) < 10001:
    index += 1
    if isprime(index):
        primes.append(index)

print(index)
