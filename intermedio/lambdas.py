# FUNCIONES LAMBDA EN PYTHON

# 1. Qué es una función lambda
# Es una función anónima y pequeña que se define en una sola línea.

# Sintaxis: lambda argumentos: expresión

# 2. Ejemplo básico
sumar = lambda a, b: a + b
print("Suma lambda:", sumar(3, 5))

# 3. Lambda sin argumentos
saludo = lambda: "Hola mundo"
print("Saludo:", saludo())

# 4. Lambda con un argumento
al_cuadrado = lambda x: x ** 2
print("4 al cuadrado:", al_cuadrado(4))

# 5. Usar lambda con map
numeros = [1, 2, 3, 4]
cuadrados = list(map(lambda x: x ** 2, numeros))
print("Cuadrados con map:", cuadrados)

# 6. Usar lambda con filter
pares = list(filter(lambda x: x % 2 == 0, numeros))
print("Pares con filter:", pares)

# 7. Usar lambda con reduce (requiere importar desde functools)
from functools import reduce
suma_total = reduce(lambda x, y: x + y, numeros)
print("Suma total con reduce:", suma_total)

# 8. Ordenar listas con lambda
personas = [("Ana", 25), ("Luis", 30), ("Carlos", 20)]
# Ordenar por edad (índice 1)
ordenado = sorted(personas, key=lambda persona: persona[1])
print("Personas ordenadas por edad:", ordenado)

# 9. Lambda dentro de una función
def crear_multiplicador(n):
    return lambda x: x * n

doble = crear_multiplicador(2)
triple = crear_multiplicador(3)
print("Doble de 5:", doble(5))
print("Triple de 5:", triple(5))

# 10. Lambda con condicional (if-else)
mayor = lambda x, y: x if x > y else y
print("Mayor entre 10 y 20:", mayor(10, 20))

# 11. Lambda como reemplazo rápido de funciones simples
lista = ["banana", "manzana", "pera", "kiwi"]
ordenada_por_longitud = sorted(lista, key=lambda fruta: len(fruta))
print("Ordenadas por longitud:", ordenada_por_longitud)

# 12. Comparación entre función normal y lambda
def elevar_cuadrado(x):
    return x ** 2

lambda_cuadrado = lambda x: x ** 2

print("Normal:", elevar_cuadrado(6))
print("Lambda:", lambda_cuadrado(6))
