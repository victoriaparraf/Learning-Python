# ===== SETS EN PYTHON =====
# Los sets son colecciones desordenadas, sin elementos duplicados y sin índices

# === 1. Creación de Sets ===
print("=== CREACIÓN DE SETS ===")

# Set vacío (no se puede usar {}, ya que eso crea un diccionario vacío)
set_vacio = set()
print(f"Set vacío: {set_vacio}")

# Set con elementos
numeros = {1, 2, 3, 4, 5}
print(f"Set de números: {numeros}")

# Set con diferentes tipos de datos
mixto = {1, "Hola", 3.14, True}
print(f"Set mixto: {mixto}")

# Crear set a partir de una lista (elimina duplicados)
lista_con_duplicados = [1, 2, 2, 3, 3, 3, 4, 5, 5]
set_desde_lista = set(lista_con_duplicados)
print(f"Lista con duplicados: {lista_con_duplicados}")
print(f"Set desde lista (sin duplicados): {set_desde_lista}")

# Crear set a partir de un string (caracteres únicos)
set_desde_string = set("Mississippi")
print(f"Set desde string 'Mississippi': {set_desde_string}")

# Crear set a partir de una tupla
set_desde_tupla = set((1, 2, 3, 2, 1))
print(f"Set desde tupla (1, 2, 3, 2, 1): {set_desde_tupla}")

# Nota: Los sets solo pueden contener elementos inmutables (hashables)
# set_invalido = {[1, 2], 3}  # Esto daría un TypeError porque las listas son mutables
print()

# === 2. Características de los Sets ===
print("=== CARACTERÍSTICAS DE LOS SETS ===")

# 1. No tienen orden definido
numeros = {5, 3, 1, 4, 2}
print(f"Set de números: {numeros}")  # El orden puede variar en cada ejecución

# 2. No permiten duplicados
con_duplicados = {1, 2, 3, 1, 2, 3}
print(f"Set con duplicados (se eliminan): {con_duplicados}")

# 3. No se pueden indexar
# print(numeros[0])  # Esto daría un TypeError

# 4. Son mutables (el set en sí, no sus elementos)
numeros = {1, 2, 3}
print(f"Set original: {numeros}")
numeros.add(4)
print(f"Después de add(4): {numeros}")

# 5. Solo pueden contener elementos inmutables (hashables)
# Los tipos inmutables incluyen: números, strings, tuplas (si contienen solo inmutables)
# Los tipos mutables que no se pueden incluir: listas, diccionarios, sets
print("\nElementos válidos e inválidos para sets:")
print("Válidos: números, strings, tuplas (con elementos inmutables)")
print("Inválidos: listas, diccionarios, sets")

# Ejemplo de tupla válida e inválida como elemento de un set
set_con_tupla = {(1, 2), "hola"}
print(f"Set con tupla inmutable: {set_con_tupla}")

# Esto daría error porque la tupla contiene una lista (mutable)
# set_invalido = {(1, [2, 3]), "hola"}
print()

# === 3. Métodos para Añadir Elementos ===
print("=== MÉTODOS PARA AÑADIR ELEMENTOS ===")

colores = {"rojo", "verde"}
print(f"Set original: {colores}")

# add() - Añadir un elemento
colores.add("azul")
print(f"Después de add('azul'): {colores}")

# Si el elemento ya existe, no se añade (no hay duplicados)
colores.add("azul")
print(f"Después de add('azul') de nuevo: {colores}")

# update() - Añadir múltiples elementos
colores.update(["amarillo", "naranja", "verde"])
print(f"Después de update(['amarillo', 'naranja', 'verde']): {colores}")

# update() puede recibir cualquier iterable
colores.update(("morado", "rosa"))  # Tupla
print(f"Después de update(('morado', 'rosa')): {colores}")

colores.update("blanco")  # String (añade cada carácter)
print(f"Después de update('blanco'): {colores}")  # Añade 'b', 'l', 'a', 'n', 'c', 'o'
print()

# === 4. Métodos para Eliminar Elementos ===
print("=== MÉTODOS PARA ELIMINAR ELEMENTOS ===")

