def palin(n,depth=0):
	if depth > 50:
		return False

	palin_sum = int(str(n)[::-1])+n

	if str(palin_sum) == str(palin_sum)[::-1]:
		return True
	else:
		depth += 1
		return palin(palin_sum,depth+1)

sol = 0

for i in range(1,10**4):
	if not palin(i):
		print(i,': ',palin(i))
		sol += 1

print(sol)