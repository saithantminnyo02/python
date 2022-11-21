from operator import itemgetter
std_dict = {}
# print(std_dict)
# if "color" in std_dict:
#     print("True")
# std_dict["color"] = "red"
# std_dict["type"] = "sedan"

# for item in std_dict.items():
#     print(item[0])

def printInvalid():
    print("Invalid score!")

while True:
    inputs = input("Enter student name and score: ")
    if "end" in inputs:
        break
    else:
        name, score = inputs.split()
        if name not in std_dict:
            if score.isnumeric():
                score = int(score)
                if 0 <= score <= 100:
                    std_dict[name] = score
                else:
                    printInvalid()
            else:
                printInvalid()
        else:
            print("Duplicate name!")

print("List:")
if not std_dict:
    print("empty list!")
else:
    for item in sorted(std_dict.items(), key=itemgetter(1), reverse=True):
        print(item[0], "\t", item[1])