import math
shape = input("Input a shape T/S/C: ")
if shape not in ["T","S","C"]:
    print("Type must be only T/S/C.")
else:
    length = input("Input a length: ")
    if length.isnumeric():
        length = int(length)
        if length >0:
            if shape == "T":
                area = (length * length) / 4
                print("The surface area of triangle is %.2f"%area)
            elif shape =="S":
                area = (length * length) / 2
                print("The surface area of square is %.2f"%area)
            else:
                area = ((length / 2) **2)* math.pi
                print("The surface area of circle is %.2f"%area)
        else:
            print("length must be more than or equal to zero")
    else:
        print("Error")
