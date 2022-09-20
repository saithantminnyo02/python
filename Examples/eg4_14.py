d = input("Enter distance: ")
if d.isnumeric():
    d = int(d)
    if 0 < d < 100:
        s = 10
    elif 100 <= d < 150:
        s = 10 + (5 * (d - 100))
    else:
        s = 260 + (7 * (d - 150))
    print("Shipping cost = %.2f$" % s)
else:
    print("Error.")