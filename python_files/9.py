import numpy as np

sqn = []


for i in range(1,1000):
    if i**2 > 1000000:
        break
    sqn.append(i**2)



for i in sqn:
    for j in sqn:
        for k in sqn[2:]:
            if i + j == k and i**(1/2) + j**(1/2) + k**(1/2) == 1000:
                print(i**(1/2) * j**(1/2) * k**(1/2))
                quit()