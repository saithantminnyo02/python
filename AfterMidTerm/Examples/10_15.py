import numpy as np

a = np.array([[5, 15, 56], [-4, -11, -41], [-1, -3, -11]])
b = np.array([[35], [-26], [-7]])
# x = 1, y = 2, z = 0
if np.linalg.det(a) != 0:
    c = np.linalg.inv(a)
    # c = (1/np.linalg.det(a)) * c
    print(c)
    ans = np.matmul(c, b)
    print(ans)
    print(b)