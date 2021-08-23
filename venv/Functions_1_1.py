import math
import random
import time

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits import mplot3d


def get_power_flow(src_cord, point_cord, n, power, cell_size,
                   lda, abs_coeff):
    """Считает удельную мощность в точке с координатой point_cord[] от источника с координатами src_cord для длины
    волны lda """
    distance = ((src_cord[0] - point_cord[0]) ** 2 +
                (src_cord[1] - point_cord[1]) ** 2 +
                (src_cord[2] - point_cord[2]) ** 2) ** 0.5  # Находим расстояние от источника до заданной точки
    distance = (distance / n) * cell_size
    try:
        power_flow = power / (4 * 3.14159 * distance ** 2) * 10 ** (
                    -abs_coeff * distance)  # Вводим коэффициент поглощения среды в расчёт

    except ZeroDivisionError:  # На случай вокселя-источника, чтобы избежать деления на нулевое расстояние
        power_flow = 0
        pass
    return power_flow


# Функция для цветного вывода заданной грани
def show_edge(edge):
    fig, dots = plt.subplots()  # Задаём подразделы графика для вывода
    fig.set_figwidth(6.8)
    fig.set_figheight(10)
    dots.pcolormesh(edge, cmap='rainbow', vmin=0,
                    vmax=10)  # Задаём имя объекта для вывода (первое в скобках) и цветовую гамму
    plt.show()


# Функция для цветного вывода всего кубика
def show_cube_3d(array):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    z, y, x = array.nonzero()
    cube = ax.scatter(x, y, z, zdir='z', c=array[z, y, x], cmap=plt.cm.rainbow)  # Plot the cube
    cbar = fig.colorbar(cube, shrink=0.06, aspect=5)  # Add a color bar which maps values to colors.
    plt.show()


def cube(n=51,
         x_source=25, y_source=25, z_source=25):
    start_time = time.time()
    down_slice = np.zeros((n, n))
    up_slice = np.zeros((n, n))
    left_slice = np.zeros((n, n))
    right_slice = np.zeros((n, n))
    back_slice = np.zeros((n, n))
    front_slice = np.zeros((n, n))
    angle_weight = np.zeros((n, n))
    sum_weight = 0
    '''Перебор всех наружных слоев'''
    for x in range(0, n):
        for y in range(0, n):
            # down_slice
            xa = 0
            ya = 0
            za = - z_source
            xb = x - x_source
            yb = y - y_source
            zb = - z_source
            cos_alpha = (xa * xb + ya * yb + za * zb) / math.sqrt(
                (xa ** 2 + ya ** 2 + za ** 2) * (xb ** 2 + yb ** 2 + zb ** 2))
            distance = math.sqrt((x - x_source) ** 2 + (y - y_source) ** 2 + z_source ** 2)
            down_slice[x, y] = cos_alpha * (1 / distance ** 2)
            angle_weight[x, y] = cos_alpha * down_slice[x, y]
            # up_slice
            xa = 0
            ya = 0
            za = n - 1 - z_source
            xb = x - x_source
            yb = y - y_source
            zb = n - 1 - z_source
            cos_alpha = (xa * xb + ya * yb + za * zb) / math.sqrt(
                (xa ** 2 + ya ** 2 + za ** 2) * (xb ** 2 + yb ** 2 + zb ** 2))
            distance = math.sqrt((x - x_source) ** 2 + (y - y_source) ** 2 + (z_source - n + 1) ** 2)
            up_slice[x, y] = cos_alpha * (1 / distance ** 2)

        for z in range(0, n):
            # left_slice
            xa = 0
            ya = - y_source
            za = 0
            xb = x - x_source
            yb = - y_source
            zb = z - z_source
            cos_alpha = (xa * xb + ya * yb + za * zb) / math.sqrt(
                (xa ** 2 + ya ** 2 + za ** 2) * (xb ** 2 + yb ** 2 + zb ** 2))
            distance = math.sqrt((x - x_source) ** 2 + y_source ** 2 + (z - z_source) ** 2)
            left_slice[x, z] = cos_alpha * (1 / distance ** 2)
            # right_slice
            xa = 0
            ya = n - 1 - y_source
            za = 0
            xb = x - x_source
            yb = n - 1 - y_source
            zb = z - z_source
            cos_alpha = (xa * xb + ya * yb + za * zb) / math.sqrt(
                (xa ** 2 + ya ** 2 + za ** 2) * (xb ** 2 + yb ** 2 + zb ** 2))
            distance = math.sqrt((x - x_source) ** 2 + (y_source - n + 1) ** 2 + (z - z_source) ** 2)
            right_slice[x, z] = cos_alpha * (1 / distance ** 2)
    for y in range(0, n):
        for z in range(0, n):
            # back_slice
            xa = - x_source
            ya = 0
            za = 0
            xb = - x_source
            yb = y - y_source
            zb = z - z_source
            cos_alpha = (xa * xb + ya * yb + za * zb) / math.sqrt(
                (xa ** 2 + ya ** 2 + za ** 2) * (xb ** 2 + yb ** 2 + zb ** 2))
            distance = math.sqrt(x_source ** 2 + (y - y_source) ** 2 + (z - z_source) ** 2)
            back_slice[y, z] = cos_alpha * (1 / distance ** 2)
            # front_slice
            xa = n - 1 - x_source
            ya = 0
            za = 0
            xb = n - 1 - x_source
            yb = y - y_source
            zb = z - z_source
            cos_alpha = (xa * xb + ya * yb + za * zb) / math.sqrt(
                (xa ** 2 + ya ** 2 + za ** 2) * (xb ** 2 + yb ** 2 + zb ** 2))
            distance = math.sqrt((x_source - n + 1) ** 2 + (y - y_source) ** 2 + (z - z_source) ** 2)
            front_slice[y, z] = cos_alpha * (1 / distance ** 2)

    '''Часть Монте-Карло и углов'''
    r = round(n / 2)  # радиус кругового клеточного слоя
    innerdot = 0
    x0 = round(n / 2) - 1  # координаты центра круглого клеточного слоя
    y0 = round(n / 2) - 1
    for x in range(0, n):  # расчет отношения числа точек в нужной области к их общему числу
        for y in range(0, n):
            if (x - x0) ** 2 + (y - y0) ** 2 <= r ** 2:  # условие попадения в круг на дне ячейки
                innerdot += down_slice[x, y]
                sum_weight += angle_weight[x, y]
                # Часть расчета углов падения

    sum_points = np.sum([down_slice, up_slice, left_slice, right_slice, front_slice, back_slice])
    runtime = time.time() - start_time
    print("--- %s seconds ---" % runtime)  # Вывод времени работы программы
    return innerdot / sum_points  # , innerdot_up/sum_points, innerdot_left/sum_points, innerdot_right/sum_points,
    # innerdot_front/sum_points, innerdot_back/sum_points
