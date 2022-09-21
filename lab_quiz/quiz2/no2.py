s = input("Please enter your informaiton: ").split(",")
input1, input2 = s[0], s[1]
input1, input2 = input1.strip(), input2.strip()
if (input1.isnumeric() or input2.isnumeric()) and (input1.isalpha() or input2.isalpha()):
    age, name = 0, ""
    if input1.isnumeric():
        age = int(input1)
    elif input2.isnumeric():
        age = int(input2)
    if 0 <= age <= 120:
        if input1.isalpha():
            name = input1
        elif input2.isalpha():
            name = input2
        print("Your name is %s." % name)
        print("Your age is %d." % age)
    else:
        print("Please enter your complete informaiton.")

else:
    print("Please enter your complete informaiton.")