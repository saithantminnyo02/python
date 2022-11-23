while True:
    num = input("Enter an integer number (0 to exit): ")
    if num == "0":
        print("Exit program. Bye!")
        break
    else:
        if num.isnumeric() and 0 <= (int(num)) <= 9:
            num = int(num)
            for i in range(1, num + 1):
                for j in range(num):
                    if i + j >= num:
                        print(num, end=" ")
                    else:
                        print(" ", end="")
                print()
        else:
            print("Valid value is between 0 and 9!")
            break