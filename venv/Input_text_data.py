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

# print(get_spectre(filepath))
