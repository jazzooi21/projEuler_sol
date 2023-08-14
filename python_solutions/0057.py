from fractions import Fraction

def sqrt2_frac(n):
	#n = 1: 1 + 1/2
	output = 1
	
	for i in range(1,n+1):
		output = 1 + Fraction(1,output+1)

	return output

sol = 0

for j in range(1,1000+1):
	frac = sqrt2_frac(j)
	num = frac.numerator
	denom = frac.denominator

	if len(str(num)) > len(str(denom)):
		sol += 1
		#print(j,frac)

print(sol)