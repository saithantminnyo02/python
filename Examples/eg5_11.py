nvows, ncons, nothers = 0, 0, 0
message = "Hi, Alice"
message = message.replace(" ", "")
for ch in message:
    if ch.isalpha():
        if ch in "aeiou":
            print(ch, "is a vowel.")        
            nvows += 1
        else:
            print(ch, "is a consonant.")
            ncons += 1
    else:
        print(ch, "is a other character.")
        nothers += 1
print("%d vowels, %d consonants and %d other characters." % (nvows, ncons, nothers))
