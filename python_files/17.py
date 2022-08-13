letters = 0

for n in range(1,1000):
#n = 999
    x = letters

    s = '00' + str(n)

    #FIRST TWO DIGITS
    unit = s[-1]
    tens = s[-2]
    hun = s[-3]
    uniten = tens + unit

    if tens in ['1']:
        if unit in ['0']:
            letters += 3
        elif unit in ['1', '2']:
            letters += 6
        elif unit in ['5', '6']:
            letters += 7
        elif unit in ['3', '4', '8', '9']:
            letters += 8
        elif unit in ['7']:
            letters += 9
    else:
        if unit in ['1', '2', '6']:
            letters += 3
        elif unit in ['4', '5', '9']:
            letters += 4
        elif unit in ['3', '7', '8']:
            letters += 5

        if tens in ['4', '5', '6']:
            letters += 5
        elif tens in ['2', '3', '8', '9']:
            letters += 6
        elif tens in ['7']:
            letters += 7
        # if tens == 0 do nothing

    if n >= 100:
        letters += 7 #'hundred'
        if hun in ['1', '2', '6']:
            letters += 3
        elif hun in ['4', '5', '9']:
            letters += 4
        elif hun in ['3', '7', '8']:
            letters += 5

    #AND
    if uniten != "00" and n > 100:
        letters += 3

    print(n, letters - x)


letters += 11 #1000

print(letters)