import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-10, 10, 0.1)
y = np.sqrt(x**2 * (x + 1))
plt.plot(x, y, linewidth=2, linestyle="dashed", color="blue")
plt.show()
