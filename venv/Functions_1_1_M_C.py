import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import random, math, time

def get_power_flow(src_cord, point_cord, n, power, cell_size,
                   lda, abs_coeff):
    '''Считает удельную мощность в точке с координатой point_cord[] от источника с координатами src_cord для длины волны lda'''
    distance = ((src_cord[0] - point_cord[0])**2 +
                (src_cord[1] - point_cord[1])**2 +
                (src_cord[2] - point_cord[2])**2)**0.5 # Находим расстояние от источника до заданной точки
    distance = (distance/n) * cell_size
    try:
        power_flow = power/(4*3.14159*distance**2) * 10**(-abs_coeff * distance) # Вводим коэффициент поглощения среды в расчёт

    except ZeroDivisionError: # На случай вокселя-источника, чтобы избежать деления на нулевое расстояние
        power_flow = 0
        pass
    return power_flow

# Функция для цветного вывода заданной грани
def show_edge(edge):
    fig, dots = plt.subplots()  # Задаём подразделы графика для вывода
    fig.set_figwidth(6.8)
    fig.set_figheight(10)
    dots.pcolormesh(edge, cmap='rainbow', vmin=0, vmax=10)  # Задаём имя объекта для вывода (первое в скобках) и цветовую гамму
    plt.show()

# Функция для цветного вывода всего кубика
def show_cube_3D(array):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    z, y, x = array.nonzero()
    cube = ax.scatter(x, y, z, zdir='z', c=array[z, y, x], cmap=plt.cm.rainbow)  # Plot the cube
    cbar = fig.colorbar(cube, shrink=0.06, aspect=5)  # Add a color bar which maps values to colors.
    plt.show()

def MonteCarlo(n = 51, n_iter = 10000,
         x_source = 3, y_source = 3, z_source = 3): # Возвращает 3D массив cell с распределением излучения на наружных слоях
    start_time = time.time()
    cell = np.zeros((n, n, n)) # Задаём ячейку (3-мерный массив из нулей)
    h = 0.45
    for _ in range(n_iter):
        x = x_source
        y = y_source
        z = z_source
        theta = math.acos(random.uniform(-1,1))
        phi = random.uniform(0,2*math.pi)
        sin_theta = math.sin(theta)
        cos_theta = math.cos(theta)
        sin_phi = math.sin(phi)
        cos_phi = math.cos(phi)
        while (x < n-1) and (x > 0) and (y < n-1) and (y > 0) and (z < n-1) and (z > 0):
            x += (sin_theta * cos_phi) * h
            y += (sin_theta * sin_phi) * h
            z += (cos_theta) * h
        cell[round(x),round(y),round(z)] += 1

    '''Часть Монте-Карло и углов'''
    r = round(n/2)  # радиус кругового клеточного слоя
    innerdot = 0
    angles = np.zeros((n,n))
    angle_weight = np.zeros((n,n))
    x0 = round(n/2)-1 # координаты центра круглого клеточного слоя
    y0 = round(n/2)-1

    for x in range(0, n): # расчет отношения числа точек в нужной области к их общему числу
        for y in range(0, n):
            if (x - x0) ** 2 + (y - y0) ** 2 <= r ** 2:  # условие попадения в круг на дне ячейки
                innerdot += cell[x, y, 0]
                '''Часть расчета углов падения'''
                alpha = math.atan(math.sqrt((x-x_source)**2+(y-y_source)**2)/z_source)
                angles[x,y] = alpha
                angle_weight[x, y] = alpha * cell[x, y, 0]

    dots_in_area = innerdot/np.sum(cell)
    #print('Часть точек, попавших в нужную область:', dots_in_area)
    np.savetxt('angle_weight.txt', angle_weight)
    np.savetxt('angles.txt', angles)
    np.savetxt('cell_down.txt', cell[:, :, 0])
    #print('Средний угол падения:', (np.sum(angle_weight) / innerdot) / math.pi * 180)
    runtime = time.time() - start_time
    #print("--- %s seconds ---" % (runtime))  # Вывод времени работы программы
    return dots_in_area