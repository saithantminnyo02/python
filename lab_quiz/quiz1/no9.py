speed = int(input("Enter speed in mph: "))
if speed >= 0:
    distance = int(input("Enter distance in miles: "))
    if distance >= 0:
        ch = input("Enter output format (D or M): ")
        if ch in ['D', 'M']:
            mph = distance / speed
            print("At %d mph, it will take" % speed)
            if ch == "D":
                print("%.2f hours to travel %d miles." % (mph, distance))
            elif ch == "M":
                mph = mph * 60
                hours = int(mph / 60)
                seconds = mph % 60
                print("%d hours and %d minutes to travel %d miles." % (hours, seconds, distance))
        else:
            print("Invalid input")
    else:
        print("Invalid input")
else:
    print("Invalid input")
