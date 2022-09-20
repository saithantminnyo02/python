sum = 0
for i in range(0, 10001):
    sum += (((-1)**i) / ((2 * i) + 1))
print(sum * 4)