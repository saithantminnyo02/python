# n = 5
# for i in range(n-1):
#     for j in range(n):
#         if j <= i:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     for j in range(n,-1,-1):
#         if j <= i:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print("")
# for i in range(n-1,-1,-1):
#     for j in range(n):
#         if j <= i:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     for j in range(n,-1,-1):
#         if j <= i:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print("")
n = 5
for i in range(n-1):
    for j in range(n):
        if j <= i:
            print("*", end="")
        else:
            print(" ", end="")
    print("")
for i in range(n-1,-1,-1):
    for j in range(n):
        if j <= i:
            print("*", end="")
        else:
            print(" ", end="")
    print("")
for i in range(n-1):
    for j in range(n):
        if j <= i:
            print("*", end="")
        else:
            print(" ", end="")
    print("")
for i in range(n-1,-1,-1):
    for j in range(n):
        if j <= i:
            print("*", end="")
        else:
            print(" ", end="")
    print("")