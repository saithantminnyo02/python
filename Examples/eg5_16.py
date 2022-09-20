a = 0
b = 2
n = 10
d = (b - a) / n
sum = 0
for i in range(1, n+1):
    x = a + ((((2 * i) - 1) * d) / 2)
    sum += x**3 + 2
    print(sum)
print("A =", d * sum)