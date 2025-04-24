# ===== LISTAS EN PYTHON =====
# Las listas son colecciones ordenadas y mutables que permiten elementos duplicados

# === 1. Creación de Listas ===
print("=== CREACIÓN DE LISTAS ===")

# Lista vacía
lista_vacia = []
print(f"Lista vacía: {lista_vacia}")

# Lista con elementos
numeros = [1, 2, 3, 4, 5]
print(f"Lista de números: {numeros}")

# Lista con diferentes tipos de datos
mixta = [1, "Hola", 3.14, True, [1, 2]]
print(f"Lista mixta: {mixta}")

# Crear lista con la función list()
lista_desde_rango = list(range(1, 6))  # Convierte un rango a lista
print(f"Lista desde rango: {lista_desde_rango}")

lista_desde_string = list("Python")  # Convierte un string a lista de caracteres
print(f"Lista desde string: {lista_desde_string}")

# Lista con repetición
repetida = [0] * 5
print(f"Lista repetida: {repetida}")

# Listas anidadas (matrices)
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"Matriz (lista anidada): {matriz}")
print()

# === 2. Acceso a Elementos ===
print("=== ACCESO A ELEMENTOS ===")

frutas = ["manzana", "banana", "cereza", "durazno", "fresa"]
print(f"Lista de frutas: {frutas}")

# Acceso por índice (comienza en 0)
print(f"Primer elemento (índice 0): {frutas[0]}")
print(f"Tercer elemento (índice 2): {frutas[2]}")

# Índices negativos (desde el final)
print(f"Último elemento (índice -1): {frutas[-1]}")
print(f"Penúltimo elemento (índice -2): {frutas[-2]}")

# Acceso a elementos en listas anidadas
print(f"Matriz: {matriz}")
print(f"Elemento en posición [1][2]: {matriz[1][2]}")  # Fila 1, columna 2 (valor 6)

# Verificar si un elemento existe
print(f"¿'banana' está en la lista? {'banana' in frutas}")
print(f"¿'sandía' está en la lista? {'sandía' in frutas}")
print()

# === 3. Slicing (Rebanado) ===
print("=== SLICING (REBANADO) ===")

numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"Lista completa: {numeros}")

# Sintaxis: lista[inicio:fin:paso]
print(f"numeros[2:5]: {numeros[2:5]}")  # Elementos del índice 2 al 4
print(f"numeros[:4]: {numeros[:4]}")    # Elementos desde el inicio hasta el índice 3
print(f"numeros[6:]: {numeros[6:]}")    # Elementos desde el índice 6 hasta el final
print(f"numeros[1:8:2]: {numeros[1:8:2]}")  # Elementos del 1 al 7 con paso 2
print(f"numeros[::3]: {numeros[::3]}")  # Todos los elementos con paso 3
print(f"numeros[::-1]: {numeros[::-1]}")  # Lista invertida
print()

# === 4. Modificación de Listas ===
print("=== MODIFICACIÓN DE LISTAS ===")

colores = ["rojo", "verde", "azul"]
print(f"Lista original: {colores}")

# Cambiar un elemento
colores[1] = "amarillo"
print(f"Después de cambiar el segundo elemento: {colores}")

# Cambiar un rango de elementos
colores[0:2] = ["naranja", "morado"]
print(f"Después de cambiar un rango: {colores}")

# Insertar más elementos de los que se reemplazan
colores[1:2] = ["rosa", "gris", "negro"]
print(f"Después de insertar más elementos: {colores}")

# Insertar menos elementos de los que se reemplazan
colores[2:5] = ["blanco"]
print(f"Después de insertar menos elementos: {colores}")
print()

# === 5. Métodos de Listas ===
print("=== MÉTODOS DE LISTAS ===")

frutas = ["manzana", "banana", "cereza"]
print(f"Lista original: {frutas}")

# append() - Añadir un elemento al final
frutas.append("durazno")
print(f"Después de append('durazno'): {frutas}")

# insert() - Insertar un elemento en una posición específica
frutas.insert(1, "fresa")
print(f"Después de insert(1, 'fresa'): {frutas}")

# extend() - Añadir elementos de otra lista (o iterable)
mas_frutas = ["kiwi", "limón"]
frutas.extend(mas_frutas)
print(f"Después de extend({mas_frutas}): {frutas}")

# remove() - Eliminar un elemento por valor
frutas.remove("banana")
print(f"Después de remove('banana'): {frutas}")

# pop() - Eliminar un elemento por índice y devolverlo
fruta_eliminada = frutas.pop(2)
print(f"Elemento eliminado con pop(2): {fruta_eliminada}")
print(f"Lista después de pop(2): {frutas}")

