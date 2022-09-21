alphabet = "abcdefghijklmnopqrstuvwxyz"
ch1 = input("Give me a character: ")
ch2 = input("Give me another character: ")

if ch1.isalpha() and ch2.isalpha():
    if ch1 > ch2:
        order1, order2 = ch2, ch1
    else:
        order1, order2 = ch1, ch2
    for ch in alphabet:
        if order1 <= ch <= order2:
            print(f"{ch}", end="")
    print()
else:
    print("You need to input two characters.")