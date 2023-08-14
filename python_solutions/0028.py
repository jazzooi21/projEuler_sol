#501 diags

oddsquares = [(2*n+1)**2 for n in range(1,501)]

#print(len(oddsquares))

corner_sum = [sum([oddsquares[i-1],oddsquares[i-1]-(2*i),oddsquares[i-1]-(4*i),oddsquares[i-1]-(6*i)]) for i in range(1,501)]

#print(corner_sum)

print(sum(corner_sum)+1)
#+1 at the end