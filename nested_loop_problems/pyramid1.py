n = 5
for i in range(1, n+1):
    counter = 1
    bol = True
    for j in range(1, (i * 2)):
        print(counter, end=" ")
        if bol:
            counter += 1
        else:
            counter -= 1
        if i == j:
            counter -= 2
            bol = False
    print()


