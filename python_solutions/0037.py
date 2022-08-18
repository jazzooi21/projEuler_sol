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


trunc_primes = set()

primes = primes_between_ab(10, 1000000)

for p in primes:
    L = True
    R = True
    for i in range(len(str(p))-1):
        if not isprime(int(str(p)[i+1:])):
            L = False
            break
    for i in range(len(str(p))):
        if not isprime(int(str(p)[:len(str(p))-i])):
            R = False
            break
    if L and R:
        trunc_primes.add(p)
    if len(trunc_primes) >= 11:
        break

print(trunc_primes)
print(sum(trunc_primes))
