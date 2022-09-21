# for i in range(5):
#     for j in range(5):
#         if i == j:
#             print("$",end=" ")
#         else:
#             print(".",end=" ")
#     print()
# save = 4
# for i in range(5):
#     for j in range(5):
#         if save == j:
#             print("$",end=" ")
#             save -= 1
#         else:
#             print(".",end=" ")
#     print()

spe = input("Enter a special character: ")
size = input("Enter the size of the pattern: ")
option = input("Enter option for the pattern: ")
if (spe in ["#", "$", "@", "*", "^"]) and (size.isnumeric()) and (option.isnumeric()) and (option in ["1", "2"]):
    size, option = int(size), int(option)
    save = size - 1
    for i in range(size):
        for j in range(size):
            if option == 1:
                if i == j:
                    print(spe, end=" ")
                else:
                    print(".", end=" ")
            elif option == 2:
                if save == j:
                    print(spe, end=" ")
                    save -= 1
                else:
                    print(".", end=" ")
        print()
else:
    print("Wrong input values.")