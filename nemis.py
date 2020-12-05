
goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.

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



divan_cost = store['34567'][0]["quantity"] * store['34567'][0]["price"] +\
             store['34567'][1]["quantity"] * store['34567'][1]["price"]
divan_quantity = store['34567'][0]["quantity"] + store['34567'][1]["quantity"]
print('Диван', divan_quantity  , 'шт, стоимость', divan_cost , 'руб')



