# LIST COMPREHENSION EN PYTHON

# 1. Lista de números al cuadrado
cuadrados = [x**2 for x in range(10)]
print("Cuadrados:", cuadrados)

# 2. Lista de números pares
pares = [x for x in range(20) if x % 2 == 0]
print("Pares:", pares)

# 3. Filtrar una lista
nombres = ["Ana", "Luis", "Carlos", "Laura"]
nombres_largos = [nombre for nombre in nombres if len(nombre) > 4]
print("Nombres largos:", nombres_largos)

# 4. Convertir elementos a mayúsculas
mayusculas = [nombre.upper() for nombre in nombres]
print("Mayúsculas:", mayusculas)

# 5. Doble condicional
dobles_pares = [x*2 for x in range(20) if x % 2 == 0 and x > 10]
print("Dobles pares mayores que 10:", dobles_pares)

# 6. Con else (forma extendida)
resultado = [x if x % 2 == 0 else "impar" for x in range(10)]
print("Pares o 'impar':", resultado)

# 7. List comprehension con strings
frase = "hola mundo"
vocales = [letra for letra in frase if letra in "aeiou"]
print("Vocales en la frase:", vocales)

# 8. Anidar bucles
productos = [(x, y) for x in [1, 2, 3] for y in ['a', 'b']]
print("Combinaciones:", productos)

# 9. Matriz de 3x3
matriz = [[col for col in range(3)] for fila in range(3)]
print("Matriz 3x3:", matriz)

# 10. Aplanar una lista de listas
lista_de_listas = [[1, 2], [3, 4], [5, 6]]
aplanada = [num for sublista in lista_de_listas for num in sublista]
print("Lista aplanada:", aplanada)

# 11. Usar funciones en list comprehension
def cuadrado(x):
    return x * x

cuadrados_funcion = [cuadrado(i) for i in range(5)]
print("Cuadrados con función:", cuadrados_funcion)

# 12. Set comprehension
unicos = {x % 3 for x in range(10)}
print("Set de únicos:", unicos)

# 13. Dict comprehension
cuadrados_dict = {x: x**2 for x in range(5)}
print("Diccionario de cuadrados:", cuadrados_dict)