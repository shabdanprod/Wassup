# блоки кода
x, y = 10, 29
if x < 0:
  print("X меньше нуля")
  z = x**2 + y
else:
  print("X больше нуля")
  z = x - y
print("Результат", z)


# вложенные блоки кода
name = input("Enter your name>>>")
if name == "Ola":
    opponent = "Ola"
    print("Hi, Ola!")
else:
    if name == "Sofi":
        opponent = "Sofi"
        print("Hi, Sofi")
    else:
        if name == "Katy":
            opponent = "Katy"
            print("Hi, Katy!")
        else:
            opponent = "anonymous"
            print("Hi, anonymous!")

#   оператор pass
if x < 0:
    if y > 0:
        pass
    else:
        z = -x - y
else:
    z = x + y



#пробелы в операторах
x = 2
y = x* x+ 1
is_big=x   >=3000

x = my_poem    [-1]
print      (x)
my_lists= [2,3 ,4,   5,6,]



#continue
cars = ["audi", "bmw", "Tiko", "Fit", "Porter", "Mers"]
i = -1
while i < len(cars):
    i += 1
    if car == cars[2]:
        continue
    if car == "Porter":
        break
