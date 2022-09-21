import math
num1, num2 = input("Please enter two integers: ").split(" ")
if num1.isnumeric() and num2.isnumeric():
    num1, num2 = int(num1), int(num2)
    if (1 < num1 < 30) and (1 < num2 < 30):
        if num1 > num2:
            max = num1
            min = num2
        else:
            max = num2
            min = num1
        sum = 0
        for i in range(min, max+1):
            sum += i
        print("The minimum number is", min)
        print("The maximum number is", max)
        print("The square root of the summation is %.2f" % (math.sqrt(sum)))
    else:
        print("Invalid Inputs")
else:
    print("Invalid Inputs")