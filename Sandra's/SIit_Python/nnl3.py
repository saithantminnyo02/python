#inverted half pyramid
n = 11
for i in range(n):
    for j in range(n,-1,-1):
        if i < j :
            print("*", end="")
        else:
            print(" ",end="")
    print(" ")