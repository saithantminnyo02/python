from operator import itemgetter
dic = {"ce": 0, "che": 0, "ec": 0, "ie": 0, "me": 0}
li = []
while True:
    student = input("Input: ")
    if student == "done":
        break
    name, major, gpa = student.split(" ")

    gpa = float(gpa)
    if major not in dic or gpa < 0.00 or gpa > 4.00:
        print("ERROR")
    else:
        dic[major] += 1
        li.append([name, major, gpa])

print("----SUMMARY----")
for key, value in dic.items():
    print(key, "=", value)

print("----LIST----")
if li:
    li = sorted(li, key=itemgetter(2), reverse=True)
    for i in li:
        for j in i:
            print(j, end=" ")
        print()
else:
    print("The list is empty.")