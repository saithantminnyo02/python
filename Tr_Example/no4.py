import random
w = input("Rectangle width: ")
h = input("Rectangle height: ")
b = input("Border thickness: ")
if w.isnumeric() and h.isnumeric() and b.isnumeric():
    w, h, b = int(w), int(h), int(b)
    for row in range(h):
        for col in range(w):
            if b <= row <= h-b-1 and b <= col <= w-b-1:
                print(" ", end ="")
            else:
                print(random.choice(["#", ""]))
        print()
else:
    print("Invalid input")