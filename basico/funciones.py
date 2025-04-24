# FUNCIONES EN PYTHON

# 1. Función simple
def saludar():
    print("Hola, bienvenido a Python")

saludar()

# 2. Función con parámetros
def saludar_persona(nombre):
    print(f"Hola, {nombre}")

saludar_persona("Carlos")

# 3. Función con retorno de valor
def sumar(a, b):
    return a + b

resultado = sumar(3, 5)
print("Suma:", resultado)

# 4. Función con parámetros por defecto
def saludar_con_estilo(nombre="Amigo"):
    print(f"¡Hola, {nombre}! Qué bueno verte.")

saludar_con_estilo()
saludar_con_estilo("Ana")

# 5. Función con argumentos arbitrarios (*args)
def listar_nombres(*nombres):
    for nombre in nombres:
        print("Nombre:", nombre)

listar_nombres("Ana", "Luis", "Pedro")

# 6. Función con argumentos arbitrarios de palabra clave (**kwargs)
def mostrar_info(**info):
    for clave, valor in info.items():
        print(f"{clave}: {valor}")

mostrar_info(nombre="Laura", edad=28, ciudad="Madrid")

# 7. Función dentro de otra función (función anidada)
def operacion(a, b):
    def sumar(x, y):
        return x + y
    return sumar(a, b)

print("Resultado de función anidada:", operacion(10, 5))

# 8. Función lambda
doble = lambda x: x * 2
print("Doble de 4:", doble(4))

# 9. Función con docstring (documentación)
def dividir(a, b):
    """
    Divide dos números y devuelve el resultado.
    """
    if b == 0:
        return "No se puede dividir entre cero."
    return a / b

print("División:", dividir(10, 2))
print(dividir.__doc__)

