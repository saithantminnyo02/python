n = 5
col = n + n - 1
counter = 1
for i in range(1, n+1):
    for j in range(1, col + 1):
        if i > n - j and j - n < i:
            print(counter, end=" ")
            if j >= n:
                counter -= 1
            else:
                counter += 1
        else:
            print(" ", end=" ")
    print()
    counter = 1