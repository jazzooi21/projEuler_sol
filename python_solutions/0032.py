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

nodupe_4digit = []

for i in range(1000, 10000):
    if len(list(str(i))) == len(set(str(i))) and '0' not in str(i):
        nodupe_4digit.append(i)

noprime = []
for n in nodupe_4digit:
    if not isprime(n):
        noprime.append(n)

pandig_prod = set()
for n in noprime:
    for i in range(2, int(math.sqrt(n))+1):
        if n%i == 0:
            if set(str(n)+str(i)+str(int(n/i))) == set('123456789'):
                # print(i, int(n/i), n)
                pandig_prod.add(n)

print(sum(pandig_prod))