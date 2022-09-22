import math
a, b, c = input("Please enter an input:").split("*")
choice = input("Please enter your choice (1 or 2): ")
if a.isnumeric() and b.isnumeric() and c.isnumeric() and choice.isnumeric():
    a,b,c, choice = int(a), int(b), int(c), int(choice)
    if a < 0 or b < 0 or c < 0 or (choice != 1 and choice != 2):
        print("Invalid Inputs")
    else:
        if choice == 1:
            first = a + (math.sqrt((b*b)+(c*c*c)))
            print("The output is %.2f"%first)
        elif choice == 2:
            a = str(a)
            b = str(b)
            d = a + b
            d = int(d)
            if c <=0:
                print("Invalid Inputs")
            else:
                output =d % c
                print("The output is %.2f"%output)
else:
    print("Invalid Inputs")