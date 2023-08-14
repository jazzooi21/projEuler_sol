pent_nums = [n*(3*n-1)//2 for n in range(1,10000)]

sol = 9999999999999999999999999999999999999999999999999

for n in pent_nums:
	for m in pent_nums:
		if n-m <= 0:
			break
		#print(n,m)
		if n-m in pent_nums and n+m in pent_nums:
			if n-m < sol:
				sol = abs(n-m)
				print(sol)
				quit()
