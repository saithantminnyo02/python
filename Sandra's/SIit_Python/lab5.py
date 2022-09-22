
speed = input("Enter speed in mph:")
if not speed.isnumeric() or int(speed) <0:
    print("Invalid input")
else:
    miles = input("Enter distance in miles:")
    if not miles.isnumeric() or int(miles) <0:
        print("Invalid input")
    else:
        format = input("Enter output format (D or M):")
        if format not in ["M","D"]:
            print("Invalid input")
        else:
            speed, miles = int(speed) , int(miles)
            if format == "D":
                t = miles/ speed
                print(f"At {speed} mph, it will take")
                print("%.2f hours to travel %d miles."%(t,miles))
            elif format == "M":
                total = miles //speed
                reminder = ((miles % speed)/speed)*60
                reminder = int(reminder)
                print(f"At {speed} mph, it will take")
                print(f"{total} hours and {reminder} minuters to travel {miles} miles.")


    
