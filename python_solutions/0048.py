summation = 0

for i in range(1, 1001):
    summation += i**i
    print(i)

print(summation)
print(str(summation)[len(str(summation))-10:])