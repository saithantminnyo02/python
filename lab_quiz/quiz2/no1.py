import math
ch = input("Input a shape T/S/C: ")
if ch in ['T', 'S', 'C']:
    length = input("Input a length: ")
    if length.isnumeric():
        length = int(length)
        if length >= 0:
            if ch == "T":
                ans = length * length * 0.25
                print("The surface area of triangle is %.2f" % ans)
            elif ch == "S":
                ans = length**2 * 0.5
                print("The surface area of square is %.2f" % ans)
            elif ch == "C":
                ans = math.pi * ((length / 2)**2)
                print("The surface area of circle is %.2f" % ans)
        else:
            print("Length must be more than or equal to zero.")
    else:
        print("Length must be numeric.")
else:
    print("Type must be only T/S/C.")