# pop() sin argumentos elimina y devuelve el último elemento
ultimo = frutas.pop()
print(f"Último elemento (pop()): {ultimo}")
print(f"Lista después de pop(): {frutas}")

# clear() - Eliminar todos los elementos
numeros = [1, 2, 3]
numeros.clear()
print(f"Después de clear(): {numeros}")

# index() - Encontrar la posición de un elemento
print(f"Posición de 'fresa' en frutas: {frutas.index('fresa')}")
# print(f"Posición de 'plátano': {frutas.index('plátano')}")  # Daría error si no existe

# count() - Contar ocurrencias de un elemento
letras = ["a", "b", "c", "a", "d", "a"]
print(f"Ocurrencias de 'a' en {letras}: {letras.count('a')}")

# sort() - Ordenar la lista (modifica la original)
numeros = [3, 1, 4, 1, 5, 9, 2]
print(f"Lista desordenada: {numeros}")
numeros.sort()
print(f"Después de sort(): {numeros}")

# sort() con reverse=True - Ordenar en orden descendente
numeros.sort(reverse=True)
print(f"Después de sort(reverse=True): {numeros}")

# sort() con key - Ordenar con una función personalizada
palabras = ["zanahoria", "manzana", "pera", "uva"]
palabras.sort(key=len)  # Ordenar por longitud
print(f"Palabras ordenadas por longitud: {palabras}")

# reverse() - Invertir el orden de los elementos
numeros = [1, 2, 3, 4, 5]
numeros.reverse()
print(f"Después de reverse(): {numeros}")

# copy() - Crear una copia de la lista
original = [1, 2, 3]
copia = original.copy()
print(f"Original: {original}, Copia: {copia}")
copia[0] = 99  # Modificar la copia no afecta al original
print(f"Original después de modificar la copia: {original}")
print()

# === 6. Operaciones con Listas ===
print("=== OPERACIONES CON LISTAS ===")

# Concatenación (+)
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
concatenada = lista1 + lista2
print(f"{lista1} + {lista2} = {concatenada}")

# Repetición (*)
repetida = [0, 1] * 3
print(f"[0, 1] * 3 = {repetida}")

# Longitud (len)
print(f"Longitud de {lista1}: {len(lista1)}")

# Máximo y mínimo
numeros = [5, 2, 8, 1, 9]
print(f"Máximo de {numeros}: {max(numeros)}")
print(f"Mínimo de {numeros}: {min(numeros)}")

# Suma
print(f"Suma de {numeros}: {sum(numeros)}")

# Ordenar sin modificar la original (sorted)
desordenada = [3, 1, 4, 1, 5, 9]
ordenada = sorted(desordenada)
print(f"Lista original: {desordenada}")
print(f"Lista ordenada (con sorted): {ordenada}")
print(f"Lista original después de sorted: {desordenada}")  # No se modifica

# Ordenar en reversa
ordenada_reversa = sorted(desordenada, reverse=True)
print(f"Lista ordenada en reversa: {ordenada_reversa}")

# Convertir a string (join)
frutas = ["manzana", "banana", "cereza"]
texto = ", ".join(frutas)
print(f"Lista convertida a string: '{texto}'")
print()

# === 7. Comprensión de Listas ===
print("=== COMPRENSIÓN DE LISTAS ===")

# Sintaxis básica: [expresión for elemento in iterable]
numeros = [1, 2, 3, 4, 5]
cuadrados = [x**2 for x in numeros]
print(f"Números: {numeros}")
print(f"Cuadrados: {cuadrados}")

# Con condición: [expresión for elemento in iterable if condición]
pares = [x for x in range(10) if x % 2 == 0]
print(f"Números pares del 0 al 9: {pares}")

# Con múltiples condiciones
numeros = [x for x in range(20) if x % 2 == 0 if x % 3 == 0]
print(f"Números divisibles por 2 y 3: {numeros}")

# Con if-else en la expresión
numeros = [1, 2, 3, 4, 5]
paridad = ["par" if x % 2 == 0 else "impar" for x in numeros]
print(f"Paridad de {numeros}: {paridad}")

# Comprensión de listas anidadas
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
aplanada = [x for fila in matriz for x in fila]
print(f"Matriz: {matriz}")
print(f"Matriz aplanada: {aplanada}")

# Crear una matriz con comprensión de listas
matriz_3x3 = [[i + j * 3 + 1 for i in range(3)] for j in range(3)]
print(f"Matriz 3x3 creada con comprensión: {matriz_3x3}")
print()

