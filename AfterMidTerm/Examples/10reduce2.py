import numpy as np

b = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(b)
print(np.sum(b))
print(np.sum(b, axis = 1))
print(np.sum(b, axis = 0))