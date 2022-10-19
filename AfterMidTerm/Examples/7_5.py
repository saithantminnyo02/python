x = input("Input a positive integer here: ")
if x.isnumeric():
    x = int(x)
    print("Prime factor of", x, end=" = ")
    i, factors = 2, []
    while i * i <= x:
        if x % i == 0:
            x //= i
            factors.append(i)
        else:
            i += 1
    if x > 1:
        factors.append(x)
    factors = [str(e) for e in factors]
    print("*".join(factors))
else:
    print("Invalid input")