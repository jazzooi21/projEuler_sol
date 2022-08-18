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
    for i in reversed(range(a, b)):
        if isprime(i) and len(set(str(i))) == len(list(str(i))) and '0' not in str(i):
            if len(str(i)) == 8:
                if '9' not in str(i):
                    return i
            elif len(str(i)) == 7:
                if '9' not in str(i) and '8' not in str(i):
                    return i
            elif len(str(i)) == 8:
                if '9' not in str(i) and '8' not in str(i) and '7' not in str(i):
                    return i


#tested; no valid solution between 1 000 000 000 and 100 000 000
sol = primes_between_ab(2143, 10000000)

print(sol)
