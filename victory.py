"""
(МОДУЛЬ 4) В проекте создать новый модуль victory.py. Задание
Написать или улучшить программу Викторина из предыдущего дз (Для тренировки предлагаю не пользоваться
никакими библиотеками кроме random)
Есть 10 известных людей и их даты рождения в формате '02.01.1988' ('dd.mm.yyyy') - предлагаю для тренировки
пока использовать строку
Программа выбирает из этих 10-и 5 случайных людей, это можно реализовать с помощью модуля random и функции sample
Пример использования sample:
import random
numbers = [1, 2, 3, 4, 5]

# 2 - количество случайных элементов
result = random.sample(numbers, 2)

print(result) # [5, 1]

После того как выбраны 5 случайных людей, предлагаем пользователю ввести их дату рождения
пользователь вводит дату в формате 'dd.mm.yyyy'

Например, 03.01.2009, если пользователь ответил неверно, то выводим правильный ответ, но уже в следующем виде:
третье января 2009 года, склонением можно пренебречь

В конце считаем количество правильных и неправильных ответов и предлагаем начать снова
"""
import json
from random import choices


class Man:
    def __init__(self, name: str, data: list):
        self.date = int(data[2])
        self.mouth = int(data[1])
        self.year = int(data[0])
        self.name = name

    def check(self, date: [int, int, int]) -> bool:
        if date[0] == self.date and date[1] == self.mouth and date[2] == self.year:
            return True
        else:
            return False

    def get_date(self, dictionary: dict) -> str:
        return f"{dictionary['day'][str(self.date)]} {dictionary['month'][str(self.mouth)]} {self.year}"


def random_men(n: int) -> dict:
    """
    Выборка случайных людей из базы

    :param n: int число случайных людей
    :return: dict словарь с верными датами рождения
    """

    with open('data.json') as json_file:
        data = json.load(json_file)

    new = {}
    for i in choices(list(data.keys()), k=n):
        new[i] = data[i]

    return new


def input_date(person: object) -> list:
    """
    Ввод даты рождения

    :param person: object класс персоны
    :return: list список типа [дата, месяц, год]
    """

    while True:
        date = input(f"Ввдите дату рождения {person.name} в формате дд.мм.гггг (ОТВЕТ {person.date}.{person.mouth}.{person.year}): ")
        date = date.split(sep='.')
        if len(date) != 3:
            print("Неверный ввод")
        elif date[0].isdigit() and date[1].isdigit() and date[2].isdigit():
            date[0] = int(date[0])
            date[1] = int(date[1])
            date[2] = int(date[2])

            if 0 < date[0] <= 31 and 0 < date[1] <= 12:
                return date
            else:
                print("Неверный ввод")
        else:
            print("Неверный ввод")


def input_n() -> int:
    while True:
        n = input('Выберите количество вопросов от 5 до 20: ')
        if n.isdigit():
            n = int(n)
            if 5 <= n <= 20:
                return n
            else:
                print("Неверный ввод, число должно быть от 5 до 20")
        else:
            print("Неверный ввод")


def end_game():
    while True:
        answer = input('Хотите повторить игру (Да/Нет): ')
        answer = answer.lower()
        if answer == 'нет':
            return True
            print("До свидания")
        elif answer == 'да':
            return False
            print("Давайте повторим")
        else:
            print("Неверный ввод, только Да или Нет")


def main():
    with open('date.json', 'r') as f:
        dictionary = json.load(f)
    while True:
        statistics = 0
        n = input_n()

        for key, value in random_men(n).items():
            person = Man(name=key, data=value)
            date = input_date(person=person)
            if person.check(date):
                statistics += 1
                print(person.get_date(dictionary))

        print(f"Колличество верных ответов:     {statistics}")
        print(f"Количество ошибок:              {n - statistics}")
        print(f"Процент правильных ответов:     {round(statistics / n * 100, 2)}")
        print(f"Процент неправильных ответов:   {round((n - statistics) / n * 100, 2)}")

        if end_game():
            break


if __name__ == '__main__':
    main()
