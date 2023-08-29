import math
from itertools import combinations


def isprime(p):
    if p == 1 or p <= 0:
        return False
    elif p == 2:
        return True
    for i in range(2, int(math.sqrt(p))+1):
        if p%i == 0:
            return False
    return True




primes = []

for n in range(1000, 10000):
    if isprime(n):
        primes.append(n)


primes_pair = [[''.join(sorted(str(p))),p] for p in primes]


digits_dict = {}
for pair in primes_pair:
    digits_dict[pair[0]] = []

for pair in primes_pair:
    digits_dict[pair[0]].append(pair[1])



for key in digits_dict.copy():
    if len(digits_dict[key]) < 3:
        del digits_dict[key]

ll = [digits_dict[key] for key in digits_dict]

ll3 = []

for l in ll:
    ll3 += sorted(combinations(l,3))



for l in ll3[:]:
    if len(l) == 3:
        if l[1]-l[0] == l[2]-l[1]:
            print(l)