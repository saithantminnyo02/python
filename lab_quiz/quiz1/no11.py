a = input("a=? ")
b = input("b=? ")
c = input("c=? ")
if a.isnumeric() and b.isnumeric() and c.isnumeric():
    a, b, c = int(a), int(b), int(c)
    if a > 0 and b > 0 and c > 0:
        arr = [a, b, c]
        arr.sort()
        if arr[2] < (arr[0] + arr[1]):
            print("Form a triangle.")
        else:
            print("Can't form a triangle.")
    else:
        print("Some input is not a positive.")
else:
    print("Some input is not a number")