import math
print ("Введите координаты точки и радиус круга")
tocha_1 = float(input("x = "))
tocha_2 = float(input("y = "))
radius = float(input("r ="))
h = ( math.sqrt(tocha_1**2 + tocha_2**2, )
print("round h 2")
if h <= radius:
    print ("Да далбан точка находиться в кругу с радиусом", radius)
else:
    print ("Нет ебр не находиться в кругу с радиусом", radius)

