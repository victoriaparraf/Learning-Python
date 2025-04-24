# ===== NIVEL BÁSICO =====
# ===== Imprimir en pantalla =====
print('hola mundo')

# ===== VARIABLES EN PYTHON =====
# Las variables son espacios en memoria que almacenan valores
# Python es de tipado dinámico (no necesitas declarar el tipo)

# === Declaración de variables ===
nombre = "Ana"
edad = 25
altura = 1.75
es_estudiante = True

# Imprimir variables
print("=== Variables básicas ===")
print(f"Nombre: {nombre}")
print(f"Edad: {edad}")
print(f"Altura: {altura}")
print(f"¿Es estudiante?: {es_estudiante}")
print()

# === Tipos de datos básicos ===
print("=== Tipos de datos ===")
print(f"Tipo de 'nombre': {type(nombre)}")       # str (string/cadena)
print(f"Tipo de 'edad': {type(edad)}")           # int (entero)
print(f"Tipo de 'altura': {type(altura)}")       # float (decimal)
print(f"Tipo de 'es_estudiante': {type(es_estudiante)}")  # bool (booleano)
print()

# === Reasignación de variables ===
# Las variables pueden cambiar de valor y tipo
print("=== Reasignación de variables ===")
contador = 10
print(f"Contador (inicial): {contador}, tipo: {type(contador)}")

contador = "diez"
print(f"Contador (reasignado): {contador}, tipo: {type(contador)}")
print()

# === Variables múltiples en una línea ===
print("=== Asignación múltiple ===")
x, y, z = 5, "Hola", False
print(f"x: {x}, y: {y}, z: {z}")

# Asignar el mismo valor a múltiples variables
a = b = c = 100
print(f"a: {a}, b: {b}, c: {c}")
print()

# === Nombres de variables ===
# Reglas:
# - Pueden contener letras, números y guiones bajos
# - No pueden empezar con un número
# - No pueden ser palabras reservadas (if, for, while, etc.)
# - Son sensibles a mayúsculas/minúsculas (case-sensitive)

mi_variable = 42          # Convención: snake_case para variables
MiVariable = 42           # CamelCase (no es la convención en Python)
_variable_privada = 42    # Las variables que empiezan con _ suelen indicar privacidad
print("=== Convenciones de nombres ===")
print(f"snake_case: {mi_variable}")
print(f"CamelCase: {MiVariable}")
print(f"Variable con _: {_variable_privada}")
print()

# === Constantes ===
# Python no tiene constantes reales, pero por convención
# se usan MAYÚSCULAS para indicar que una variable no debe cambiar
PI = 3.14159
GRAVEDAD = 9.8
print("=== Constantes (por convención) ===")
print(f"PI: {PI}")
print(f"GRAVEDAD: {GRAVEDAD}")
print()

# === Eliminación de variables ===
temporal = "Esto se eliminará"
print(f"Variable temporal: {temporal}")
del temporal
# print(f"Después de eliminar: {temporal}")  # Esto daría error

# === Variables y alcance (scope) ===
def funcion_ejemplo():
    # Variable local (solo existe dentro de la función)
    variable_local = "Solo existo dentro de la función"
    print(f"Dentro de la función: {variable_local}")
    # También podemos acceder a variables globales
    print(f"Accediendo a variable global desde función: {nombre}")

print("\n=== Variables y alcance ===")
funcion_ejemplo()
# print(variable_local)  # Esto daría error porque es local a la función