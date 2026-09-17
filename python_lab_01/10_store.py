#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь кодов товаров

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.
# Каждый товар может лежать в нескольких местах (партиях) с разной ценой.

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Рассчитать на какую сумму лежит каждого товара на складе
# и вывести в формате
#   <товар> - <кол-во> шт, стоимость <сумма> руб

# Пример:
#   Лампа - 27 шт, стоимость 1134 руб

# TODO здесь ваш код
def cost_of_goods(goods, store):
    result = {}
    for item, code in goods.items():
        total_quantity = 0
        total_cost = 0
        for batch in store[code]:
            total_quantity += batch['quantity']
            total_cost += batch['quantity'] * batch['price']
        result[item] = {'quantity': total_quantity, 'cost': total_cost}
            
    return result


def run():
    total = cost_of_goods(goods, store)
    for item, data in total.items():
        print(f"{item} - {data['quantity']} шт, стоимость {data['cost']} руб")


if __name__ == '__main__':
    run()