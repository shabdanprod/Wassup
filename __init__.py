# zoo_pets = ["lion", "skunk", "elephant", "horse"]
# for animal in zoo_pets:
#     for char in animal:
#         print(char)
#     print(animal)

# цикл по словарям
# pets_mass = {
#     "lion" : 300,
#     "skunk" : 5,
#     "elephant" : 5000,
#     "horse" : 400,
#
#     }
# total_mass = 0
# for animal in pets_mass:
#     mass = pets_mass[animal]
#     print(animal, mass)
#     total_mass += mass
# print("Общая масса животных", total_mass)

#.values
pets_mass = {
    "lion" : 300,
    "skunk" : 5,
    "elephant" : 5000,
    "horse" : 400,

    }
total_mass = 0
for  mass in pets_mass.values():
    print( mass)
    total_mass += mass
print("Общая масса животных", total_mass)



