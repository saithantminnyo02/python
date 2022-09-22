start = input("Give me a character:")
end = input("Give me another character:")
list= "abcdefghijklmnopqrstuvwxyz"
if start.isalpha() and end.isalpha and start.islower() and end.islower():
    if start > end:
        s = end
        e = start
    else:
        s = start
        e = end
    for i in range (len(list)):
        if s <= list[i] and e >= list[i]:
            print(list[i], end="")
        else:
            break
    print(" ")
else:
    print("You need to input two characters.")


