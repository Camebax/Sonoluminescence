import numpy as np
from Functions import *


def show_2d_array(array, min_val=0, max_val=1):
    fig, dots = plt.subplots()  # Задаём подразделы графика для вывода
    fig.set_figwidth(6.8)
    fig.set_figheight(10)
    dots.pcolormesh(array, cmap='rainbow', vmin=min_val,
                    vmax=max_val)  # Задаём имя объекта для вывода (первое в скобках) и цветовую гамму
    plt.show()


n_wox = 201  # Размер моделируемого куба
r_source = 20  # Диаметр источника света
x0 = round(n_wox / 2)
y0 = round(n_wox / 2)
test_field = np.zeros((n_wox, n_wox))
count = 0
coeff_geom = 0
coeff_m_c = 0


for x in range(0, n_wox):
    for y in range(0, n_wox):
        if (x - x0) ** 2 + (y - y0) ** 2 <= r_source ** 2:
            test_field[x, y] = 1
            # coeff_geom += cube_geometry(n=n_wox, x_source=x, y_source=y, z_source=165)
            coeff_m_c += cube_monte_carlo(n=n_wox, x_source=x, y_source=y, z_source=165)
            count += 1
            print('Расчет точки номер ', count)

print('Итоговый коэффициент (геометрический):', coeff_geom / count)
print('Итоговый коэффициент (MC):', coeff_m_c / count)
show_2d_array(test_field)
