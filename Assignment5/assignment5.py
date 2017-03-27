import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import ImageGrid
import numpy as np

a = [1, 2]
b = [2, 4]
t, s = [-6, 6], [1, 2]
fig, ax = plt.subplots()
ax.plot(a, b)
ax.grid(True)


plt.show()