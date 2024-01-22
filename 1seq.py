'''
(МОДУЛЬ 1) Создать новый проект, в нем создать модуль 1seq.py. Задание:
Пользователь вводит количество элементов будущего списка
После этого по очереди по одной вводит любые цифры
Сохранить цифры в список
Отсортировать список по возрастанию и вывести на экран
Пример работы: Введите количество элементов: 3
Введите 1 элемент: 5
Введите 2 элемент: 2
Введите 3 элемент: 4
Вывод: [2, 4, 5]
'''

def main():
    print("Введите количество элементов: ", end='')
    num = count()
    num_list = []

    for i in range(num):
        print(f"Введите {i + 1} элемент: ", end='')
        num_list.append(count())

    print(f"Список: {num_list}")


def count() -> int:
    while True:
        num = input()
        if num.isdigit():
            return int(num)
        else:
            print("Неверный ввод")


if __name__ == '__main__':
    main()