s = input("Enter a string: ")
for c in s:
    if c.lower() not in "aeiou":
        print(c, end="")
print()