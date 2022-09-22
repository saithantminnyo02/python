# column = 17
n = 5
col = n + n - 1
for i in range(1, n+1):
    bol = True
    for j in range(1, col + 1):
        if i > n - j and j - n < i:
            if bol:
                print(i, end="")
                bol = False
            else:
                print("*", end="")
                bol = True
        else:
            print("*", end="")
    print()