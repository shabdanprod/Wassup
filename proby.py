x, y = 3, 8
if x == 3:
    print(42)
if x < 0:
    if y > 0:
        print("налево!")
    else:
        print("направо!")
else:
    print(
        "стой!")

# названия переменных
my_pets_count = 34
if my_pets_count > 10:
    print("I need more space for my pets!")
kottor = ["cat", "wolf", "ostrich"]
if "lion" in kottor:
    print("Wow!")

# цикл While (Повторение части кода)
print("Здарова")
i = 3
a = 8
while a < 100:
    i = i * 2
    print(i)
print("Пока!")

# последовательность фабионачи
t1, t2 = 2, 2
print(t1)
while t2 < 1000:
    print(t2)
t1, t2 = t2, t1 + t2


# else
i = 1
while i < 10:
    i *= 2
    print(i)
else:
    print("i >= 10")
print("пока")

# break
my_pets = ["cat", "dog", "hamster"]
i = 0
while i < len(my_pets):
    pet = my_pets[i]
    print("Проверяем", pet)
    if pet == 'cat':
        print("Ура, кот найден!")
    i += 1
print('Пока')