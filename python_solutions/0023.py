import math



def factors(num):
    fac = set()
    fac.add(1)
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            fac.add(i)
            fac.add(int(num / i))
    return fac


abun_nums = []


for n in range(12, 28123):
    if sum(factors(n)) > n:
        abun_nums.append(n)

#print(abun_nums)

l_not_abun_sum = list(range(1,28124))

for i,n in enumerate(abun_nums):
    for m in abun_nums[i:]:
        print(n,m)
        if n+m in l_not_abun_sum:
            l_not_abun_sum.remove(n+m)
        if n + m > 28124:
            break

print(l_not_abun_sum)

sol = sum(l_not_abun_sum)

print(sol)
