animals = {}
while True:
    animal = input("Input (DONE = exit): ")
    if animal == "DONE":
        break
    else:
        keys_lower = [key.lower() for key in animals.keys()]
        print(keys_lower)
        if animal.lower() not in keys_lower:
            animals[animal] = 1
        else:
            for key in animals.keys():
                if key.lower() == animal.lower():
                    animals[key] += 1

for key, value in animals.items():
    print(key, "=", value)