num = 100

sqsum = 0
sumsq = 0

for i in range(1,101):
    sqsum += i**2

for i in range(1,101):
    sumsq += i

sumsq = sumsq**2

print(sumsq - sqsum)