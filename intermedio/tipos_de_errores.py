#tipos de errores
from math import pi
import math

#Errores de sintaxis / SyntaxError
#print "Hola Mundo"
print("Hola Mundo")

#Errores de nombre / NameError
#print(nombre) 
nombre = "Juan"
print(nombre)

#Errores de tipo / TypeError
#print(5 + "5")

#Errores de índice / IndexError
lista = [1,2,3]
#print(lista[3])

# ModuleNotFoundError
# import maths # Descomentar para Error

# AttributeError
# print(math.PI) # Descomentar para Error
print(math.pi)

# KeyError
my_dict = {"Nombre": "Brais", "Apellido": "Moure", "Edad": 35, 1: "Python"}
print(my_dict["Edad"])
# print(my_dict["Apelido"]) # Descomentar para Error
print(my_dict["Apellido"])

# TypeError
# print(my_list["0"]) # Descomentar para Error
print(lista[0])
print(lista[False])

# ImportError
# from math import PI # Descomentar para Error
print(pi)

# ValueError
# my_int = int("10 Años") # Descomentar para Error
my_int = int("10")
print(type(my_int))

# ZeroDivisionError
# print(4/0) # Descomentar para Error
print(4/2)