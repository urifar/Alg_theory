from importlib import import_module

import pytest

distance = import_module('python_lab_01.00_distance')
circle = import_module('python_lab_01.01_circle')
operations = import_module('python_lab_01.02_operations')
movies = import_module('python_lab_01.03_favorite_movies')
family = import_module('python_lab_01.04_my_family')
zoo = import_module('python_lab_01.05_zoo')
songs = import_module('python_lab_01.06_songs_list')
secret = import_module('python_lab_01.07_secret')
garden = import_module('python_lab_01.08_garden')
shopping = import_module('python_lab_01.09_shopping')
store = import_module('python_lab_01.10_store')


# --- 00_distance -------------------------------------------------------------

def test_calculate_distances():
    # египетский треугольник 3-4-5: гипотенуза ровно 5, без погрешности
    sites = {'A': (0, 0), 'B': (3, 4)}
    result = distance.calculate_distances(sites)

    assert result['A']['B'] == 5
    assert result['B']['A'] == 5


def test_distance_to_self_is_zero():
    sites = {'A': (10, 20), 'B': (30, 40)}
    result = distance.calculate_distances(sites)

    assert result['A']['A'] == 0
    assert result['B']['B'] == 0


# --- 01_circle ---------------------------------------------------------------

def test_circle_area():
    # 3.1415926 * 42 ** 2 = 5541.7693464, округление до 4 знаков
    assert circle.calc_circle_area(42) == pytest.approx(5541.7693)


def test_point_inside_circle():
    # расстояние от (23, 34) до центра ≈ 41.05 < 42
    assert circle.is_inside_circle((23, 34), 42) is True


def test_point_outside_circle():
    # расстояние от (30, 30) до центра ≈ 42.43 > 42
    assert circle.is_inside_circle((30, 30), 42) is False


def test_point_on_circle_border():
    # точка ровно на окружности: сравнение строгое, поэтому False
    assert circle.is_inside_circle((42, 0), 42) is False


# --- 02_operations -----------------------------------------------------------

def test_formula_for_9():
    assert operations.formula_for_9() == 9


def test_formula_for_25():
    assert operations.formula_for_25() == 25


# --- 03_favorite_movies ------------------------------------------------------

def test_selected_movies():
    result = movies.get_selected_movies(movies.my_favorite_movies)

    assert result['first'] == 'Терминатор'
    assert result['last'] == 'Назад в будущее'
    assert result['second'] == 'Пятый элемент'
    assert result['second_from_end'] == 'Чужие'


def test_selected_movies_without_commas():
    result = movies.get_selected_movies(movies.my_favorite_movies)

    for value in result.values():
        assert ',' not in value


# --- 04_my_family ------------------------------------------------------------

def test_father_height():
    heights = [['Мать', 165], ['Отец', 180], ['Я', 187]]

    assert family.get_father_height(heights) == 180


def test_father_not_found():
    heights = [['Мать', 165], ['Сестра', 160]]

    assert family.get_father_height(heights) is None


def test_total_family_height():
    heights = [['Мать', 165], ['Отец', 180], ['Я', 187]]

    assert family.total_height_calc(heights) == 532


# --- 05_zoo ------------------------------------------------------------------
# списки изменяются на месте, поэтому в каждом тесте свежие данные

def test_add_bear():
    animals = ['lion', 'kangaroo', 'elephant', 'monkey']

    assert zoo.add_bear(animals) == [
        'lion', 'bear', 'kangaroo', 'elephant', 'monkey',
    ]


def test_add_birds():
    animals = ['lion', 'kangaroo']
    birds = ['rooster', 'ostrich', 'lark']

    assert zoo.add_birds(animals, birds) == [
        'lion', 'kangaroo', 'rooster', 'ostrich', 'lark',
    ]


def test_remove_elephant():
    animals = ['lion', 'elephant', 'monkey']

    assert zoo.remove_elephant(animals) == ['lion', 'monkey']


def test_find_cage():
    # состояние зоопарка после всех трёх операций
    animals = [
        'lion', 'bear', 'kangaroo', 'monkey', 'rooster', 'ostrich', 'lark',
    ]

    assert zoo.find_cage(animals, 'lion') == 1
    assert zoo.find_cage(animals, 'lark') == 7


# --- 06_songs_list -----------------------------------------------------------

def test_total_time_from_list():
    # 4.9 + 4.20 + 5.83
    result = songs.total_time_list(
        songs.violator_songs_list,
        ['Halo', 'Enjoy the Silence', 'Clean'],
    )

    assert result == 14.93


def test_total_time_from_dict():
    # 4.43 + 4.88 + 4.18
    result = songs.total_time_dict(
        songs.violator_songs_dict,
        ['Sweetest Perfection', 'Policy of Truth', 'Blue Dress'],
    )

    assert result == 13.49


def test_unknown_song_is_skipped():
    result = songs.total_time_dict(songs.violator_songs_dict, ['Halo', 'Нет такой'])

    assert result == 4.3


# --- 07_secret ---------------------------------------------------------------

def test_decode_secret_message():
    result = secret.decode_secret_message(secret.secret_message)

    assert result == 'в бане веник дороже денег'


# --- 08_garden ---------------------------------------------------------------

def test_garden_flower_sets():
    result = garden.analyze_flowers(garden.garden, garden.meadow)

    assert result['all'] == {
        'ромашка', 'роза', 'одуванчик', 'гладиолус',
        'подсолнух', 'клевер', 'мак',
    }
    assert result['both'] == {'ромашка', 'одуванчик'}
    assert result['garden_only'] == {'роза', 'гладиолус', 'подсолнух'}
    assert result['meadow_only'] == {'клевер', 'мак'}


def test_garden_sets_have_no_duplicates():
    result = garden.analyze_flowers(('роза', 'роза', 'мак'), ('мак',))

    assert result['all'] == {'роза', 'мак'}


# --- 09_shopping -------------------------------------------------------------

def test_two_cheapest_shops_per_product():
    result = shopping.build_sweets_dict(shopping.shops)

    for shops_list in result.values():
        assert len(shops_list) == 2


def test_cheapest_shop_goes_first():
    result = shopping.build_sweets_dict(shopping.shops)

    assert result['печенье'] == [
        {'shop': 'пятерочка', 'price': 9.99},
        {'shop': 'ашан', 'price': 10.99},
    ]
    assert result['конфеты'][0] == {'shop': 'магнит', 'price': 30.99}


# --- 10_store ----------------------------------------------------------------

def test_store_single_batch():
    # Лампа: 27 шт по 42 руб = 1134 руб (пример из условия)
    result = store.cost_of_goods(store.goods, store.store)

    assert result['Лампа'] == {'quantity': 27, 'cost': 1134}


def test_store_several_batches():
    # Стул: 50*100 + 12*95 + 43*97 = 10311 руб, всего 105 шт
    result = store.cost_of_goods(store.goods, store.store)

    assert result['Стул'] == {'quantity': 105, 'cost': 10311}


def test_store_covers_all_goods():
    result = store.cost_of_goods(store.goods, store.store)

    assert set(result.keys()) == {'Лампа', 'Стол', 'Диван', 'Стул'}