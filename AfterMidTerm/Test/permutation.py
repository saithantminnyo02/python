l = input("Enter a comma-separated list: ").split(',')
# l = [1, 2, 3]
for i in l:
    for j in l:
        for k in l:
            
            c = [i, j, k]
            print(f"{c[0]} {c[1]} {c[2]}")
