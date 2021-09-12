import math, random, winsound
import matplotlib.pyplot as plt
import venv
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from Functions import *

n_wox = 101
angles_geometry = []
angles_m_c = []
x = []


# Проносит источник по заданному направлению
# и выводит графики зависимости кол-ва излучения, прилетающего в нужную область
def move_source(lim=n_wox - 1, step=4):
    start_time = time.time()
    for _ in range(1, lim, step):
        angles_geometry.append(
            cube_geometry(n=n_wox, x_source=_, y_source=round(n_wox / 2) - 1, z_source=round(n_wox / 2) - 1))
        angles_m_c.append(
            cube_monte_carlo(n=n_wox, x_source=_, y_source=round(n_wox / 2) - 1, z_source=round(n_wox / 2) - 1))
        x.append(_)

    plt.plot(x, angles_geometry, 'r', linewidth=0.7)
    plt.plot(x, angles_m_c, 'g', linewidth=0.7)
    plt.xlabel('Положение источника по оси X')
    plt.ylabel('Часть лучей, испускаемых источником,\n проходящая через препарат')
    plt.xlim([0, lim])
    plt.ylim([0, 6])
    plt.grid()
    runtime = time.time() - start_time
    print("--- %s seconds ---" % runtime, 'Кол-во рассчитанных точек:', lim / step)  # Вывод времени работы программы
    plt.show()


# print(cube_geometry(n = 201, x_source=100, y_source=100, z_source=10))
# print(cube_monte_carlo(n = 201, n_iter=10000, x_source=100, y_source=100, z_source=10))

# move_source()
# show_cube(cube)

print(cube_geometry(n=201, x_source=100, y_source=100, z_source=100))
print(cube_monte_carlo(n=201, x_source=100, y_source=100, z_source=100))
