#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = ['Мать', 'Отец', 'Бабушка', 'Дедушка', 'Брат', 'Сестра', 'Я']

# список списков приблизительного роста членов вашей семьи
my_family_height = [
    ['Мать', 165],
    ['Отец', 180],
    ['Бабушка', 160],
    ['Дедушка', 175],
    ['Брат', 170],
    ['Сестра', 160],
    ['Я', 187]
]

# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см

# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см

# TODO здесь ваш код
def get_father_height(family_height):
    for member in family_height:
        if member[0] == 'Отец':
            return member[1]
    return None


def total_height_calc(family_height):
    total_height = sum(member[1] for member in family_height)
    return total_height


def run():
    print(f'Рост отца - {get_father_height(my_family_height)} см')
    print(f'Общий рост моей семьи - {total_height_calc(my_family_height)} см')


if __name__ == '__main__':
    run()