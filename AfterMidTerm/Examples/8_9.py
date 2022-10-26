s = input("Input a string: ")
vowels = {'A': 0, 'E': 0, 'I': 0, 'O': 0, 'U': 0}

for ch in s:
    ch = ch.upper()
    if ch in vowels:
        for key in vowels:
            if ch == key:
                vowels[key] += 1

for key, value in vowels.items():
    print(key, "=", value)