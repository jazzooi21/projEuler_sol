import numpy as np

dummy = 0

n = 2

trinum = 1

while True:

    l = set()

    trinum += n

    l.add(1)
    l.add(trinum)

#int(np.sqrt(trinum)) + 1
    for fac in range(1, int(np.sqrt(trinum))+1):
        if trinum%fac == 0:
            l.add(fac)
            l.add(int(trinum/fac))


    print(n, trinum, len(l))

    if len(l) >= 500:
        print(trinum)
        quit()

    n += 1