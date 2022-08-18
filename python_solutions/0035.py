import math


def isprime(p):
    if p == 1 or p <= 0:
        return False
    elif p == 2:
        return True
    for i in range(2, int(math.sqrt(p))+1):
        if p%i == 0:
            return False
    return True


def primes_between_ab(a, b):
    p_list = []
    for i in range(a, b):
        if isprime(i):
            p_list.append(i)
    return p_list


circ_primes = {2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97}

primes = primes_between_ab(101, 1000000)

for p in primes:

    if p not in circ_primes:
        str_p = str(p)
        circ = True
        for rot_times in range(len(str(p))):
            if int(str_p[1:] + str_p[0]) not in primes:
                circ = False
                break
            else:
                str_p = str_p[1:] + str_p[0]
        if circ:
            # print(p)
            # print('cir_p len:', len(circ_primes))
            str_p = str(p)
            for rot_times in range(len(str(p))):
                circ_primes.add(int(str_p))
                str_p = str_p[1:] + str_p[0]
            circ_primes.add(int(str_p))



print(len(circ_primes))

