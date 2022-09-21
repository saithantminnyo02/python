s = input("Input: ")
for i in s:
    if i.isnumeric():
        num = int(i)
        for j in range(1, num+1):
            if j % 3 == 0:
                print("#", end="")
            else:
                print("*", end="")
        print()