# === 8. Listas como Pilas y Colas ===
print("=== LISTAS COMO PILAS Y COLAS ===")

# Pila (LIFO: Last In, First Out)
print("Pila (LIFO):")
pila = []
pila.append(1)  # Añadir al final
print(f"Después de append(1): {pila}")
pila.append(2)
print(f"Después de append(2): {pila}")
pila.append(3)
print(f"Después de append(3): {pila}")

elemento = pila.pop()  # Sacar del final
print(f"Elemento extraído (pop): {elemento}")
print(f"Pila después de pop: {pila}")
elemento = pila.pop()
print(f"Elemento extraído (pop): {elemento}")
print(f"Pila después de pop: {pila}")

# Cola (FIFO: First In, First Out)
# Para colas eficientes, es mejor usar collections.deque
from collections import deque
print("\nCola (FIFO):")
cola = deque([])
cola.append(1)  # Añadir al final
print(f"Después de append(1): {cola}")
cola.append(2)
print(f"Después de append(2): {cola}")
cola.append(3)
print(f"Después de append(3): {cola}")

elemento = cola.popleft()  # Sacar del principio
print(f"Elemento extraído (popleft): {elemento}")
print(f"Cola después de popleft: {cola}")
elemento = cola.popleft()
print(f"Elemento extraído (popleft): {elemento}")
print(f"Cola después de popleft: {cola}")
print()

# === 9. Listas y Referencias ===
print("=== LISTAS Y REFERENCIAS ===")

# Las listas son objetos mutables y se pasan por referencia
original = [1, 2, 3]
referencia = original  # No crea una copia, sino una referencia
print(f"Original: {original}")
print(f"Referencia: {referencia}")

# Modificar a través de la referencia afecta al original
referencia[0] = 99
print(f"Referencia después de modificar: {referencia}")
print(f"Original después de modificar la referencia: {original}")

# Formas de crear copias reales
# 1. Usando el método copy()
copia1 = original.copy()
# 2. Usando list()
copia2 = list(original)
# 3. Usando slicing
copia3 = original[:]

print(f"Original: {original}")
print(f"Copia1: {copia1}")
print(f"Copia2: {copia2}")
print(f"Copia3: {copia3}")

# Modificar las copias no afecta al original
copia1[0] = 100
copia2[1] = 200
copia3[2] = 300
print(f"Copia1 modificada: {copia1}")
print(f"Copia2 modificada: {copia2}")
print(f"Copia3 modificada: {copia3}")
print(f"Original sin cambios: {original}")

# Copia superficial vs. copia profunda
anidada = [1, 2, [3, 4]]
copia_superficial = anidada.copy()
print(f"\nLista anidada: {anidada}")
print(f"Copia superficial: {copia_superficial}")

# Modificar la lista interna afecta a ambas
copia_superficial[2][0] = 99
print(f"Copia superficial después de modificar: {copia_superficial}")
print(f"Original después de modificar la copia: {anidada}")

# Para copias profundas, usar copy.deepcopy()
import copy
anidada = [1, 2, [3, 4]]
copia_profunda = copy.deepcopy(anidada)
print(f"\nLista anidada: {anidada}")
print(f"Copia profunda: {copia_profunda}")

# Modificar la lista interna no afecta a la original
copia_profunda[2][0] = 99
print(f"Copia profunda después de modificar: {copia_profunda}")
print(f"Original sin cambios: {anidada}")
print()

# === 10. Funciones Útiles con Listas ===
print("=== FUNCIONES ÚTILES CON LISTAS ===")

numeros = [5, 2, 8, 1, 9]
print(f"Lista: {numeros}")

# enumerate() - Obtener índice y valor
print("Usando enumerate():")
for i, valor in enumerate(numeros):
    print(f"Índice {i}: {valor}")

# zip() - Combinar listas
nombres = ["Ana", "Juan", "María"]
edades = [25, 30, 22]
print(f"\nNombres: {nombres}")
print(f"Edades: {edades}")
print("Usando zip():")
for nombre, edad in zip(nombres, edades):
    print(f"{nombre} tiene {edad} años")

# map() - Aplicar una función a cada elemento
numeros = [1, 2, 3, 4, 5]
cuadrados = list(map(lambda x: x**2, numeros))
print(f"\nNúmeros: {numeros}")
print(f"Cuadrados usando map(): {cuadrados}")

# filter() - Filtrar elementos según una condición
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(f"Números pares usando filter(): {pares}")

# any() - Verifica si al menos un elemento cumple una condición
hay_par = any(x % 2 == 0 for x in numeros)
print(f"¿Hay algún número par?: {hay_par}")

