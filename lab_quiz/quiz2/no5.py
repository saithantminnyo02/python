a, b, c = input("a, b, c = ").split(" ")
if (a == "True" or a == "False") and (b == "True" or b == "False") and (c == "True" or c == "False"):
    if a == "True":
        print("Grant")
    else:
        if b == "False" and c == "False":
            print("Grant")
        else:
            print("Deny")
else:
    print("Invalid input")
