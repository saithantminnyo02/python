n = input("Input:")
if n.isnumeric():
    n = int(n)
    count = 0
    for i in range(0,n):
        for j in range(0,n):
            if i>j:
                print(0*i, end="\t")
            else:
                count+= 1
                print(count, end="\t")
        print(" ")
    

