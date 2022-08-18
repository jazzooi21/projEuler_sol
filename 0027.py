import math


def isprime(p):
    if p == 1:
        return False
    elif p == 2:
        return True
    elif p <= 0:
        return False
    for i in range(2, int(math.sqrt(p))):
        if p%i == 0:
            return False
    return True

primes = []
for i in range(1, 100000):
    if isprime(i):
        primes.append(i)



num_of_pri_gen = [0, 0, 0]

#n**2 + an + b
for b in range(1,1000):
    for sign in [1,-1]:
        for a in range(1,1000):
            iter_num = 0
            for x in range(0,999999999999999):
                iter_num += 1
                if not isprime( x**2 + (sign*a)*x + b ):
                    if iter_num > num_of_pri_gen[0]:
                        num_of_pri_gen = [iter_num, sign*a, b]
                    break

print(num_of_pri_gen)
print(num_of_pri_gen[1],'x', num_of_pri_gen[2], '=', num_of_pri_gen[1]*num_of_pri_gen[2])