numeros = {1, 2, 3, 4, 5}
print(f"Set original: {numeros}")

# remove() - Eliminar un elemento (da error si no existe)
numeros.remove(3)
print(f"Después de remove(3): {numeros}")

# Si el elemento no existe, lanza KeyError
# numeros.remove(10)  # Esto lanzaría KeyError

# discard() - Eliminar un elemento (no da error si no existe)
numeros.discard(2)
print(f"Después de discard(2): {numeros}")

# Si el elemento no existe, no hace nada
numeros.discard(10)
print(f"Después de discard(10) (elemento inexistente): {numeros}")

# pop() - Eliminar y devolver un elemento arbitrario
elemento = numeros.pop()
print(f"Elemento eliminado con pop(): {elemento}")
print(f"Después de pop(): {numeros}")

# clear() - Eliminar todos los elementos
numeros.clear()
print(f"Después de clear(): {numeros}")
print()

# === 5. Operaciones de Conjuntos ===
print("=== OPERACIONES DE CONJUNTOS ===")

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
print(f"Conjunto A: {A}")
print(f"Conjunto B: {B}")

# Unión (|) - Elementos en A o en B
union = A | B
print(f"Unión (A | B): {union}")

# Método union()
union_metodo = A.union(B)
print(f"Unión con método (A.union(B)): {union_metodo}")

# Intersección (&) - Elementos en A y en B
interseccion = A & B
print(f"Intersección (A & B): {interseccion}")

# Método intersection()
interseccion_metodo = A.intersection(B)
print(f"Intersección con método (A.intersection(B)): {interseccion_metodo}")

# Diferencia (-) - Elementos en A pero no en B
diferencia = A - B
print(f"Diferencia (A - B): {diferencia}")

# Método difference()
diferencia_metodo = A.difference(B)
print(f"Diferencia con método (A.difference(B)): {diferencia_metodo}")

# Diferencia simétrica (^) - Elementos en A o en B, pero no en ambos
diferencia_simetrica = A ^ B
print(f"Diferencia simétrica (A ^ B): {diferencia_simetrica}")

# Método symmetric_difference()
diferencia_simetrica_metodo = A.symmetric_difference(B)
print(f"Diferencia simétrica con método (A.symmetric_difference(B)): {diferencia_simetrica_metodo}")
print()

# === 6. Métodos de Operaciones de Conjuntos (con asignación) ===
print("=== MÉTODOS DE OPERACIONES DE CONJUNTOS (CON ASIGNACIÓN) ===")

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
print(f"Conjunto A original: {A}")
print(f"Conjunto B original: {B}")

# update() / |= - Unión con asignación
C = A.copy()  # Copia para no modificar A original
C.update(B)  # Equivalente a C |= B
print(f"Después de C.update(B): {C}")

# intersection_update() / &= - Intersección con asignación
C = A.copy()
C.intersection_update(B)  # Equivalente a C &= B
print(f"Después de C.intersection_update(B): {C}")

# difference_update() / -= - Diferencia con asignación
C = A.copy()
C.difference_update(B)  # Equivalente a C -= B
print(f"Después de C.difference_update(B): {C}")

# symmetric_difference_update() / ^= - Diferencia simétrica con asignación
C = A.copy()
C.symmetric_difference_update(B)  # Equivalente a C ^= B
print(f"Después de C.symmetric_difference_update(B): {C}")
print()

# === 7. Métodos de Comparación de Conjuntos ===
print("=== MÉTODOS DE COMPARACIÓN DE CONJUNTOS ===")

A = {1, 2, 3}
B = {1, 2, 3, 4, 5}
C = {1, 2, 3}
D = {6, 7, 8}
print(f"Conjunto A: {A}")
print(f"Conjunto B: {B}")
print(f"Conjunto C: {C}")
print(f"Conjunto D: {D}")

# issubset() / <= - ¿Es subconjunto?
print(f"¿A es subconjunto de B? (A.issubset(B)): {A.issubset(B)}")
print(f"¿A es subconjunto de B? (A <= B): {A <= B}")

