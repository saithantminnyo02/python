l = []
while True:
    try:
        x = int(input("Enter an integer (-999=exit): "))
        if x == -999:
            break
        l.append(x)
    except ValueError:
        print("Invalid value. Please input an integer!")
print("Sum = %d" % sum(l))

# while True:
#     x = int(input("Enter an integer (-999=exit): "))
#     if x == -999:
#         break
#     l.append(x)
# print("Sum = %d" % sum(l))