
sol = 0

file = open("files/p022_names.txt", "r")

l = file.read()

l = l.split('","')

l[0] = l[0][1:]

l[len(l)-1] = l[len(l)-1][:-1]

l.sort()

abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for order, name in enumerate(l):
    score = 0
    for letter in name:
        for i, char in enumerate(abc):
            if letter == char:
                score += i+1

    score *= order + 1

    sol += score


print(sol)