#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
def calculate_distances(sites):
    distances = {}

    # TODO здесь заполнение словаря

    for city1, (x1, y1) in sites.items():
        distances[city1] = {}
        for city2, (x2, y2) in sites.items():
            distances[city1][city2] = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

    return distances


def run():
    print(calculate_distances(sites))


if __name__ == '__main__':
    run()