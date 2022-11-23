dic = {}
while True:
    id, score = input("Enter student ID and score: ").split(" ")
    if id == "done" and score == "0":
        break
    if len(id) == 4:
        score = int(score)
        if 0 <= score <= 100:
            if id not in dic:
                dic[id] = score
            else:
                print("The ID is already recorded!")
        else:
            print("Invalid score!")
    else:
        print("Invalid ID format!")

print("List:")
if dic:
    for key, value in sorted(dic.items()):
        print(f"{key}\t{value}")
    count = len(dic)
    avg = sum(dic.values()) / count
    print("There are %d student(s). The average score is %.2f points." % (count, avg))
else:
    print("> no score is recorded!")