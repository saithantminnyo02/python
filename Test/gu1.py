remaining = input("Input a remaining battery percentage: ")
per_min = input("Input a battery draining per minute: ")

remaining, per_min = float(remaining), float(per_min)
if remaining > 0 and per_min > 0:
    to_sec = per_min / 60
    secs = remaining / to_sec
    mins = secs / 60
    secs = secs % 60
    print("The remaining time is %d minutes and %d seconds." % (mins, secs))
else:
    print("Please check your input values")