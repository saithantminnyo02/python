import numpy as np
import math

def calDistance(i, j):
  ans = (i[0] - j[0]) ** 2 + (i[1] - j[1]) ** 2 + (i[2] - j[2]) ** 2
  return math.sqrt(ans)

arr = []
for i in range(1, 4):
  a, b, c = input("Input coordinate of P%d: " % i).split(" ")
  arr.append([int(a), int(b), int(c)])

arr = np.reshape(arr, (3, 3))
distances = []
for count in range(3):
  a = count
  if count == 2:
    b = 0
  else:
    b = count + 1

  distances.append(calDistance(arr[a], arr[b]))

print("Output:")
print("The longest distance = %.2f" % np.max(distances))
