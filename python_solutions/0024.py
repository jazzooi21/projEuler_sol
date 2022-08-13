import itertools

l = list(itertools.permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))


l.sort()
print(l)

num = 1000000%(len(l)) - 1

print(l[num])