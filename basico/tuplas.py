# ===== TUPLAS EN PYTHON =====
# Las tuplas son colecciones ordenadas e inmutables que permiten elementos duplicados

# === 1. Creación de Tuplas ===
print("=== CREACIÓN DE TUPLAS ===")

# Tupla vacía
tupla_vacia = ()
print(f"Tupla vacía: {tupla_vacia}")

# Tupla con elementos
numeros = (1, 2, 3, 4, 5)
print(f"Tupla de números: {numeros}")

# Tupla con diferentes tipos de datos
mixta = (1, "Hola", 3.14, True, (1, 2))
print(f"Tupla mixta: {mixta}")

# Tupla con un solo elemento (requiere una coma)
tupla_unitaria = (42,)  # Sin la coma sería un entero entre paréntesis
print(f"Tupla unitaria: {tupla_unitaria}, tipo: {type(tupla_unitaria)}")
no_es_tupla = (42)  # Esto es un entero, no una tupla
print(f"No es tupla: {no_es_tupla}, tipo: {type(no_es_tupla)}")

# Crear tupla sin paréntesis (empaquetado de tupla)
tupla_implicita = 1, 2, 3, 4, 5
print(f"Tupla implícita: {tupla_implicita}, tipo: {type(tupla_implicita)}")

# Crear tupla con la función tuple()
tupla_desde_lista = tuple([1, 2, 3])  # Convierte una lista a tupla
print(f"Tupla desde lista: {tupla_desde_lista}")

tupla_desde_string = tuple("Python")  # Convierte un string a tupla de caracteres
print(f"Tupla desde string: {tupla_desde_string}")

# Tupla con repetición
repetida = (0,) * 5
print(f"Tupla repetida: {repetida}")

# Tuplas anidadas
anidada = (1, 2, (3, 4), (5, 6, 7))
print(f"Tupla anidada: {anidada}")
print()

# === 2. Acceso a Elementos ===
print("=== ACCESO A ELEMENTOS ===")

frutas = ("manzana", "banana", "cereza", "durazno", "fresa")
print(f"Tupla de frutas: {frutas}")

# Acceso por índice (comienza en 0)
print(f"Primer elemento (índice 0): {frutas[0]}")
print(f"Tercer elemento (índice 2): {frutas[2]}")

# Índices negativos (desde el final)
print(f"Último elemento (índice -1): {frutas[-1]}")
print(f"Penúltimo elemento (índice -2): {frutas[-2]}")

# Acceso a elementos en tuplas anidadas
tupla_anidada = (1, 2, (3, 4, 5), 6)
print(f"Tupla anidada: {tupla_anidada}")
print(f"Elemento en posición [2][1]: {tupla_anidada[2][1]}")  # Accede al 4

# Verificar si un elemento existe
print(f"¿'banana' está en la tupla? {'banana' in frutas}")
print(f"¿'sandía' está en la tupla? {'sandía' in frutas}")
print()

# === 3. Slicing (Rebanado) ===
print("=== SLICING (REBANADO) ===")

numeros = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
print(f"Tupla completa: {numeros}")

# Sintaxis: tupla[inicio:fin:paso]
print(f"numeros[2:5]: {numeros[2:5]}")  # Elementos del índice 2 al 4
print(f"numeros[:4]: {numeros[:4]}")    # Elementos desde el inicio hasta el índice 3
print(f"numeros[6:]: {numeros[6:]}")    # Elementos desde el índice 6 hasta el final
print(f"numeros[1:8:2]: {numeros[1:8:2]}")  # Elementos del 1 al 7 con paso 2
print(f"numeros[::3]: {numeros[::3]}")  # Todos los elementos con paso 3
print(f"numeros[::-1]: {numeros[::-1]}")  # Tupla invertida
print()

# === 4. Inmutabilidad de Tuplas ===
print("=== INMUTABILIDAD DE TUPLAS ===")

tupla = (1, 2, 3, 4, 5)
print(f"Tupla original: {tupla}")

# Las tuplas son inmutables, no se pueden modificar directamente
# tupla[0] = 10  # Esto daría un TypeError

# Para "modificar" una tupla, hay que crear una nueva
tupla_nueva = (10,) + tupla[1:]
print(f"Nueva tupla: {tupla_nueva}")

# La tupla original permanece sin cambios
print(f"Tupla original (sin cambios): {tupla}")

# Caso especial: si una tupla contiene objetos mutables, estos sí pueden modificarse
tupla_con_lista = (1, 2, [3, 4], 5)
print(f"\nTupla con lista: {tupla_con_lista}")

