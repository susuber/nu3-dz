'''
(МОДУЛЬ 3) В проекте создать новый модуль 3seq.py. Задание:

Пользователь вводит элементы 1-го списка (по очереди как в МОДУЛЬ 1 или вместе как в МОДУЛЬ 2)
Затем он вводит элементы 2-го списка
Удалить из первого списка элементы присутствующие во 2-ом и вывести результат на экран
Пример работы: Введите элементы 1-го списка: 1,2,3,4,5
Введите элементы 2-го списка: 2,5
Результат: 1,3,4

Предлагаю проверить работу программы на разных списках, чтобы убедиться что она работает верно

'''

def main():
    data = input('Введите элементы 1 списка через разделитель (Варианты разделителей , / ; : .): ')
    list_1 = split_data(data=data)

    data = input('Введите элементы 2 списка через разделитель (Варианты разделителей , / ; : .): ')
    list_2 = split_data(data=data)

    print('Результат:')
    print([num for num in list_1 if num not in list_2])


def split_data(data: str) -> list:
    data = data.split(',')
    if len(data) == 1:
        data = data[0].split('/')
    if len(data) == 1:
        data = data[0].split(';')
    if len(data) == 1:
        data = data[0].split(':')
    if len(data) == 1:
        data = data[0].split('.')

    return data


if __name__ == '__main__':
    main()