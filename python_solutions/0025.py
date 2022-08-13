lastn = 0
n = 1

#THIS SHOULD BE 1000
dig = 1000

for i in range(1,10000000):
    n += lastn
    lastn = n - lastn

    if len(str(n)) == dig:
        print(i+1)
        quit()