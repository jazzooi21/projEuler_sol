powers = set()
# set elements are unique

for a in range(2,101):
    for b in range(2,101):
        pwr = a**b
        powers.add(pwr)

print(len(powers))