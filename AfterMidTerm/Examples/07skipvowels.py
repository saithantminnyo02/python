s = input("Enter a string: ")
for c in s:
    if c.lower() in "aeiou":
        continue
    print(c, end="")
print()