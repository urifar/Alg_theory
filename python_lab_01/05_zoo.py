#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть список животных в зоопарке
zoo = ['lion', 'kangaroo', 'elephant', 'monkey']

# Посадите медведя (bear) между львом и кенгуру
# и выведите список на консоль
# TODO здесь ваш код
def add_bear(zoo):
    zoo.insert(1, 'bear')
    return zoo


# Добавьте птиц из списка birds в последние клетки зоопарка
birds = ['rooster', 'ostrich', 'lark']
# и выведите список на консоль
# TODO здесь ваш код
def add_birds(zoo, birds):
    zoo.extend(birds)
    return zoo
# Уберите слона (elephant) из зоопарка
# и выведите список на консоль
# TODO здесь ваш код
def remove_elephant(zoo):
    zoo.remove('elephant')
    return zoo
# Выведите на консоль в какой клетке сидит лев (lion) и жаворонок (lark).
# Номера при выводе должны быть 1-индексированными (первая клетка - номер 1).
# TODO здесь ваш код
def find_cage(zoo, animal):
    return (zoo.index(animal) + 1)


def run():
    print(add_bear(zoo))
    print(add_birds(zoo, birds))
    print(remove_elephant(zoo))
    print(f'Лев сидит в клетке {find_cage(zoo, "lion")}')
    print(f'Жаворонок сидит в клетке {find_cage(zoo, "lark")}')


if __name__ == '__main__':
    run()