# Modificar la lista dentro de la tupla
tupla_con_lista[2][0] = 30
print(f"Después de modificar la lista interna: {tupla_con_lista}")

# Pero no podemos reemplazar la lista por otra
# tupla_con_lista[2] = [30, 40]  # Esto daría un TypeError
print()

# === 5. Métodos de Tuplas ===
print("=== MÉTODOS DE TUPLAS ===")

# Las tuplas tienen muy pocos métodos debido a su inmutabilidad

numeros = (1, 2, 3, 2, 4, 2, 5)
print(f"Tupla: {numeros}")

# count() - Contar ocurrencias de un elemento
print(f"Ocurrencias del número 2: {numeros.count(2)}")

# index() - Encontrar la posición de un elemento (primera ocurrencia)
print(f"Posición del número 3: {numeros.index(3)}")
print(f"Posición del número 2: {numeros.index(2)}")  # Primera ocurrencia

# Buscar a partir de un índice específico
print(f"Posición del número 2 a partir del índice 2: {numeros.index(2, 2)}")

# Buscar en un rango de índices
print(f"Posición del número 2 entre índices 3 y 6: {numeros.index(2, 3, 6)}")

# Si el elemento no existe, se produce un ValueError
# print(numeros.index(10))  # Esto lanzaría un ValueError
print()

# === 6. Operaciones con Tuplas ===
print("=== OPERACIONES CON TUPLAS ===")

# Concatenación (+)
tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)
concatenada = tupla1 + tupla2
print(f"{tupla1} + {tupla2} = {concatenada}")

# Repetición (*)
repetida = (0, 1) * 3
print(f"(0, 1) * 3 = {repetida}")

# Longitud (len)
print(f"Longitud de {tupla1}: {len(tupla1)}")

# Máximo y mínimo
numeros = (5, 2, 8, 1, 9)
print(f"Máximo de {numeros}: {max(numeros)}")
print(f"Mínimo de {numeros}: {min(numeros)}")

# Suma
print(f"Suma de {numeros}: {sum(numeros)}")

# Ordenar (sorted devuelve una lista, no una tupla)
desordenada = (3, 1, 4, 1, 5, 9)
ordenada = sorted(desordenada)
print(f"Tupla original: {desordenada}")
print(f"Ordenada (como lista): {ordenada}")
print(f"Ordenada (como tupla): {tuple(ordenada)}")

# Convertir a string (join)
frutas = ("manzana", "banana", "cereza")
texto = ", ".join(frutas)
print(f"Tupla convertida a string: '{texto}'")
print()

# === 7. Desempaquetado de Tuplas ===
print("=== DESEMPAQUETADO DE TUPLAS ===")

# Desempaquetado básico
coordenadas = (10, 20, 30)
x, y, z = coordenadas
print(f"Tupla: {coordenadas}")
print(f"Desempaquetado: x={x}, y={y}, z={z}")

# El número de variables debe coincidir con el número de elementos
# a, b = coordenadas  # Esto daría un ValueError (demasiados valores para desempaquetar)
# a, b, c, d = coordenadas  # Esto daría un ValueError (no hay suficientes valores)

# Desempaquetado con * (asterisco) para capturar múltiples elementos
numeros = (1, 2, 3, 4, 5)
primero, *medio, ultimo = numeros
print(f"\nTupla: {numeros}")
print(f"Desempaquetado con *: primero={primero}, medio={medio}, ultimo={ultimo}")

# Otro ejemplo
*inicio, penultimo, ultimo = numeros
print(f"Otro desempaquetado: inicio={inicio}, penultimo={penultimo}, ultimo={ultimo}")

# Ignorar valores con _ (convención)
a, _, c, _, e = numeros
print(f"Ignorando valores: a={a}, c={c}, e={e}")

# Intercambio de variables usando tuplas
a, b = 10, 20
print(f"\nAntes del intercambio: a={a}, b={b}")
a, b = b, a  # Intercambio usando desempaquetado de tuplas
print(f"Después del intercambio: a={a}, b={b}")

# Retorno múltiple en funciones
def obtener_dimensiones():
    return (1920, 1080)  # Retorna una tupla

ancho, alto = obtener_dimensiones()  # Desempaqueta la tupla retornada
print(f"\nDimensiones: ancho={ancho}, alto={alto}")
print()

# === 8. Tuplas vs Listas ===
print("=== TUPLAS VS LISTAS ===")

# Rendimiento
import sys
import time

# Tamaño en memoria
lista = [1, 2, 3, 4, 5]
tupla = (1, 2, 3, 4, 5)

