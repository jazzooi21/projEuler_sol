yes = set()
no = set()

def sq_end_89(n):
	if n == 1:
		if n <= (9**2)*7:
			no.add(n)
		return False
	elif n == 89:
		if n <= (9**2)*7:
			yes.add(n)
		return True
	elif n in no:
		return False
	elif n in yes:
		return True
	else:
		return sq_end_89(sum(int(i)**2 for i in str(n)))

sol = 0

for i in range(1,10**7):

	bool_89 = sq_end_89(i)

	if i%100000 == 0:
		print(i,': ', bool_89)

	if bool_89:
		sol += 1


print(sol)