#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# В саду сорвали цветы
garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )

# На лугу сорвали цветы
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )

# Создайте множество цветов, произрастающих в саду и на лугу
# garden_set =
# meadow_set =
# TODO здесь ваш код
def analyze_flowers(garden, meadow):
    garden_set = set(garden)
    meadow_set = set(meadow)
    return {
        'all': garden_set.union(meadow_set),
        'both': garden_set.intersection(meadow_set),
        'garden_only': garden_set.difference(meadow_set),
        'meadow_only': meadow_set.difference(garden_set)
    }


def run():
    result = analyze_flowers(garden, meadow)
    print(f'Все цветы: {result["all"]}')
    print(f'Цветы, растущие и в саду, и на лугу: {result["both"]}')
    print(f'Цветы, растущие только в саду: {result["garden_only"]}')
    print(f'Цветы, растущие только на лугу: {result["meadow_only"]}')


if __name__ == '__main__':
    run()
