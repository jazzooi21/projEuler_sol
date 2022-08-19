import math

def isprime(p):
    if p == 1 or p <= 0:
        return False
    elif p == 2:
        return True
    for i in range(2, int(math.sqrt(p)) + 1):
        if p % i == 0:
            return False
    return True

def primes_between_ab(a, b):
    p_list = []
    for i in range(a, b):
        if isprime(i):
            p_list.append(i)
    return p_list


sq_n = [i**2 for i in range(0, 1000)]
primes = primes_between_ab(1, 999999)

for n in range(3, 999999, 2):
    if not isprime(n):
        print(n)
        cond = False
        for p in primes:
            if p>n:
                break
            if (n-p)/2 in sq_n:
                cond = True

        if not cond:
            print('solution is', n)
            exit()
