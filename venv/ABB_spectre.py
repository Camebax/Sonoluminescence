pi = 3.1415926535
c = 299792458
h = 6.62607015 * 10 ** (-34)
e = 2.718281828
k = 1.380649 * 10 ** (-23)

filepath = 'text_files/Spectra/abs_spec_ce6.txt'
'''В ТОНИНЫХ ФАЙЛАХ СПЕКТРЫ ПОГЛОЩЕНИЯ ДАНЫ С ШАГОМ 2НМ !!!'''


def get_spectre(filepath):
    """Извлекает спектр из текстового файла по адресу filepath и заносит его в словарь spectre, ключи - длины частот
    в НАНОМЕТРАХ!!! """
    spectre = {}
    with open(filepath) as file_object:
        for line in file_object:  # Перебираем файл по строкам
            line_spl = line.split()
            spectre[int(line_spl[0])] = float(line_spl[1].replace(',', '.'))
    return spectre


def get_slice_abs_coeff(T, clorine_abs_spectre, l=10 ** (-6),  # Эти аргументы, скорее всего, придется менять
                        lda_min=380 * 10 ** (-9), lda_max=800 * 10 ** (-9)):
    """Находит, какую часть от исходной мощности АЧТ с T[К] поглотил слой хлорина толщиной l[м]"""
    sum_energy_in = 0
    sum_energy_out = 0
    lda = lda_min
    while lda <= lda_max:  # Перебор всех длин волн из указанного диапазона
        u_lda = (8 * pi * h * c / lda ** 5) / \
                (e ** (h * c / (lda * k * T)) - 1)  # Спектральная плотность энергии для данной lda
        sum_energy_in += (u_lda * 10 ** (-9)) * 2  # Прибавляем спектральную плотность в данной точке к общей мощности
        lda += (10 ** (-9)) * 2  # Переходим к следующей длине волны (шаг 2 нанометра, так как в Тонином файле он такой)
    lda = lda_min  # Подсчитываем энергию, прошедшую через слой l хлорина на каждой длине волны
    while lda <= lda_max:
        a = clorine_abs_spectre[round(lda * 10 ** 9)]  # Коэффициент поглощения для длины волны lda
        u_lda = (8 * pi * h * c / lda ** 5) / \
                (e ** (h * c / (lda * k * T)) - 1)
        sum_energy_out += (u_lda * 10 ** (-9)) * 2 * (10 ** (-a * l))  # ВЕРНО ЛИ ???
        lda += (10 ** (-9)) * 2  # Умножение на 2, тк шаг по частотам 2нм
    return 1 - sum_energy_out / sum_energy_in  # Возвращаем долю усвоенной хлорином энергии (от исходной)


'''Вносим в программу нужные спектры поглощения'''
file_clorine = 'text_files/spectra/abs_spec_clorine.txt'
clorine_abs_spectre = get_spectre(file_clorine)  # Словарь со спектром поглощения хлорина ("длина волны-значение")

print('Часть поглощенной препаратом энергии:', get_slice_abs_coeff(5000, clorine_abs_spectre, 2 * 10 ** (-6)))
