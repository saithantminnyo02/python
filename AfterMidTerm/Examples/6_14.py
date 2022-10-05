s = input("Input a string: ")
consonants = [ch for ch in s if ch.isalpha() and ch not in "aeiou"]
vowels = [ch for ch in s if ch in "aeiou"]
print("The number of consonants =", len(consonants))
print("The number of vowels =", len(vowels))
