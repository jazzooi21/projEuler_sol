import numpy as np

l = set()

def factorsum(n):
    facsum = 0
    for factor in range(1, int(n/2)+1):
        if n%factor == 0:
            facsum += factor
    return facsum

for i in range(10000):
    facsumi = factorsum(i)
    if factorsum(facsumi) == i and facsumi != i:
        l.add(i)
        l.add(facsumi)

print(l)
print(sum(l))




