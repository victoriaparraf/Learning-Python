# EXCEPCIONES EN PYTHON

# 1. Manejo básico de excepciones con try-except
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Error: No se puede dividir entre cero.")

# 2. Múltiples excepciones
try:
    lista = [1, 2, 3]
    print(lista[5])
except IndexError:
    print("Error: Índice fuera de rango.")
except ZeroDivisionError:
    print("Error: División por cero.")

# 3. Captura de la excepción como variable
try:
    int("hola")
except ValueError as e:
    print(f"Ocurrió un error: {e}")

# 4. Uso de else (se ejecuta si no hay excepción)
try:
    numero = int("123")
except ValueError:
    print("No se pudo convertir el número.")
else:
    print("Conversión exitosa:", numero)

# 5. Uso de finally (se ejecuta siempre)
try:
    archivo = open("archivo_que_no_existe.txt", "r")
except FileNotFoundError:
    print("Archivo no encontrado.")
finally:
    print("Este bloque se ejecuta siempre.")

# 6. Lanzar excepciones con raise
def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("Intentaste dividir por cero.")
    return a / b

try:
    print(dividir(10, 0))
except ZeroDivisionError as e:
    print("Error lanzado:", e)

# 7. Crear excepciones personalizadas
class MiError(Exception):
    """Una excepción personalizada"""
    pass

def verificar_edad(edad):
    if edad < 18:
        raise MiError("Debes ser mayor de edad.")
    print("Acceso concedido.")

try:
    verificar_edad(16)
except MiError as e:
    print("Excepción personalizada:", e)

# 8. Atrapando cualquier excepción (no recomendado salvo en casos controlados)
try:
    x = 10 / 0
except Exception as e:
    print(f"Se capturó una excepción inesperada: {e}")

