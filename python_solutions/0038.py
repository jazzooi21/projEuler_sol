
sol = 123456789

for n in range(1, 100000):
    #print(n)
    n_concprod = ''
    for mul in range(1, 10):
        n_concprod += str(n*mul)

        if len(n_concprod) > 9:
            break
        elif len(n_concprod) == 9:
            if len(set(n_concprod)) == len(list(n_concprod)) and '0' not in n_concprod:
                if int(n_concprod) > sol:
                    sol = int(n_concprod)
                    print(n, sol)
            break


print(sol)