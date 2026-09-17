#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь магазинов с распродажами

shops = {
    'ашан': [
        {'name': 'печенье', 'price': 10.99},
        {'name': 'конфеты', 'price': 34.99},
        {'name': 'карамель', 'price': 45.99},
        {'name': 'пирожное', 'price': 67.99}
    ],
    'пятерочка': [
        {'name': 'печенье', 'price': 9.99},
        {'name': 'конфеты', 'price': 32.99},
        {'name': 'карамель', 'price': 46.99},
        {'name': 'пирожное', 'price': 59.99}
    ],
    'магнит': [
        {'name': 'печенье', 'price': 11.99},
        {'name': 'конфеты', 'price': 30.99},
        {'name': 'карамель', 'price': 41.99},
        {'name': 'пирожное', 'price': 62.99}
    ],
}

# Создайте словарь цен на продукты следующего вида (писать прямо в коде)
# sweets = {
#     'печенье': [
#         {'shop': 'пятерочка', 'price': 9.99},
#         {'shop': 'ашан', 'price': 10.99},
#     ],
#     ...
# }
# Указать надо только по 2 магазина с минимальными ценами


def build_sweets_dict(shops):
    sweets = {

    }
    for shop, products in shops.items():
        for product in products:
            name = product['name']
            price = product['price']
            if name not in sweets:
                sweets[name] = []
            sweets[name].append({'shop': shop, 'price': price})

    for name in sweets:
        sweets[name] = sorted(sweets[name], key=lambda x: x['price'])[:2]
    return sweets


def run():
    sweets = build_sweets_dict(shops)
    print(sweets)


if __name__ == '__main__':
    run()