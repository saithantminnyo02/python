def penny():
    global n
    n = 10
    print("Penny is", n, "years old.")

def amy():
    print("Amy is", n+3, "years old.")

n = 15
amy()
print("Lenoard is", n, "years old.")
penny()
print("Sheldon is", n+5, "years old.")
