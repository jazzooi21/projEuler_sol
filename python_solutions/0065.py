from fractions import Fraction

e_seq = [2,1,2]

for k in range(2,50):
	e_seq += [1,1,2*k]


e_seq = e_seq[:100]

print(e_seq)


def e_contfrac(seq,n):
	if n == 0:
		return 2
	eseq = seq[:n+1]
	e = eseq[-1]
	for i,n in enumerate(eseq[::-1][1:]):
		e = n+Fraction(1,e)
	return e

for i in range(0,100):
	break
	print(i+1, e_contfrac(e_seq,i))



e = e_contfrac(e_seq,100)
sol = list(str(e.numerator))
sol = [int(d) for d in sol]
print(sum(sol))
