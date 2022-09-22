#hollow inverted half pyramid
n = 6
for i in range(n):
    for j in range(n,-1,-1):
        if i < j and j <= (n-i) :
            print("*", end="")
        else:
            print(" ",end="")
    print(" ")