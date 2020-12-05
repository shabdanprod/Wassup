print("привет")

# break
my_pets = ["dog", "hamster", "cat", "hamster", "hamster", "hamster" ]
i = 0
while i < len(my_pets):
    pet = my_pets[i]
    print("Проверяем", pet)
    if pet == 'cat':
        print("Ура, кот найден!")
        break
    i = i + 1
else:
    print('Не нашли кота')
print('Пока')




#бесконечный цикл
x1, x2, count = 0, 1, 0
while x2 < 10000:
    count += 1
    if count > 27:
        print("цикл больше 27, прерываюcь!")
        break
    x1, x2 =x2, x1 + x2
    if x2 < 1000:
        continue
    print(count)
else:
    print("Циклов", - count)



