import numpy as np

a = np.arange(1, 11, 1)
print(a)
b = np.reshape(a, (2, 5))
print(b)
c = np.reshape(a, (5, 2))
print(c)
d = np.reshape(a, (10, 1))
print(d)