from operator import itemgetter

students = []
for i in range(2):
    sid = input("Enter a student id: ")
    score = input("Enter a score: ")
    if sid.isnumeric() and score.isnumeric():
        students.append([sid, int(score)])
    else:
        print("Skip an invalid input")
print(students)
print('=' * 20)
print(sorted(students))
print('=' * 20)
print(sorted(students, key=itemgetter(1)))