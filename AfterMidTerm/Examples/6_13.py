l = input("Enter integers: ").split()
m = [int(x) for x in l if x.isnumeric()]
print("Sum of input integers = %d" % sum(m))