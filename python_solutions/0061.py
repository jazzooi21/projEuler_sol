tri_l = [] #T
sqr_l = [] #S
pen_l = [] #P
hexa_l = [] #X
hept_l = [] #H
octa_l =[] #O

def four_digit(n):
	if len(str(n)) == 4:
		return True
	else:
		return False



for i in range(1,99999999):

	tri = i*(i+1)//2
	if four_digit(tri):
		tri_l.append(str(tri))
	elif len(str(tri)) > 4:
		break

	sqr = i**2
	if four_digit(sqr):
		sqr_l.append(str(sqr))

	pen = i*(3*i-1)//2
	if four_digit(pen):
		pen_l.append(str(pen))

	hexa = i*(2*i-1)
	if four_digit(hexa):
		hexa_l.append(str(hexa))

	hept = i*(5*i-3)//2
	if four_digit(hept):
		hept_l.append(str(hept))

	octa = i*(3*i-2)
	if four_digit(octa):
		octa_l.append(str(octa))


#print(tri_l,sqr_l,pen_l,hexa_l,hept_l,octa_l)

all_l = tri_l+sqr_l+pen_l+hexa_l+hept_l+octa_l
all_l_end = set([s[2:] for s in all_l])
all_l_start = set([s[:2] for s in all_l])


for s in all_l:
	if s[:2] not in all_l_end or s[2:] not in all_l_start:
		for l in [tri_l,sqr_l,pen_l,hexa_l,hept_l,octa_l]:
			if s in l:
				l.remove(s)

all_l = tri_l+sqr_l+pen_l+hexa_l+hept_l+octa_l

sols = []

for s1 in all_l:
	for s2 in all_l:
		if s1[2:] == s2[:2]:
			for s3 in all_l:
				if s2[2:] == s3[:2]:
					for s4 in all_l:
						if s3[2:] == s4[:2]:
							for s5 in all_l:
								if s4[2:] == s5[:2]:
									for s6 in all_l:
										if s5[2:] == s6[:2]:
											sols.append([s1,s2,s3,s4,s5,s6])


'''
for s in all_l:
	if s in tri_l:
		print('tri')
	if s in sqr_l:
		print('sq')
	if s in pen_l:
		print('pen')
	if s in hexa_l:
		print('hex')
	if s in hept_l:
		print('hept')
	if s in octa_l:
		print('oct')
'''

def num_s(n):
	n = str(n)
	output = ''
	if n in tri_l:
		output += 'T'
	if n in sqr_l:
		output += 'S'
	if n in pen_l:
		output += 'P'
	if n in hexa_l:
		output += 'X'
	if n in hept_l:
		output += 'H'
	if n in octa_l:
		output += 'O'
	return output

print(len(sols))

sols = [tuple(l) for l in sols if len(set(l)) == 6]
sols = list(dict.fromkeys(sols))
sols = [t for t in sols if t[-1][2:]==t[0][:2]]

print(len(sols))

sols_dict_l = [dict.fromkeys(sol) for sol in sols]

for d in sols_dict_l:
	for key in d:
		d[key] = num_s(key)
		#print(key,d[key])

#print(sols_dict_l)

for d in sols_dict_l[:]:
	str_tot_l = d.values()
	str_tot = ''.join(str_tot_l)
	if len(set(str_tot_l)) < 6 or any(c not in str_tot for c in list('TSPXHO')):
		sols_dict_l.remove(d)

#for d in sols_dict_l:
	#print(d)
	#print(sum(int(k) for k in d.keys()))

sols_num = []
for d in sols_dict_l[:]:
	sols_num.append(set(int(k) for k in d.keys()))

sols_num_nodupe = []
for n in sols_num:
	if n not in sols_num_nodupe:
		sols_num_nodupe.append(n)

print(sum(sols_num_nodupe[0]))