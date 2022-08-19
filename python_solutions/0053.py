import math

sol = 0

for i in range(1, 101):
    for j in range(1, i):
        if math.comb(i, j) > 1000000:
            sol += 1

print(sol)