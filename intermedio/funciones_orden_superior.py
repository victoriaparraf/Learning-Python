# FUNCIONES DE ORDEN SUPERIOR EN PYTHON

# ¿Qué son?
# Son funciones que pueden recibir otras funciones como argumentos y/o devolver funciones como resultado.

# 1. Función que recibe otra función como argumento
def aplicar_operacion(x, y, operacion):
    return operacion(x, y)

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

print("Suma:", aplicar_operacion(5, 3, suma))
print("Resta:", aplicar_operacion(5, 3, resta))

# 2. Función que devuelve otra función
def crear_multiplicador(factor):
    def multiplicador(x):
        return x * factor
    return multiplicador

duplicar = crear_multiplicador(2)
triplicar = crear_multiplicador(3)

print("Duplicar 4:", duplicar(4))
print("Triplicar 4:", triplicar(4))

# 3. Uso con funciones lambda
print("Lambda multiplicar:", aplicar_operacion(4, 5, lambda a, b: a * b))

# 4. map(): aplicar una función a cada elemento de un iterable
numeros = [1, 2, 3, 4]
dobles = list(map(lambda x: x * 2, numeros))
print("Dobles:", dobles)

# 5. filter(): filtrar elementos con una función que devuelva True/False
pares = list(filter(lambda x: x % 2 == 0, numeros))
print("Pares:", pares)

# 6. reduce(): aplicar una función acumulativa (requiere functools)
from functools import reduce
suma_total = reduce(lambda x, y: x + y, numeros)
print("Suma total:", suma_total)

# 7. sorted() con funciones como clave
personas = [("Ana", 25), ("Luis", 30), ("Carlos", 20)]
ordenadas_por_edad = sorted(personas, key=lambda persona: persona[1])
print("Ordenadas por edad:", ordenadas_por_edad)

# 8. any() y all() con funciones
valores = [10, 20, 30]
condiciones = [x > 5 for x in valores]

print("¿Todos > 5?", all(condiciones))
print("¿Alguno > 25?", any(x > 25 for x in valores))

# 9. Funciones dentro de funciones (encapsulamiento)
def procesar_lista(lista, funcion):
    def operacion(x):
        return funcion(x)
    return [operacion(i) for i in lista]

print("Procesar al cuadrado:", procesar_lista([1, 2, 3], lambda x: x**2))

# 10. Composición de funciones (crear una función combinando otras)
def componer(f, g):
    return lambda x: f(g(x))

doblar = lambda x: x * 2
incrementar = lambda x: x + 1

doblar_y_luego_incrementar = componer(incrementar, doblar)
print("Doblar y luego incrementar 5:", doblar_y_luego_incrementar(5))