tamano_lista = sys.getsizeof(lista)
tamano_tupla = sys.getsizeof(tupla)

print(f"Tamaño de lista {lista}: {tamano_lista} bytes")
print(f"Tamaño de tupla {tupla}: {tamano_tupla} bytes")
print(f"Diferencia: {tamano_lista - tamano_tupla} bytes")

# Velocidad de creación
inicio = time.time()
for _ in range(1000000):
    _ = [1, 2, 3, 4, 5]
fin = time.time()
tiempo_lista = fin - inicio

inicio = time.time()
for _ in range(1000000):
    _ = (1, 2, 3, 4, 5)
fin = time.time()
tiempo_tupla = fin - inicio

print(f"\nTiempo para crear 1,000,000 de listas: {tiempo_lista:.6f} segundos")
print(f"Tiempo para crear 1,000,000 de tuplas: {tiempo_tupla:.6f} segundos")
print(f"Relación: las listas toman {tiempo_lista/tiempo_tupla:.2f} veces más tiempo")

# Cuándo usar tuplas vs listas
print("\nCuándo usar tuplas vs listas:")
print("- Usa tuplas para datos heterogéneos, listas para datos homogéneos")
print("- Usa tuplas para colecciones inmutables (que no cambiarán)")
print("- Usa tuplas como claves de diccionarios (las listas no pueden ser claves)")
print("- Usa tuplas para datos que deben ser protegidos contra modificaciones")
print("- Usa listas cuando necesites añadir, eliminar o modificar elementos")
print()

# === 9. Tuplas como Registros ===
print("=== TUPLAS COMO REGISTROS ===")

# Las tuplas pueden usarse como registros o estructuras simples
estudiante = ("Juan Pérez", 20, "Ingeniería", 8.7)
print(f"Registro de estudiante: {estudiante}")

# Desempaquetado para acceder a los campos
nombre, edad, carrera, promedio = estudiante
print(f"Nombre: {nombre}")
print(f"Edad: {edad}")
print(f"Carrera: {carrera}")
print(f"Promedio: {promedio}")

# Colección de registros
estudiantes = [
    ("Juan Pérez", 20, "Ingeniería", 8.7),
    ("Ana García", 22, "Medicina", 9.2),
    ("Carlos López", 19, "Economía", 7.8)
]

print("\nLista de estudiantes:")
for estudiante in estudiantes:
    nombre, edad, carrera, promedio = estudiante
    print(f"{nombre}, {edad} años, {carrera}, Promedio: {promedio}")

# Usando namedtuple para tuplas con nombres de campo
from collections import namedtuple

# Definir un tipo de tupla con nombres
Estudiante = namedtuple('Estudiante', ['nombre', 'edad', 'carrera', 'promedio'])

# Crear instancias
e1 = Estudiante("María Rodríguez", 21, "Arquitectura", 8.9)
e2 = Estudiante("Pedro Sánchez", 23, "Física", 9.5)

print("\nUsando namedtuple:")
print(f"Estudiante 1: {e1}")
print(f"Nombre: {e1.nombre}, Carrera: {e1.carrera}")
print(f"Estudiante 2: {e2}")
print(f"Edad: {e2.edad}, Promedio: {e2.promedio}")

# También se puede acceder por índice
print(f"Nombre de e1 por índice: {e1[0]}")
print()

# === 10. Conversiones entre Tuplas y Otros Tipos ===
print("=== CONVERSIONES ENTRE TUPLAS Y OTROS TIPOS ===")

# Lista a tupla
lista = [1, 2, 3, 4, 5]
tupla_desde_lista = tuple(lista)
print(f"Lista: {lista}")
print(f"Tupla desde lista: {tupla_desde_lista}")

# Tupla a lista
tupla = (5, 6, 7, 8, 9)
lista_desde_tupla = list(tupla)
print(f"Tupla: {tupla}")
print(f"Lista desde tupla: {lista_desde_tupla}")

# String a tupla
texto = "Python"
tupla_desde_texto = tuple(texto)
print(f"Texto: {texto}")
print(f"Tupla desde texto: {tupla_desde_texto}")

# Rango a tupla
rango = range(1, 6)
tupla_desde_rango = tuple(rango)
print(f"Rango: {rango}")
print(f"Tupla desde rango: {tupla_desde_rango}")

# Diccionario a tupla (solo las claves)
diccionario = {'a': 1, 'b': 2, 'c': 3}
tupla_desde_dict = tuple(diccionario)
print(f"Diccionario: {diccionario}")
print(f"Tupla desde diccionario (claves): {tupla_desde_dict}")

