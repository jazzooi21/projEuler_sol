import math

#a^b

sol_l = []

for b in range(1,30):
    for a in range(1,10**10):
        if len(str(a**b)) == b:
            print(a**b)
            sol_l.append(a**b)
        elif len(str(a**b)) > b:
            break

print(len(sol_l))