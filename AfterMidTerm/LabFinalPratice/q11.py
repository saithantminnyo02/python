print("Welcome to coin deposit machine")
dic = {1: 0, 2: 0, 5: 0, 10: 0}
total = 0
while True:
    coin = input("Please insert coin: ")
    if coin == "done":
        break
    else:
        if coin.isnumeric():
            coin = int(coin)
            if coin in [1, 2, 5, 10]:
                dic[coin] += 1
                total += coin
                print(f"You inserted {coin} baht coin")
            else:
                print("Only 1,2,5 and 10 baht coin are allowed")
        else:
            print("Invalid Input")

print("<-----Deposit Summary----->")
for key,value in dic.items():
    print(f"{key} baht coins -> {value}")
print(f"Deposit Amount: {total} baht")
