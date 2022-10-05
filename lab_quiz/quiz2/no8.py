n = 5
col = n+n-1
for i in range(col):
    for j in range(n):
        if i >= j and j < col - i:
            if j % 2 == 0:
                    print("*", end=" ")
            else:
                print("0", end=" ")
        else:
            print(" ", end = " ")
    # for j in range(n):
    #     if (n - j <= i + 1) and (j >= i - n + 1):
    #         if j % 2 == 0:
    #                 print("*", end=" ")
    #         else:
    #             print("0", end=" ")
    #     else:
    #         print(" ", end = " ")
    print()

# first part
# for i in range(col):
#     for j in range(n):
#         if i >= j and j < col - i:
#             if j % 2 == 0:
#                     print("*", end=" ")
#             else:
#                 print("0", end=" ")
#         else:
#             print(" ", end = " ")
#     print()

# second part
# for i in range(col):
#     for j in range(n):
#         if (n <= i + j + 1) and (j + n >= i + 1):
#             if j % 2 == 0:
#                     print("*", end=" ")
#             else:
#                 print("0", end=" ")
#         else:
#             print(" ", end = " ")
#     print()