# issuperset() / >= - ¿Es superconjunto?
print(f"¿B es superconjunto de A? (B.issuperset(A)): {B.issuperset(A)}")
print(f"¿B es superconjunto de A? (B >= A): {B >= A}")

# isdisjoint() - ¿Son conjuntos disjuntos? (sin elementos comunes)
print(f"¿A y D son disjuntos? (A.isdisjoint(D)): {A.isdisjoint(D)}")
print(f"¿A y B son disjuntos? (A.isdisjoint(B)): {A.isdisjoint(B)}")

# Igualdad (==) - ¿Tienen los mismos elementos?
print(f"¿A es igual a C? (A == C): {A == C}")
print(f"¿A es igual a B? (A == B): {A == B}")

# Subconjunto propio (<) - Subconjunto y no igual
print(f"¿A es subconjunto propio de B? (A < B): {A < B}")
print(f"¿A es subconjunto propio de C? (A < C): {A < C}")

# Superconjunto propio (>) - Superconjunto y no igual
print(f"¿B es superconjunto propio de A? (B > A): {B > A}")
print(f"¿C es superconjunto propio de A? (C > A): {C > A}")
print()

# === 8. Comprensión de Sets ===
print("=== COMPRENSIÓN DE SETS ===")

# Sintaxis básica: {expresión for elemento in iterable}
numeros = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]
cuadrados = {x**2 for x in numeros}
print(f"Lista original: {numeros}")
print(f"Set de cuadrados: {cuadrados}")

# Con condición: {expresión for elemento in iterable if condición}
pares = {x for x in range(10) if x % 2 == 0}
print(f"Set de números pares del 0 al 9: {pares}")

# Ejemplo más complejo
palabras = ["hola", "mundo", "python", "programación", "set", "hola"]
resultado = {palabra.upper() for palabra in palabras if len(palabra) > 3}
print(f"Palabras originales: {palabras}")
print(f"Set de palabras en mayúsculas con más de 3 letras: {resultado}")
print()

# === 9. Frozenset (Sets Inmutables) ===
print("=== FROZENSET (SETS INMUTABLES) ===")

# Crear un frozenset
numeros = frozenset([1, 2, 3, 4, 5])
print(f"Frozenset: {numeros}")

# No se pueden modificar
# numeros.add(6)  # Esto daría un AttributeError

# Pero se pueden usar en operaciones que no modifican el set
A = frozenset([1, 2, 3])
B = frozenset([3, 4, 5])
print(f"Frozenset A: {A}")
print(f"Frozenset B: {B}")

# Operaciones válidas (crean nuevos frozensets)
print(f"Unión (A | B): {A | B}")
print(f"Intersección (A & B): {A & B}")
print(f"Diferencia (A - B): {A - B}")
print(f"Diferencia simétrica (A ^ B): {A ^ B}")

# Los frozensets pueden usarse como elementos de otros sets o como claves de diccionarios
set_de_frozensets = {frozenset([1, 2]), frozenset([3, 4])}
print(f"\nSet de frozensets: {set_de_frozensets}")

diccionario = {frozenset([1, 2]): "Conjunto 1-2", frozenset([3, 4]): "Conjunto 3-4"}
print(f"Diccionario con frozensets como claves: {diccionario}")
print()

# === 10. Rendimiento y Consideraciones ===
print("=== RENDIMIENTO Y CONSIDERACIONES ===")

# Verificación de pertenencia (in) - O(1) en promedio
numeros = set(range(1000000))
import time

# Verificar en un set (muy rápido)
inicio = time.time()
resultado = 500000 in numeros
fin = time.time()
print(f"Tiempo para verificar en set: {(fin - inicio) * 1000:.6f} ms")

# Verificar en una lista (más lento)
numeros_lista = list(range(1000000))
inicio = time.time()
resultado = 500000 in numeros_lista
fin = time.time()
print(f"Tiempo para verificar en lista: {(fin - inicio) * 1000:.6f} ms")

# Tamaño en memoria
import sys
set_pequeno = {1, 2, 3, 4, 5}
lista_pequena = [1, 2, 3, 4, 5]
print(f"\nTamaño de set {set_pequeno}: {sys.getsizeof(set_pequeno)} bytes")
print(f"Tamaño de lista {lista_pequena}: {sys.getsizeof(lista_pequena)} bytes")

