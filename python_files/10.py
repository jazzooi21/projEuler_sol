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

sum = 2

for i in range(3,2000000-1, 2):
    print(i)
    if isprime(i):
        sum += i

print(sum)