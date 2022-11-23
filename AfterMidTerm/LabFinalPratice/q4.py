from operator import itemgetter
dic = {}
while True:
    data = input("Input: ").split(" ")
    name = data[0]
    if name == "done":
        break
    score = data[1]
    if(score.isnumeric() and int(score) >= 0):
        score = int(score)
        if name not in dic:
            dic[name] = score
        else:
            print("Duplicated player")
    else:
        print("Invalid input")

if dic:
    count = 1
    avg = sum(dic.values()) / len(dic)
    for key, value in sorted(dic.items(), key=itemgetter(1), reverse=True): 
        print(f"{key}\t{value}", end="")
        if count == 1:
            print("\tGold")
        else:
            if value > avg:
                print("\tSilver")
            else:
                print()
        count += 1
else:
    print("No player")
        