
# Функция для цветного вывода заданной грани из Functions_1_1)
def show_edge(edge):
    fig, dots = plt.subplots()  # Задаём подразделы графика для вывода
    fig.set_figwidth(6.8)
    fig.set_figheight(10)
    dots.pcolormesh(edge, cmap='rainbow', vmin=0,
                    vmax=10)  # Задаём имя объекта для вывода (первое в скобках) и цветовую гамму
    plt.show()


def get_power_flow(src_cord,
                   point_cord,
                   n,
                   power,
                   cell_size,
                   lda,
                   abs_coeff):
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


'''
print(cube_geometry(n, x_source = round(n/2)-1, y_source = round(n/2)-1, z_source = round(n/2)-1))
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