# Consideraciones de uso
print("\nCuándo usar sets:")
print("- Para eliminar duplicados de una colección")
print("- Para verificar pertenencia de forma eficiente (operación 'in')")
print("- Para operaciones matemáticas de conjuntos (unión, intersección, etc.)")
print("- Cuando el orden de los elementos no importa")
print()

# === 11. Ejemplos Prácticos ===
print("=== EJEMPLOS PRÁCTICOS ===")

# Ejemplo 1: Eliminar duplicados de una lista manteniendo el orden
def eliminar_duplicados(lista):
    return list(dict.fromkeys(lista))

numeros = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print(f"Lista original: {numeros}")
print(f"Lista sin duplicados (manteniendo orden): {eliminar_duplicados(numeros)}")

# Ejemplo 2: Encontrar elementos únicos en múltiples listas
lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]
lista3 = [7, 8, 9, 10]

set1 = set(lista1)
set2 = set(lista2)
set3 = set(lista3)

# Elementos que están en todas las listas
comunes = set1 & set2 & set3
print(f"\nElementos comunes a todas las listas: {comunes}")

# Elementos que están en al menos una lista
todos = set1 | set2 | set3
print(f"Elementos que están en al menos una lista: {todos}")

# Elementos que están solo en la primera lista
solo_en_primera = set1 - (set2 | set3)
print(f"Elementos solo en la primera lista: {solo_en_primera}")

# Ejemplo 3: Verificar si una palabra es un anagrama de otra
def es_anagrama(palabra1, palabra2):
    # Convertir a minúsculas y eliminar espacios
    palabra1 = palabra1.lower().replace(" ", "")
    palabra2 = palabra2.lower().replace(" ", "")
    # Comparar los conjuntos de caracteres y sus frecuencias
    return sorted(palabra1) == sorted(palabra2)

print("\nVerificación de anagramas:")
print(f"'listen' y 'silent': {es_anagrama('listen', 'silent')}")
print(f"'triangle' y 'integral': {es_anagrama('triangle', 'integral')}")
print(f"'python' y 'typhon': {es_anagrama('python', 'typhon')}")
print(f"'hello' y 'world': {es_anagrama('hello', 'world')}")

# Ejemplo 4: Encontrar caracteres únicos en un texto
def caracteres_unicos(texto):
    return set(texto.lower())

texto = "Python es un lenguaje de programación"
print(f"\nTexto: '{texto}'")
print(f"Caracteres únicos: {caracteres_unicos(texto)}")

# Ejemplo 5: Implementar un sistema simple de etiquetas
articulos = [
    {"id": 1, "titulo": "Introducción a Python", "etiquetas": {"python", "programación", "tutorial"}},
    {"id": 2, "titulo": "Estructuras de datos", "etiquetas": {"python", "listas", "diccionarios", "sets"}},
    {"id": 3, "titulo": "Programación web", "etiquetas": {"web", "html", "css", "javascript"}},
    {"id": 4, "titulo": "Python avanzado", "etiquetas": {"python", "decoradores", "generadores"}}
]

# Buscar artículos por etiqueta
def buscar_por_etiqueta(articulos, etiqueta):
    return [a for a in articulos if etiqueta in a["etiquetas"]]

print("\nBúsqueda de artículos por etiqueta:")
resultados = buscar_por_etiqueta(articulos, "python")
for articulo in resultados:
    print(f"- {articulo['titulo']}")

# Encontrar etiquetas relacionadas
def etiquetas_relacionadas(articulos, etiqueta, excluir=None):
    if excluir is None:
        excluir = {etiqueta}
    else:
        excluir = set(excluir) | {etiqueta}
    
    relacionadas = set()
    for articulo in buscar_por_etiqueta(articulos, etiqueta):
        relacionadas |= articulo["etiquetas"]
    
    return relacionadas - set(excluir)

print("\nEtiquetas relacionadas con 'python':")
print(etiquetas_relacionadas(articulos, "python"))