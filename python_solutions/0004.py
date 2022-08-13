def palin(number):
    if str(number) == str(number)[::-1]:
        return True
    else:
        return False

sol = 0

n = 999
m = 999

for i in range(1000): #checking squares and product of consecutive integers
    if palin(n*m):
        sol = n*m
        break
    if i%2 == 0:
          n -= 1
    elif i%2 == 1:
        m -= 1


n = 999
m = 999

for i in range(999):

    for j in range(999):
        if n * m <= sol:
            m = 999
            break
        if palin(n * m):
            sol = n * m
            break
        m -= 1

    if n * m <= sol:
        break
    if palin(n * m):
        sol = n * m
        break
    n -= 1


print(sol)