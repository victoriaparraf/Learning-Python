#Condicionales
if 5 > 2:
    print("5 es mayor que 2")
else:
    print("5 no es mayor que 2")

if 'hola' == 'hola' and 5 > 2:
    print("Ambas condiciones son verdaderas")
else:
    print("Alguna de las condiciones no se cumple")

if len('hola') == 4 or 5 > 2:
    print("Al menos una de las condiciones es verdadera")
elif 5 > 2:
    print("5 es mayor que 2")
else:
    print("5 no es mayor que 2")

#bucles
i = 1
while i < 6:
    print(i)
    i += 1
    if i == 3:
        print("i es igual a 3")
        break
    

#bucle for
frutas = ["manzana", "banana", "cereza"]
for x in frutas:
    print(x)
    if x == "banana":
        break
