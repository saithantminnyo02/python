import random as r
digit = input("Digit: ")
if digit.isnumeric():
    digit = int(digit)
    max = int("9" * digit)
    rand = r.randint(0, max)
    print(f"%d-digit random OTP = %0{digit}d" %(digit, rand))
