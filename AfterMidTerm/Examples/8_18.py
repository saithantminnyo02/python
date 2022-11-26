str1 = input("Input string1: ")
str2 = input("Input string2: ")
l1, l2 = [], []
for ch in str1:
    l1.append(ch)
for ch in str2:
    l2.append(ch)

l1, l2 = sorted(l1), sorted(l2)

if l1 == l2:
    print("The input strings are anagrams.")
else:
    print("The input strings are not anagrams.")