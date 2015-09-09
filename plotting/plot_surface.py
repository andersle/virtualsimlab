"""Simple 3D plot"""
# pylint: disable=C0103
from __future__ import print_function
from mpl_toolkits.mplot3d import Axes3D  # for projection='3d'
import matplotlib.pyplot as plt
import numpy as np
import matplotlib

try:
    matplotlib.style.use('bmh')
except AttributeError:
    print('Could not load style, update matplotlib!')

fig = plt.figure()
ax1 = fig.add_subplot(111, projection='3d')

TIME = np.linspace(0, 1, 100)

x1 = np.ones(len(TIME))
y1 = (TIME / 2)**2
radius = 1.0 - 0.5 * TIME**2
x2 = x1 - np.sin(np.pi * TIME)
y2 = radius * np.cos(np.pi * TIME)
z = TIME

xmat = np.vstack((x1, x2)).T
ymat = np.vstack((y1, y2)).T
ymat = ymat - 0.5  # centering
xmat = xmat - 1.0  # centering
zmat = np.vstack((z, z)).T
ax1.plot_surface(xmat, ymat, zmat, rstride=5, cstride=1, cmap='bwr')
ax1.set_xlim(-1.5, 1.5)
ax1.set_ylim(-1.5, 1.5)
ax1.set_xlabel('$x$')
ax1.set_ylabel('$y$')
ax1.set_zlabel('$z$')

ax1.view_init(20, 20)
plt.show()
