dna = input("DNA: ")
base = input("base: ")
if base.isalpha() and dna.isalpha():
    count = 0
    for ch in dna:
        print("c: %s" % ch)
        if ch == base:
            print("True if test")
            count += 1
    if count > 0:
        print(f"There are {count} times that the base {base} occur in this DNA.")
    else:
        print("This is not DNA String.")
else:
    print("This is not DNA String.")