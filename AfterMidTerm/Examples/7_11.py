l = []
while True:
    try:
        x = int(input("Enter number. (negative number = exit) "))
        if x < 0:
            break
        l.append(x)
    except ValueError:
        print("Enter number only.")
print(l)