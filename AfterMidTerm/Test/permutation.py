# l = input("Enter a comma-separated list: ").split(',')
# # l = [1, 2, 3]
# for i in l:
#     for j in l:
#         for k in l:
#             if (i != k) and (i != j) and (k != j):
#                 c = [i, j, k]
#                 print(f"{c[0]} {c[1]} {c[2]}")

s = "easy"

new_s = ""
# for i in range(len(s) - 1):
#     new_s += s[i]
# new_s += "ily"

# print(new_s)

for i, ch in enumerate(s):
    if i == (len(s) - 1):
        if ch == "y":
            new_s += "ily"
            continue
    new_s += ch

print(new_s)