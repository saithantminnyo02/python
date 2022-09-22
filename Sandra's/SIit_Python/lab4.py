import random as r
list = ["#",  "$", "*"]
width = input("Rectangle width:")
height = input("Rectangle height:")
thickness = input("Rectangle thickness:")
if width.isnumeric() and height.isnumeric() and thickness.isnumeric():
    width, height, thickness = int(width), int(height), int(thickness)
    for i in range(height):
        for j in range(width):
            if(i>=thickness and i<(height-thickness)) and (j>=thickness and j<(width-thickness)):
                print(" ", end="")
            else:
                print(r.choice(list), end="")
        print(" ")
else:
    print("Error")