str1 = input("Input string1: ")
str2 = input("Input string2: ")
set1, set2 = set(), set()
for ch in str1:
    set1.add(ch)
for ch in str2:
    set2.add(ch)

output = set1 & set2
output = list(output)
output = sorted(output)
print(("".join(output)))