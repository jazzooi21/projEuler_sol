from itertools import permutations

cubes = []

for n in range(345,10000):
	cubes.append(n**3)


cubes_sorted = [''.join(sorted(str(n))) for n in cubes]

for n in cubes[:]:
	sorted_str = ''.join(sorted(str(n)))
	if cubes_sorted.count(sorted_str) < 5:
		cubes.remove(n)

cubes_dict = {n:''.join(sorted(str(n))) for n in cubes}

cubes_dict = sorted(cubes_dict)

print(cubes_dict[0])