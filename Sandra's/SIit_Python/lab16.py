import math
a,b = input("Please enter two integers: ").split(" ")
if a.isnumeric() and b.isnumeric():
    a , b = int(a), int (b)
    if 1 < a < 30 and 1 < b < 30:
        sum = 0
        if a > b:
            print(f"The minimum number is {b}")
            print(f"The maximum number is {a}")  
            for i in range(b,a+1):
                sum += i
        elif b > a:
            print(f"The minimum number is {a}")
            print(f"The maximum number is {b}") 
            for i in range(a,b+1):
                sum += i
        sum = math.sqrt(sum)
        print("The square root of the summation is %.2f"%sum)
    else:
        print("Invalid Inputs")
else:
    print("Invalid Inputs")