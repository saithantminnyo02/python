l = input("Enter a comma-separated list: ").split(',')
final = []
for i in l:
    for j in l:
        if (i != j):
            c = [i, j]
            print(f"{c[0]} {c[1]}")