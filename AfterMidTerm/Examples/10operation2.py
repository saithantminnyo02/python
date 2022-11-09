import numpy as np

a = np.identity(3)
b = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
c = np.diag([1, 2, 3, 4])
print(c)

print(a + b)
# print(b * c)