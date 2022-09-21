N = input("Input: ")
if N.isnumeric():
    N = int(N)
    if 1 <= N <= 15:
        # print a matrix
        counter = 1
        for row in range(N):
            for col in range(N):
                if row <= col:
                    print(counter, end="\t")
                    counter += 1
                else:
                    print(0, end="\t")
            print()
    else: 
        print("Invalid input")
else:
    print("Invalid input")