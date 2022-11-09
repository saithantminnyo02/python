import numpy as np

a = np.array([[1,1,1,-1], [1,1,-1,1], [1,-1,1,1], [-1,1,1,1]])
b = np.identity(4)
if np.linalg.det(a) != 0 and np.linalg.det(b) != 0:
    c = np.linalg.inv(a)
    print("Inverse of a =", c)
    print("ac ="); print(np.matmul(a, c))
    print()
    d = np.linalg.inv(b)
    print("Inverse of b ="); print(d)