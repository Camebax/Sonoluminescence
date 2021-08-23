import math, random
from Functions_1_1 import *
import numpy as np

r = round(n/2) # радиус клеточного слоя
innerdot_down = 0
# расчет отношения числа точек в нужной области к их общему числу
for x in range(0,n):
    for y in range(0,n):
        if (x-round(n/2))**2 + (y-round(n/2))**2 <= r**2: # условие попадения в круг на дне ячейки
            innerdot_down += cell[x, y, 0]

print(innerdot_down, innerdot_up, innerdot_left, innerdot_right, innerdot_back, innerdot_front)
print(innerdot_down + innerdot_up + innerdot_left + innerdot_right + innerdot_back + innerdot_front)


#show_edge(down_slice)
#show_edge(up_slice)
#show_edge(left_slice)
#show_edge(right_slice)
#show_edge(back_slice)
#show_edge(front_slice)