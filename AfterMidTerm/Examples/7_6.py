x = int(input("Enter an integer: "))
prime = True
for i in range(2, x):
    if x % i == 0:
        prime = False
        break
if prime:
    print("%d is a prime number." % x)
else:
    print("%d is not a prime number." % x)