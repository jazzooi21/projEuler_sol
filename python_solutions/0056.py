max_dig_sum = 0

for i in range(1,100):
    for j in range(1, 100):
        dig_sum = 0
        for char in list(str(i**j)):
            dig_sum += int(char)
        if max_dig_sum < dig_sum:
            max_dig_sum = dig_sum

print(max_dig_sum)