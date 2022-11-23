li = []
count = 0
while count < 9:
    ch = input("Input: ")
    if ch not in ["x", "o"]:
        print("Wrong input")
        break
    else:
        li.append(ch)
    count += 1


if li:
    print("-------")
    for i in range(0,9,3):
        print(f"|{li[i]}|{li[i+1]}|{li[i+2]}|")
    print("-------")
