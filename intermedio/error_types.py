# TIPOS DE ERRORES EN PYTHON

# --------------------------------------
# 1. SyntaxError (Error de sintaxis)
# Ocurre cuando el código está mal escrito.

# print("Hola mundo"  # Falta cerrar paréntesis => SyntaxError

# --------------------------------------
# 2. NameError
# Se refiere a una variable que no está definida.

try:
    print(variable_no_definida)
except NameError as e:
    print("NameError:", e)

# --------------------------------------
# 3. TypeError
# Ocurre cuando se usa un tipo de dato inapropiado.

try:
    resultado = '3' + 2  # No se puede sumar string con int
except TypeError as e:
    print("TypeError:", e)

# --------------------------------------
# 4. ValueError
# Ocurre cuando un valor tiene el tipo correcto, pero no el valor adecuado.

try:
    numero = int("abc")  # No se puede convertir 'abc' en entero
except ValueError as e:
    print("ValueError:", e)

# --------------------------------------
# 5. IndexError
# Se accede a un índice fuera del rango de una lista.

lista = [1, 2, 3]
try:
    print(lista[5])
except IndexError as e:
    print("IndexError:", e)

# --------------------------------------
# 6. KeyError
# Se intenta acceder a una clave inexistente en un diccionario.

diccionario = {"a": 1, "b": 2}
try:
    print(diccionario["z"])
except KeyError as e:
    print("KeyError:", e)

# --------------------------------------
# 7. AttributeError
# Se usa un método o atributo que no existe para un objeto.

texto = "hola"
try:
    texto.append("!")
except AttributeError as e:
    print("AttributeError:", e)

# --------------------------------------
# 8. ZeroDivisionError
# División entre cero.

try:
    resultado = 10 / 0
except ZeroDivisionError as e:
    print("ZeroDivisionError:", e)

# --------------------------------------
# 9. ImportError
# Fallo al importar un módulo.

try:
    import modulo_que_no_existe
except ImportError as e:
    print("ImportError:", e)

# --------------------------------------
# 10. ModuleNotFoundError
# Es un subtipo de ImportError, más específico.

try:
    import fake_module
except ModuleNotFoundError as e:
    print("ModuleNotFoundError:", e)

# --------------------------------------
# 11. FileNotFoundError
# Se intenta abrir un archivo que no existe.

try:
    with open("archivo_inexistente.txt", "r") as f:
        contenido = f.read()
except FileNotFoundError as e:
    print("FileNotFoundError:", e)

# --------------------------------------
# 12. IndentationError
# Error en la indentación del código.

# def saludar():
# print("Hola")  # Esto generaría un IndentationError

# --------------------------------------
# 13. RecursionError
# Llamadas recursivas infinitas.

def recursivo():
    return recursivo()

# try:
#     recursivo()
# except RecursionError as e:
#     print("RecursionError:", e)

# --------------------------------------
# 14. MemoryError
# El sistema se queda sin memoria. (Muy raro en scripts simples)
# Ejemplo teórico:
# lista = [1] * (10**10)

# --------------------------------------
# MANEJO GENERAL DE ERRORES
try:
    x = int("no número")
except ValueError:
    print("Hubo un ValueError")
except Exception as e:
    print("Otro error ocurrió:", type(e).__name__, "-", e)
finally:
    print("Esto siempre se ejecuta (bloque finally)")
