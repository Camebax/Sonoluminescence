import math
import random
import time

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits import mplot3d
# ЭТАЛОННОЕ ЗНАЧЕНИЕ ДОЛИ СВЕТА, ПРИХОДЯЩИЙ НА КРУГ, ВПИСАННЫЙ В ГРАНЬ, ОТ Т.И. В ЦЕНТРЕ КУБА = 0.14644


# Функция для цветного вывода всего кубика
def show_cube(array):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    z, y, x = array.nonzero()
    cube = ax.scatter(x, y, z, zdir='z', c=array[z, y, x], cmap=plt.cm.rainbow)  # Plot the cube
    plt.show()


def cube_geometry(n=11,
                  x_source=5,  #
                  y_source=5,
                  z_source=5):
    start_time = time.time()
    down_slice = np.zeros((n, n))
    up_slice = np.zeros((n, n))
    left_slice = np.zeros((n, n))
    right_slice = np.zeros((n, n))
    back_slice = np.zeros((n, n))
    front_slice = np.zeros((n, n))
    angles_geometry = np.zeros((n, n))
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
            angles_geometry[x, y] = math.acos(cos_alpha)
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
            up_slice[x, y] = cos_alpha / (distance ** 2)

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

    '''Часть углов (для расчета длины оптического пути лучей)'''
    optic_distance_weight = np.zeros((n, n))
    r = round(n / 2)  # радиус кругового клеточного слоя
    innerdot = 0
    x0 = round(n / 2) - 1  # координаты центра круглого клеточного слоя
    y0 = round(n / 2) - 1
    for x in range(0, n):  # расчет отношения числа точек в нужной области к их общему числу
        for y in range(0, n):
            if (x - x0) ** 2 + (y - y0) ** 2 <= r ** 2:  # условие попадения в круг на дне ячейки
                innerdot += down_slice[x, y]
                optic_distance_weight[x, y] = down_slice[x, y] / math.cos(angles_geometry[x, y])

    sum_points = np.sum([down_slice, up_slice, left_slice, right_slice, front_slice, back_slice])
    runtime = time.time() - start_time
    # print("--- %s seconds ---" % runtime)  # Вывод времени работы программы
    # print('Часть точек, попавших в нужную область (geometry):', innerdot / sum_points)
    # np.savetxt('text_files/angles_geometry.txt', angles_geometry)
    # print('Средний угол падения (geometry):', (np.sum(optic_distance_weight) / innerdot) / math.pi * 180)
    return np.sum(optic_distance_weight) / innerdot


def cube_monte_carlo(n=11, n_iter=5000,  #
                     x_source=5,  #
                     y_source=5,
                     z_source=5):  # Заполняет 3D массив cell с распределением излучения на наружных слоях
    start_time = time.time()
    cell = np.zeros((n, n, n))  # Задаём ячейку (3-мерный массив из нулей)
    h = 0.45
    # Модуль испускания случайных лучей из точки источника
    for _ in range(n_iter):
        x = x_source
        y = y_source
        z = z_source
        theta = math.acos(random.uniform(-1, 1))
        phi = random.uniform(0, 2 * math.pi)
        sin_theta = math.sin(theta)
        cos_theta = math.cos(theta)
        sin_phi = math.sin(phi)
        cos_phi = math.cos(phi)
        while (x < n - 1) and (x > 0) and (y < n - 1) and (y > 0) and (z < n - 1) and (z > 0):
            x += (sin_theta * cos_phi) * h
            y += (sin_theta * sin_phi) * h
            z += cos_theta * h
        cell[round(x), round(y), round(z)] += 1

    '''Часть расчета отношения лучей в нужной области к общему числу лучей'''
    r = round(n / 2)  # радиус кругового клеточного слоя
    innerdot = 0
    optic_distance_weight = np.zeros((n, n))
    angles_m_c = np.zeros((n, n))
    x0 = round(n / 2) - 1  # координаты центра круглого клеточного слоя
    y0 = round(n / 2) - 1
    for x in range(0, n):  # расчет отношения числа точек в нужной области к их общему числу
        for y in range(0, n):
            if (x - x0) ** 2 + (y - y0) ** 2 <= r ** 2:  # условие попадения в круг на дне ячейки
                innerdot += cell[x, y, 0]
                '''Часть углов (для расчета длины оптического пути лучей)'''
                alpha = math.atan(math.sqrt((x - x_source) ** 2 + (y - y_source) ** 2) / z_source)
                angles_m_c[x, y] = alpha
                optic_distance_weight[x, y] = cell[x, y, 0] / math.cos(angles_m_c[x, y])

    dots_in_area = innerdot / np.sum(cell)
    # np.savetxt('text_files/angles_m_c.txt', angles_m_c)
    # print('Средний угол падения (m_c):', (np.sum(optic_distance_weight) / innerdot) / math.pi * 180)
    # print('Часть точек, попавших в нужную область (MC):', dots_in_area)
    runtime = time.time() - start_time
    # print("--- %s seconds ---" % (runtime))  # Вывод времени работы программы
    return np.sum(optic_distance_weight) / innerdot