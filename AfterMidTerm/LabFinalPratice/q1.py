def error_message():
    print("Invalid transaction!")

b = int(input("Enter the initial balance: "))

while True:
    x, y = (input('Transaction type and amount ("done 0" to exit): ')).split()
    if x == "done" and y == "0":
        print("Current balance = %d THB." % b)
        break
    else:
        if y.isnumeric() and x in "DW":
            y = int(y)
            if x == "D":
                b += y
                print("Deposit = %d THB, current balance = %d THB." % (y, b))
            elif x == "W":
                if (b - y) < 0:
                    error_message()
                    continue
                else:
                    b -= y
                    print("Withdrawal = %d THB, current balance = %d THB." % (y, b))
        else:
            error_message()


