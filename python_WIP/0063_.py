import math



for n in range(10, 99999999):
    root = n**(1/len(str(n)))
    if int(root)**(len(str(n))) == n:
        print(n)
