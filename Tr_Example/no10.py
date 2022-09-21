dna = input("DNA: ")
base = input("base: ")

if dna.isalpha() and base.isalpha():
    counter = 0
    for c in dna:
        print("c: ", c)
        if c == base:
            print("True if test")
            counter += 1
    print("There are %d times that the base %s occur in this DNA." % (counter, base))
else:
    print("This is not DNA String")