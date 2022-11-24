
dic = {}
for i in range(0, 10):
  i = str(i)
  dic[i] = []
  
integers = input("Integer inputs: ").split(" ")
for integer in integers:
  if integer.isnumeric() and integer != "0":
    last = integer[-1]
    if last in dic:  
        dic[last].append(int(integer))

for key, value in dic.items():
  if dic[key]:
    sortedValue = sorted(value)
    print(f"Group {key}, Total {len(sortedValue)}, Values: {sortedValue}")


