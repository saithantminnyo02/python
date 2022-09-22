n = 4
start = 3
bol = False
for i in range(1, n + n):
    for j in range(1, i + 1):
        if j <= n + n - i:
            print(start, end = "")
        if i >= 4:
            bol = True
    print()
    if bol:
        start -= 1
    else:
        start += 1