points = 100

def displayPoints(num):
    print("Your accumulated points = %d points" % num)

while True:
    ch, amount = (input("Command: ")).split()
    if ch == "done" and amount == "0":
        break
    else:
        if ch not in "PR" or (not amount.isnumeric()) or int(amount) < 0:
            print("Invalid command")
        else:
            amount = int(amount)
            if ch == "P":
                new_point = amount // 50
                points += new_point
                print("You earned %d points" % new_point)
                displayPoints(points)
            else:
                if (points - amount) < 0:
                    print("Not enough points") 
                else:
                    points -= amount
                    print("You redeemed %d points" % amount)
                    displayPoints(points)
                


        