from operator import itemgetter
dic = {}
while True:
    num = input("Input: ")
    if num == "done":
        break
    
    if num.isnumeric():
        num = int(num)
        if 1 <= num <= 1000:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1
        else:
            print("ERROR")
    else:
        print("ERROR")

print("----SUMMARY----")
if dic:
    for key, value in sorted(dic.items()):
        print(f"{key}  {value}")
else:
    print("The list is empty")