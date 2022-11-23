rate = {"JPY": 0.29, "USD": 31.99, "EUR": 35.62}
li = []
while True:
    inp = input("Input: ")
    if inp == "end":
        break
    else:
        cur, amount = inp.split(" ")
        amount = float(amount)
        if cur not in rate or amount < 1:
            print("ERROR")
        else:
            li.append([cur, amount])

for i in li:
    cur = i[0]
    amount = i[1]
    total = rate[cur] * amount
    print("%.2f %s is %.2f THB" % (amount, cur, total))
