from ABB_spectre import *
import matplotlib.pyplot as plt

def show_plot(data,
              xlabel = '', ylabel = '', title = ''):
    plt.plot(data.keys(), data.values())
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.grid()
    plt.show()

power = 0.8 #[Вт] - мощность источника
T = 8000 #[К] - температура источника
l = 10**(-6) #[м] - толщина слоя хлорина

print(get_slice_abs_coeff(T, clorine_abs_spectre, l))
print(get_slice_abs_coeff(5000, clorine_abs_spectre, l))

abs_energy_from_T = {}
abs_energy_from_l = {}

for T in range(3000, 12000):
    abs_energy_from_T[T] = get_slice_abs_coeff(T, clorine_abs_spectre, 10**(-6)) # После этого цикла значение T=11999

for _ in range(0, 1000):
    abs_energy_from_l[l] = get_slice_abs_coeff(8000, clorine_abs_spectre, l)
    l += 10**(-9)

T = 8000
show_plot(abs_energy_from_T, 'Температура источника [К]', 'Поглощаемая мощность [Вт]', 'Мощность источника: '+str(power)+'[Вт], '+'Толщина слоя Хлорина:'+str(round(l,9))+'[м]')
show_plot(abs_energy_from_l, 'Толщина слоя Хлорина, [м]', 'Поглощаемая мощность [Вт]','Мощность источника:'+str(power)+'[Вт],'+'Температура источника:'+str(T)+'[К]')

'''
plt.plot(abs_energy_from_l.keys(), abs_energy_from_l.values())
plt.show()
'''