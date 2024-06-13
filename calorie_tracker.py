import datetime as dt


# Тестовый пакет данных
list_of_pack = [('1:36:02', 1000),
                ('2:36:02', 2000),
                ('3:36:02', 3000),
                ('4:36:02', 4000)]

# глобальные переменные, в которых храняться: Время, шаги, килокалории, с момента начала суток
store_time, store_steps, store_kkal = 0, 0, 0


storage_date = dict()  # Словарь для хранения пакетов данных


def get_data(package):
    # Функция для распаковки пакета данных и преобразования его элементов в нужный формат
    format = '%H:%M:%S'  # Формат времени в пакете данных
    time = dt.datetime.strptime(package[0], format).time()
    steps = package[1]
    return time, steps


def verify_data(package):
    # Верификация пакета данных, проверка на его целостность и формат
    if len(package) != 2 or (not package[0] or not package[1]) or get_data(package)[0] < dt.time(0):
        return False
    else:
        return True


def get_achivement(distance):
    # Функция выбирает строку "поддержки", которая соответсвует пройденному расстоянию"
    if distance >= 6.5:
        achiv = 'Отличный результат! Цель достигнута.'
    elif distance >= 3.9:
        achiv = 'Неплохо! День был продуктивным.'
    elif distance >= 2:
        achiv = 'Маловато, но завтра наверстаем!'
    else:
        achiv = 'Лежать тоже полезно. Главное — участие, а не победа!'
    return achiv


def show_mess(package):
    # Функция выводит сообщение - сводку , в котором содержится информация о:
    # Текущем времени, кол -ве пройденных шагов, дистанции, сожженых калориях, а также вывод строки "поддержки"
    global store_steps, store_time
    weight = 100  # вес
    height = 190  # рост
    len_of_steps = 0.70  # длинна шага в м
    store_steps += get_data(package)[1]
    store_time += get_data(package)[0].minute + get_data(package)[0].hour * 60
    distance = store_steps * len_of_steps / 1000
    kkal = round((((0.035 * weight) + ((distance / height) ** 2 / height) * (0.029 * weight)) * store_time), 2)
    return f"""
    Время:{package[0]}.
    Колличество шагов за сегодня: {store_steps}.
    Дистанция составила {distance} км.
    Вы сожгли {kkal} ккал.
    {get_achivement(distance)}
"""


def accept_package(package):
    # Функция принимает пакет данных, добавляет его элементы в словарь и обрабатывает полученные данные
    if verify_data(package):
        storage_date[package[0]] = package[1]
        print(show_mess(package))
        print(storage_date)

    else:
        print('Поврежденный пакет данных')


for elem in list_of_pack:
    accept_package(elem)
