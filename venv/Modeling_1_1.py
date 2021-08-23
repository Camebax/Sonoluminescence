import numpy as np
import matplotlib.pyplot as plt
from Functions_1_1 import *
from Input_text_data import *

'''Вносим в программу спектры поглощения среды и хлорина'''
file_environment = 'text_files/abs_spec_env.txt'
file_clorine = 'text_files/abs_spec_clorine.txt'
environment_spectre = get_spectre(file_environment) # Словарь со спектром поглощения среды
clorine_spectre = get_spectre(file_clorine) # Словарь со спектром поглощения хлорина

'''Создаём ячейку'''
cell_size = 0.01 #[метров] Физический размер ячейки
n = x = y = z = 100 # Размерность массива ячейки (n*n*n), качество результата
print('Размер одного вокселя - ', cell_size/n, '[м]')
cell = np.zeros((n, n, n)) # Задаём ячейку (3-мерный массив из нулей)

'''Создаём источник'''
src_cord = ask_src_coordinates(n) # Запрашиваем координаты источника
power = 0.8 #[Вт] - мощность источника

abs_coeff = 0.001
lda = 380
add_power(src_cord, n, power, cell_size,
              cell, x, y, z,
              lda, abs_coeff)

#print(cell)
show_slice(cell, 50, n, src_cord, power, cell_size)