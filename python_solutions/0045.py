i = 1
tri_n = []
pen_n = []
hex_n = []
sol = []

while True:
    print(i)
    tri_n.append(i*(i+1)/2)
    pen_n.append(i*(3*i-1)/2)
    hex_n.append(i*(2*i-1))
    if (i*(i+1)/2) in pen_n and (i*(i+1)/2) in hex_n:
        sol.append((i*(i+1)/2))

    if len(sol) > 2:
        break

    i += 1

print(sol[2])
#sol[0] = 1, sol[1] = 40755