num = int(input("Input: "))
if num >= 1 and num <= 15:
    count = 1
    for i in range(1, num+1):
        for j in range(1, num+1):
            if i > j:
                print(0, end="\t")
            else:
                print(count, end="\t")
                count += 1
        print()
else:
    print("Invalid input")