# all() - Verifica si todos los elementos cumplen una condición
todos_positivos = all(x > 0 for x in numeros)
print(f"¿Todos los números son positivos?: {todos_positivos}")
print()

# === 11. Algoritmos Comunes con Listas ===
print("=== ALGORITMOS COMUNES CON LISTAS ===")

# Encontrar el elemento más frecuente
from collections import Counter
numeros = [1, 2, 3, 1, 2, 1, 4, 5, 1]
contador = Counter(numeros)
mas_comun = contador.most_common(1)[0]  # (elemento, frecuencia)
print(f"Lista: {numeros}")
print(f"Elemento más frecuente: {mas_comun[0]} (aparece {mas_comun[1]} veces)")

# Eliminar duplicados (manteniendo el orden)
con_duplicados = [1, 2, 3, 1, 2, 5, 6, 7, 3]
sin_duplicados = list(dict.fromkeys(con_duplicados))
print(f"\nLista con duplicados: {con_duplicados}")
print(f"Lista sin duplicados (manteniendo orden): {sin_duplicados}")

# Aplanar una lista anidada
anidada = [[1, 2], [3, 4, 5], [6, 7]]
aplanada = [item for sublist in anidada for item in sublist]
print(f"\nLista anidada: {anidada}")
print(f"Lista aplanada: {aplanada}")

# Encontrar elementos comunes entre dos listas
lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]
comunes = list(set(lista1) & set(lista2))
print(f"\nLista 1: {lista1}")
print(f"Lista 2: {lista2}")
print(f"Elementos comunes: {comunes}")

# Encontrar elementos únicos de cada lista
solo_en_lista1 = list(set(lista1) - set(lista2))
solo_en_lista2 = list(set(lista2) - set(lista1))
print(f"Elementos solo en lista 1: {solo_en_lista1}")
print(f"Elementos solo en lista 2: {solo_en_lista2}")

# Dividir una lista en partes iguales
def dividir_lista(lista, n):
    """Divide una lista en n partes de tamaño similar"""
    k, m = divmod(len(lista), n)
    return [lista[i * k + min(i, m):(i + 1) * k + min(i + 1, m)] for i in range(n)]

numeros = list(range(1, 11))  # [1, 2, 3, ..., 10]
partes = dividir_lista(numeros, 3)
print(f"\nLista original: {numeros}")
print(f"Dividida en 3 partes: {partes}")

# Rotar una lista
def rotar_lista(lista, k):
    """Rota una lista k posiciones a la derecha"""
    if not lista:
        return lista
    k = k % len(lista)  # Manejar k > len(lista)
    return lista[-k:] + lista[:-k]

numeros = [1, 2, 3, 4, 5]
rotada = rotar_lista(numeros, 2)
print(f"\nLista original: {numeros}")
print(f"Rotada 2 posiciones: {rotada}")
print()

# === 12. Rendimiento y Consideraciones ===
print("=== RENDIMIENTO Y CONSIDERACIONES ===")

# Tiempo de acceso
import time

# Crear una lista grande
n = 1000000
lista_grande = list(range(n))

# Acceso por índice (O(1))
inicio = time.time()
valor = lista_grande[500000]
fin = time.time()
print(f"Tiempo de acceso por índice: {(fin - inicio) * 1000:.6f} ms")

# Búsqueda de un valor (O(n))
inicio = time.time()
encontrado = 500000 in lista_grande
fin = time.time()
print(f"Tiempo de búsqueda de valor: {(fin - inicio) * 1000:.6f} ms")

# Inserción al final (append) - O(1) amortizado
inicio = time.time()
lista_grande.append(n)
fin = time.time()
print(f"Tiempo de append: {(fin - inicio) * 1000:.6f} ms")

# Inserción al principio (insert) - O(n)
inicio = time.time()
lista_grande.insert(0, -1)
fin = time.time()
print(f"Tiempo de insert al principio: {(fin - inicio) * 1000:.6f} ms")

# Consideraciones de memoria
import sys
lista_pequena = [1, 2, 3, 4, 5]
tamano_bytes = sys.getsizeof(lista_pequena)
print(f"\nTamaño en memoria de {lista_pequena}: {tamano_bytes} bytes")

# Las listas ocupan más memoria que las tuplas
tupla_pequena = (1, 2, 3, 4, 5)
tamano_tupla = sys.getsizeof(tupla_pequena)
print(f"Tamaño en memoria de {tupla_pequena}: {tamano_tupla} bytes")
print(f"Diferencia: {tamano_bytes - tamano_tupla} bytes más para la lista")