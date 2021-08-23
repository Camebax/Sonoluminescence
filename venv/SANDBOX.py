import math, random, winsound
import matplotlib.pyplot as plt
from Functions_1_1_M_C import *
from Functions_1_1 import *
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
n_wox = 51
angles_cube = []
dots_M_C = []
x = []
for _ in range(1,50,2):
    angles_cube.append(cube(n = n_wox ,x_source = _, y_source = round(n_wox/2)-1, z_source = round(n_wox/2)-1))
    dots_M_C.append(MonteCarlo(n = n_wox, x_source= _, y_source = round(n_wox/2)-1, z_source = round(n_wox/2)-1))
    x.append(_)
plt.plot(x,angles_cube, 'r',linewidth=0.7)
plt.plot(x,dots_M_C, 'g',linewidth=0.7)
plt.xlabel('Положение источника по оси X')
plt.ylabel('Часть лучей, испускаемых источником, проходящая через препарат')
plt.xlim([0,51])
plt.ylim([0,0.2])
plt.grid()
plt.show()

'''
print(cube(n, x_source = round(n/2)-1, y_source = round(n/2)-1, z_source = round(n/2)-1))
#print(n,ratio)
down_slice = np.loadtxt('cell_down.txt')
up_slice = np.loadtxt('cell_up.txt')
left_slice = np.loadtxt('cell_left.txt')
right_slice = np.loadtxt('cell_right.txt')
back_slice = np.loadtxt('cell_back.txt')
front_slice = np.loadtxt('cell_front.txt')


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
z,y,x = potential.nonzero()
cube = ax.scatter(x, y, z, zdir='z', c=potential[z,y,x], cmap=plt.cm.rainbow)  # Plot the cube
cbar = fig.colorbar(cube, shrink=1, aspect=1)                                # Add a color bar which maps values to colors.
#Сохранение наружных слоев ячейки cell
np.savetxt('cell_down.txt',cell[:,:,0])
np.savetxt('cell_up.txt',cell[:,:,n-1])
np.savetxt('cell_left.txt',cell[:,0,:])
np.savetxt('cell_right.txt',cell[:,n-1,:])
np.savetxt('cell_back.txt',cell[0,:,:])
np.savetxt('cell_front.txt',cell[n-1,:,:])
'''