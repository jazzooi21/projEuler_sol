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


diag = [1]
primes_len = 0
diag_len = 1
for n in range(2,10000000000,2):
	for i in range(4):
		new_n = diag[-1]+n
		diag.append(new_n)
		if isprime(new_n):
			primes_len += 1

	prime_ratio = primes_len/len(diag)
	print(prime_ratio)

	if prime_ratio < 0.1:
		print(n+1)
		quit()