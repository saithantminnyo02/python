import random
rand_list = ["#", "*", "$"]
# print(random.choice(rand_list))
width = int(input("Rectangle width: "))
height = int(input("Rectangle height: "))
thickness = int(input("Border thickness: "))
for i in range(0, height):
    for j in range(0, width):
        if j >= thickness and j < width - thickness and i >= thickness and i < height - thickness:
            print(" ", end="")
        else:
            print(random.choice(rand_list),end="")
    print()