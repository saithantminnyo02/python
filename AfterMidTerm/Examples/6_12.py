l = input("Enter integers: ").split()
print(l)
m = []
for x in l:
    if x.isnumeric():
        m.append(int(x))
    else:
        print("Error: '%s' is not an integer" % x)
print("Sum of input numbers = %d" % sum(m))