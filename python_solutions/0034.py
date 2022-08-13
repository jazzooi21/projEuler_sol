import numpy as np
l = []

for n in range(3, 1000000):
    sum = 0

    for i in range(len(str(n))):
        digit = int((str(n))[i])
        sum += np.math.factorial(digit)

    print(n, sum)

    if sum == n:
        l.append(n)

sol = 0
for num in l:
    sol += num

print(l)
print(sol)