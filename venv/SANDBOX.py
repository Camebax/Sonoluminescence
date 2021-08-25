import math, random, winsound
import matplotlib.pyplot as plt
from Functions import *
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


n_wox = 51
angles_cube = []
dots_M_C = []
x = []


for _ in range(1,50,2):
    angles_cube.append(cube_geometry(n = n_wox ,x_source = _, y_source = round(n_wox/2)-1, z_source = round(n_wox/2)-1))
    dots_M_C.append(cube_monte_carlo(n = n_wox, x_source= _, y_source = round(n_wox/2)-1, z_source = round(n_wox/2)-1))
    x.append(_)


plt.plot(x,angles_cube, 'r',linewidth=0.7)
plt.plot(x,dots_M_C, 'g',linewidth=0.7)
plt.xlabel('Положение источника по оси X')
plt.ylabel('Часть лучей, испускаемых источником,\n проходящая через препарат')
plt.xlim([0,51])
plt.ylim([0,0.2])
plt.grid()
plt.show()
