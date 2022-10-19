from re import X


sum = 0
while True:
    try:
        x = input("Enter number. (exit = DONE) ")
        if x == "DONE":
            break
        x = int(x)
        if x > 0:
            sum += x
    except ValueError:
        print("Enter number only.")
print("Sum of positive number =", sum)