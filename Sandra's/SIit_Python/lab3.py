customers = input("Input (Number of customers):")
discount = input("Input (Discount code):")
total = 0
if customers.isnumeric():
    customers = int(customers)
    if customers > 6:
        total += (customers * 599)
        print(f"{customers} person x 599.00 baht")
        print("A subtotal price is %.2f baht"%total)
    elif 4 <= customers <= 6:
        total += (customers * 499)
        print(f"{customers} person x 499.00 baht")
        print("A subtotal price is %.2f baht"%total)
    elif 1<= customers <=3:
        total += (customers * 399)
        print(f"{customers} person x 399.00 baht")
        print("A subtotal price is %.2f baht"%total)
    else:
        print("Error")    
else:
    print("Error")

if discount == "COVID":
    print("On-top discount 30%")
    print("A total price is %.2f baht"%(total-(total*0.3)))
elif discount == "BIRTHDAY":
    print("On-top discount 10%")
    print("A total price is %.2f baht"%(total-(total*0.1)))
elif discount == "CASH":
    print("On-top discount 5%")
    print("A total price is %.2f baht"%(total-(total*0.05)))
else:
    print("On-top discount 0%")
    print("A total price is %.2f baht"%total)