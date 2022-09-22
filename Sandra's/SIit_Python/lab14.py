character = input("Enter a special character: ")
size = input("Enter the size of the pattern: ")
option= input("Enter option for the pattern: ")
if character not in ["#","$","a","*","^"] or not option.isnumeric():
    print("Wrong input values.")
else:
    option = int(option)
    if option != 1 and option !=2:
        print("Wrong input values.")
    else:
        if size.isnumeric():
            size = int(size)
            if option == 1:
                for i in range(size):
                    for j in range(size):
                        if j == i:
                            print(character, end="\t")
                        else:
                            print(".",end="\t")
                    print(" ")
            elif option == 2:
                for i in range(size,0,-1):
                    for j in range(1,size+1):
                        if j == i:
                            print(character, end="\t")
                        else:
                            print(".",end="\t")
                    print(" ")
            else:
                print("Wrong input values.")
        else:
            print("Wrong input values.")

    
