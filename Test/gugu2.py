def calVolume(a, b, c):
  return (1 / 3) * (1 / 2) * a * b * c


while True:
  inp = input("Input x,y,z :")
  if inp.lower() == "exit":
    print("Program ended.")
    break

  inp = inp.split(',')

  try:
    x, y, z = float(inp[0]), float(inp[1]), float(inp[2])
    if len(inp) != 3:
      print("Enter 3 values.")
      continue
    elif x <= 0 or y <= 0 or z <= 0:
      print("Invalid input.")
      continue
    else:
      print("Volume of Tetahedron is %.2f cubic unit." % calVolume(x, y, z))
  except:
    print("Invalid input.")
    continue
