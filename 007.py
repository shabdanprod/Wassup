zoo_pets = ["lion", "skunk", "elephant", "horse","sex","audi", "keks"
            ]
for animal in zoo_pets:
    print(animal)
    del zoo_pets[1]
print(zoo_pets)

# элементы списка
# автоматичсекая распаковка содержимого списка/тьюпла
x, y = [1, 2]
(x,y) = (1, 2)
for element in [(1,2), (3,4)]:
    x, y = element[0], element[1]
    print(x+y)
for (x, y) in  [(1,2), (3,4)]:
    print(x+y)

pair_list = [(1,2), (3,4), (5,6)]

for x, y in pair_list:
    print(x+y)


