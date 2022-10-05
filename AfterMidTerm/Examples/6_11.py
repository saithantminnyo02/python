for i, x in enumerate([2, 3, 5, 7]):
    print("%4d\t%4d" % (i, x))

list1 = ["a", "b", "c", "d"]
list2 = [1, 2, 3, 4]

print("-" * 16)

for x, y in zip(list1, list2):
    print("%4s\t%4d" % (x, y))