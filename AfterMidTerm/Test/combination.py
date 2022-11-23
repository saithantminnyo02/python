l = input("Enter a comma-separated list: ").split(',')
# for i in l:
#     for j in l:
#         for k in l:
#             if (i != k) and (i != j) and (k != j) and i < j and j < k:
#                 c = [i, j, k]
#                 print(f"{c[0]} {c[1]} {c[2]}")

print(l)
print("Permutation: ")
for i in l:
    for j in l:
        for k in l:
            if (i != k) and (i != j) and (k != j):
                c = [i, j, k]
                print(f"{c[0]} {c[1]} {c[2]}")

print("Combination")

for iNo, i in enumerate(l):
    for jNo, j in enumerate(l):
        for kNo, k in enumerate(l):
            if (iNo != kNo) and (iNo != jNo) and (kNo != jNo) and iNo < jNo and jNo < kNo:
                c = [i, j, k]
                print(f"{c[0]} {c[1]} {c[2]}")