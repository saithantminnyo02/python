l = [0, 1]
sum = 0
n = 0
i = 2
while True:
    f = l[n] + l[n+1]
    if f > 100:
        break
    l.append(f)
    n += 1
print(l)
