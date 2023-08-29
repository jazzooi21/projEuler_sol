#28433 \times 2^{7830457} + 1

n = 1

for i in range(1,7830457+1):
  n *= 2
  n %= 10**10

print(n*28433 + 1)