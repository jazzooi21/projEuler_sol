#Note: 0 is monday, 6 is sunday


#1 jan 1901
dotw = 365%7


year = 1901

count = 0

for i in range(1200):

    if dotw%7 == 6:
        count += 1


    if (i%12 + 1) in [1, 3, 5, 7, 8, 10, 12]:
        dotw += 31
    elif (i%12 + 1) in [4, 6, 9, 11]:
        dotw += 30
    elif (i%12 + 1) == 2:
        if year%4 == 0:
            dotw += 29
        else:
            dotw += 28


    if (i%12 + 1) == 1:
        year += 1
    if year >= 2001:
        break

print(count)