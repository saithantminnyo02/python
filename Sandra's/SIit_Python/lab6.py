from operator import truediv


dna = input("DNA: ")
base = input("Base: ")
count = 0
d = True
for i in range(len(dna)):
    if dna[i] not in ["C","A","T","G"] or base not in ["C","A","T","G"]:
        print("This is not DNA String")
        d = False
        break
    else:
        print(f"c: {dna[i]}")
        if base == dna[i]:
            print("True if test")
            count += 1
if d:      
    print(f"There are {count} times that the base {base} occur in this DNA.")
