n = input("Input: ")
for i in range(len(n)):
    if n[i].isnumeric():
        x = int(n[i])
        if x == 0:
            print(" ",end="")
        for j in range(1,x+1):
            if j == 3 or j == 6 or j == 9:
                print("#",end="")
            else:
                print("*", end="")
        print(" ")
    else:
        continue

