from re import sub


customer = int(input("Input (Number of customers): "))
code = input("Input (Discount code): ")
price = 399
discount = 0
if customer >= 4 and customer <= 6:
    price = 499
elif customer > 6:
    price = 599

if code == "CASH":
    discount = 5
elif code == "BIRTHDAY":
    discount = 10
elif code == "COVID":
    discount = 30

print("%d person x %.2f baht" % (customer, price))
subtotal = customer * price
print("A subtotal price is %.2f baht" % subtotal)
print("On-top discount %d%%" % discount)
print("A total price is %.2f baht" % (subtotal - (subtotal * (discount / 100))))
