
l = []

for n in range(2, 1000000):
    sum = 0

    for i in range(len(str(n))):
        sum += int((str(n))[i])**5

    print(n, sum)

    if sum == n:
        l.append(n)

sol = 0
for num in l:
    sol += num

print(sol)