a = input("Input: a=? ")
b = input("Input: b=? ")
c = input("Input: c=? ")
if a.isnumeric() and b.isnumeric() and c.isnumeric():
    a,b,c = int(a), int(b), int(c)
    if a <0 or b <0 or c<0:
        print("Output: Can't form a triangle")
    else:
        if a > b and a >c:
            if a<(b+c):
                print("Output: Form a triangle")
            else:
                print("Output: Can't form a triangle")
        elif b > a and b >c:
            if b<(a+c):
                print("Output: Form a triangle")
            else:
                print("Output: Can't form a triangle")
        elif c > b and c >a:
            if c<(b+a):
                print("Output: Form a triangle")
            else:
                print("Output: Can't form a triangle")
        else:
            print("Output: Form a triangle")
else:
    print("Some input is not a number")
