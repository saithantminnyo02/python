first, second = input("Please enter your information: ").split(",")
if (not first.isalpha() and not second.isalpha()) or not first.isalpha() and not second.isalpha():
    print("Please enter your complete information.")
else:
    if first.isnumeric():
        first = int(first)
        if 0 <= first <= 120:
            print(f"Your name is {second}.")
            print(f"Your age is {first}.")
        else:
            print("Please enter your complete information.")
    elif second.isnumeric():
        second = int(second)
        if 0<= second <= 120:
            print(f"Your name is {first}.")
            print(f"Your age is {second}.")
        else:
            print("Please enter your complete information.")
    else:
        print("Please enter your complete information.")

