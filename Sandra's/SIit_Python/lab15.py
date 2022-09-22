a, b, c = input("a, b, c = ").split(" ")
if a not in ["True", "False"] or b not in ["True", "False"] or c not in ["True", "False"]:
    print("Invalid input")
else:
    if a == "False":
        if b == "False" and c == "False":
            print("Grant")
        else:
            print("Deny")
    else:
        print("Grant")