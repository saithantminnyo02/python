unit = input("Enter the count unit: ")
if unit.isnumeric():
    unit = int(unit)
    if 1 <= unit <= 40:
        for i in range(13):
            print("%d * %d = %d" % (i, unit, (i * unit)))
    else:
        print("Out of range")
else:
    print("Out of range")