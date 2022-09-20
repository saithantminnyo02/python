year = input("Enter year: ")
if year.isnumeric():
    bol = False
    year = int(year)
    if year % 400 == 0:
        bol = True
    elif year % 100 == 0:
        pass
    elif year % 4 == 0:
        bol = True
    print(bol)
else:
    print("Error.")