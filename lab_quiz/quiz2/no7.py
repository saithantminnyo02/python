import math
a, b, c = input("Please enter an input: ").split("*")
choice = input("Please enter your choice (1 or 2): ")
if a.isnumeric() and b.isnumeric() and c.isnumeric() and choice.isnumeric() and (choice in ["1", "2"]):
    a, b, c = int(a), int(b), int(c)
    if a > 0 and b > 0 and c > 0:
        if choice == "1":
            ans = a + math.sqrt((b**2) + (c**3))
        else:
            ab = int(str(a) + str(b))
            ans = ab % c
        print("The output is %.2f" % ans)
    else:
        print("Invalid Inputs")
else:
    print("Invalid Inputs")