
s = ''

for i in range(1, 1000000):
    if len(s) <= 1000000:
        s += str(i)

# index starts at 0!!!
sol = int(s[1-1])*int(s[10-1])*int(s[100-1])*int(s[1000-1])*int(s[10000-1])*int(s[100000-1])*int(s[1000000-1])
print(sol)