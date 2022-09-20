import numpy as np
import matplotlib.pyplot as plt

x1 = np.arange(-5, 1, 0.1)
x2 = np.arange(1, 5.1, 0.1)
y1 = 7 - (4 * x1)
y2 = x2**2 + 2
plt.plot(x1, y1, color="blue", linestyle="dotted", linewidth=2)
plt.plot(x2, y2, color="yellow", linestyle="dashed", linewidth=2)
plt.show()