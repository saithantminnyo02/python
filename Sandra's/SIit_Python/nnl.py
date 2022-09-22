n = input("Input: ")
if n.isnumeric():
    n = int(n)
    for i in range(n):
        for j in range(n,-1,-1):
            if j<= i:
                print("#", end="")
            else:
                print(" ", end="") 
        print(" ", end="") 
        for j in range(n):
            if j<= i:
                print("#", end="")
            else:
                print(" ", end="") 
        print(" ")
else:
    print("Your input is invalid.")