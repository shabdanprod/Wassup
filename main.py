
zoo_pets = ["lion", "elephant", "monkey", "skunk", "horse"]
for animal in zoo_pets:
    print("Сейчас переменная animal указывает на", animal)
    if animal == "elephant":
        print("Нашли слона...!")
        break
    print("Это не слон...!")
print("Выход из цикла")