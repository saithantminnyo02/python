import numpy as np

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8],
        [9, 10, 11, 12], [13, 14, 15, 16]])
b = np.identity(4)
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[5, -1], [1, 0], [-2, 3]])

print(np.matmul(a, b))
print(np.matmul(c, d))