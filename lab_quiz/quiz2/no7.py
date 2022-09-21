import math
a, b, c = input("Please enter an input: ").split("*")
choice = input("Please enter your choice (1 or 2): ")
if a.isnumeric() and b.isnumeric() and c.isnumeric() and choice.isnumeric() and (choice in ["1", "2"]):
    a, b, c = int(a), int(b), int(c)
    if choice == "1":
        ans = a + ()
else:
    print("Invalid Inputs")