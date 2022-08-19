
for i in range(1, 999999999):
    if len(str(i)) == len(str(6*i)) and len(list(str(i))) == len(set(str(i))):
        if set(str(i)) == set(str(2*i)) == set(str(3*i)) == set(str(4*i)) == set(str(5*i)) == set(str(6*i)):
            print(i)
            exit()