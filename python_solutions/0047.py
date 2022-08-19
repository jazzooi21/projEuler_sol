import math


def isprime(p):
    if p == 1 or p <= 0:
        return False
    elif p == 2:
        return True
    for i in range(2, int(math.sqrt(p))+1):
        if p%i == 0:
            return False
    return True

def primefactors(num):
    fac = set()
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            if isprime(i):
                fac.add(i)
            if isprime(int(num / i)):
                fac.add(int(num / i))
    return fac

fax = []

for i in range(1,99999999):
    #print(i, len(primefactors(i)), primefactors(i))
    fax.append(len(primefactors(i)))
    if fax[len(fax)-4:] == [4, 4, 4, 4]:
        print(i-3)
        exit()