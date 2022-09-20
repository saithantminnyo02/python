score = input("Enter your score. ")
if score.isnumeric():
    score = int(score)
    if 0 <= score <= 100:
        if 80 <= score <= 100:
            print("A")
        elif 70 <= score < 80:
            print("B")
        elif 60 <= score < 70:
            print("C")
        elif 40 <= score < 60:
            print("D")
        else:
            print("F")
    else:
        print("Error")
else:
    print("Error")