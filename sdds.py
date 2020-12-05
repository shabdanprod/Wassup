my_cars = ["Audi", "Bmw", "Fit", "Tiko"]
for car in my_cars:
    print("Переменная указывает на", car)
    if car == "Fit":
        print("Нашли то что искали")

    print("Это не наша машина")
else:
    print("Выход из цикла")

#continue
zoo_pets = ["lion", "skunk", "elephant", "monkey", "horse"]
for animal in zoo_pets:
    if animal == "elephant":
        continue
    print("У нас в руках", animal)
print("Exit")


# полный пример
zoo_pets = ["lion", "monkey", "skunk", "elephant", "horse"]
for animal in zoo_pets:
    if animal == "skunk":
        print("Фуу...!")
        continue
    print("Сейчас переменная указывает на", animal)
    if animal == "elephant":
        print("Нашли слона!")
        break
    print("Это не слон")
else:
    print("Тут слона нет...")
print("Выход из цикла")
