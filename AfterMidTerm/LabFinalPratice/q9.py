dic = {}
while True:
    inp = input("Input: ")
    if inp == "done":
        break
    else:
        type, count = inp.split(" ")
        count = int(count)
        if type not in dic:
            dic[type] = count
        else:
            dic[type] += count

if not dic:
    print("Empty List")
print("###Summary###")
for key, value in dic.items():
    print(f"Total Number of {key} : {value}")