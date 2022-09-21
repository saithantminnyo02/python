hour, min, sec = (input("Input: ")).split(':')
if hour.isnumeric() and min.isnumeric() and sec.isnumeric():
    hour = int(hour)
    min = int(min)
    sec = int(sec)
    if (0 <= hour <= 23) and (0 <= min <= 59) and (0 <= sec <= 59):
        print("The number of seconds = %d" % ((hour * 3600) + (min * 60) + sec))
    else:
        print("Invalid time")
else:
    print("Invalid time")