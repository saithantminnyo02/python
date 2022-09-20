a, b, n = input("Enter a, b and n: ").split(",")
a, b, n = int(a), int(b), int(n)
d = (b - a) / n
sum = 0
for i in range(1, n+1):
    x = a + ((((2 * i) - 1) * d) / 2)
    sum += x**2 + (2 * x) + 1
print("A =", d * sum)