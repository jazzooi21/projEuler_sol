
lastn = 1

n = 1

sum = 0

while n < 4000000:
    n += lastn
    lastn = n - lastn
    if n%2 == 0:
        sum += n

print(sum)