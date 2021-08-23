import numpy as np
import matplotlib.pyplot as plt
import random, math, time, winsound
from Functions_1_1_M_C import *
from Functions_1_1 import *

n_wox = 119
x_src = round(n_wox/2)-1
y_src = round(n_wox/2)-1
z_src = round(n_wox/2)-1

print(cube(n = n_wox,x_source=x_src,y_source=y_src,z_source=z_src))
#ratio_m_c = MonteCarlo(n,x_source,y_source,z_source)