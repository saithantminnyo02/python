import numpy as np

d = np.arange(1, 3, 0.5)
print(np.ndim(d), np.shape(d))
e = np.zeros([3, 3])
print(np.ndim(e), np.shape(e))
f = np.ones(4)
print(np.ndim(f), np.shape(f))
g = np.identity(5)
print(np.ndim(g), np.shape(g))