# Conjunto a tupla
conjunto = {1, 2, 3, 4, 5}
tupla_desde_conjunto = tuple(conjunto)
print(f"Conjunto: {conjunto}")
print(f"Tupla desde conjunto: {tupla_desde_conjunto}")
print()

# === 11. Comprensión de Generadores (similar a comprensión de listas) ===
print("=== COMPRENSIÓN DE GENERADORES ===")

# La comprensión de generadores crea un generador, no una tupla
generador = (x**2 for x in range(10))
print(f"Generador: {generador}")

# Convertir el generador a tupla
tupla_desde_generador = tuple(generador)
print(f"Tupla desde generador: {tupla_desde_generador}")

# Otro ejemplo
generador = (x for x in range(100) if x % 10 == 0)
print(f"Tupla de múltiplos de 10: {tuple(generador)}")

# Comparación de memoria con listas
import sys

# Generador (no almacena todos los valores en memoria)
generador = (x for x in range(1000))
tamano_generador = sys.getsizeof(generador)

# Lista por comprensión (almacena todos los valores)
lista = [x for x in range(1000)]
tamano_lista = sys.getsizeof(lista)

# Tupla (almacena todos los valores)
tupla = tuple(range(1000))
tamano_tupla = sys.getsizeof(tupla)

print(f"\nTamaño del generador: {tamano_generador} bytes")
print(f"Tamaño de la lista: {tamano_lista} bytes")
print(f"Tamaño de la tupla: {tamano_tupla} bytes")
print()

# === 12. Ejemplos Prácticos ===
print("=== EJEMPLOS PRÁCTICOS ===")

# Ejemplo 1: Coordenadas geográficas
def distancia_entre_puntos(punto1, punto2):
    """Calcula la distancia euclidiana entre dos puntos"""
    import math
    return math.sqrt((punto2[0] - punto1[0])**2 + (punto2[1] - punto1[1])**2)

# Tuplas como coordenadas (x, y)
punto_a = (0, 0)
punto_b = (3, 4)
print(f"Punto A: {punto_a}, Punto B: {punto_b}")
print(f"Distancia entre A y B: {distancia_entre_puntos(punto_a, punto_b)}")

# Ejemplo 2: Colores RGB
def es_color_oscuro(color):
    """Determina si un color RGB es oscuro"""
    r, g, b = color
    return (r + g + b) / 3 < 128

# Tuplas como colores RGB (r, g, b)
rojo = (255, 0, 0)
verde = (0, 255, 0)
azul = (0, 0, 255)
negro = (0, 0, 0)
blanco = (255, 255, 255)

print(f"\nColores:")
print(f"Rojo {rojo} es oscuro: {es_color_oscuro(rojo)}")
print(f"Verde {verde} es oscuro: {es_color_oscuro(verde)}")
print(f"Azul {azul} es oscuro: {es_color_oscuro(azul)}")
print(f"Negro {negro} es oscuro: {es_color_oscuro(negro)}")
print(f"Blanco {blanco} es oscuro: {es_color_oscuro(blanco)}")

# Ejemplo 3: Retorno múltiple en funciones
def estadisticas(numeros):
    """Calcula varias estadísticas de una secuencia de números"""
    return min(numeros), max(numeros), sum(numeros) / len(numeros)

datos = [5, 2, 9, 1, 7, 3, 8]
minimo, maximo, promedio = estadisticas(datos)
print(f"\nDatos: {datos}")
print(f"Mínimo: {minimo}, Máximo: {maximo}, Promedio: {promedio:.2f}")

# Ejemplo 4: Tuplas como claves de diccionarios
# Las tuplas pueden ser claves de diccionarios porque son inmutables
coordenadas_valores = {
    (0, 0): "Origen",
    (1, 0): "Este",
    (0, 1): "Norte",
    (1, 1): "Noreste"
}

print(f"\nValor en el origen: {coordenadas_valores[(0, 0)]}")
print(f"Valor en el noreste: {coordenadas_valores[(1, 1)]}")

# Ejemplo 5: Tuplas para representar fechas
from datetime import date

# Convertir tupla a fecha
def tupla_a_fecha(tupla_fecha):
    """Convierte una tupla (año, mes, día) a un objeto date"""
    return date(*tupla_fecha)

fecha_tupla = (2023, 5, 15)
fecha_obj = tupla_a_fecha(fecha_tupla)
print(f"\nTupla de fecha: {fecha_tupla}")
print(f"Objeto date: {fecha_obj}")
print(f"Día de la semana: {fecha_obj.strftime('%A')}")