#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть строка с перечислением фильмов

my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'

# Выведите на консоль с помощью индексации строки, последовательно:
#   первый фильм
#   последний
#   второй
#   второй с конца

# Запятая не должна выводиться. Переопределять my_favorite_movies нельзя.
# Использовать .split() или .find() или другие методы строки нельзя - пользуйтесь только срезами,
# как указано в задании!

# TODO здесь ваш код
def get_selected_movies(movies):
    movies_dict = {
        'first': movies[0:10],
        'last': movies[-15:],
        'second': movies[12:25],
        'second_from_end': movies[-22:-17]
    }
    return movies_dict
    
    
def run():
    movies = get_selected_movies(my_favorite_movies)
    print(movies['first'])
    print(movies['last'])
    print(movies['second'])
    print(movies['second_from_end'])


if __name__ == '__main__':
    run()