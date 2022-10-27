num_dict = {}
num_list = input("Input: ").split(" ")
for num in num_list:
    if num.isnumeric():
        num = int(num)
        if num not in num_dict:
            num_dict[num] = 1
        else:
            num_dict[num] += 1

for key, value in num_dict.items():
    if key == value:
        isGood = True
    else:
        isGood = False
        break

if isGood:
    print("Output: good sequence")
else:
    print("Output: not good sequence")
