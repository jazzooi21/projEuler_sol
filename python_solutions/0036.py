doub_palin_n = []
doub_palin_bin = []

for i in range(1, 1000000):
    i_bin = str(bin(i))[2:]
    if '0' not in [ str(i)[-1], i_bin[-1] ]:
        if str(i) == str(i)[::-1] and i_bin == i_bin[::-1]:
            doub_palin_n.append(i)
            doub_palin_bin.append(i_bin)

print(doub_palin_n)
print(doub_palin_bin)

print(sum(doub_palin_n))
