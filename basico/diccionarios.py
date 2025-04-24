# Diccionarios en Python

# Crear un diccionario vacío
diccionario_vacio = {}
print("Diccionario vacío:", diccionario_vacio)

# Crear un diccionario con valores
diccionario = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Bogotá"
}
print("Diccionario con datos:", diccionario)

# Acceder a valores por su clave
print("Nombre:", diccionario["nombre"])

# Modificar un valor
diccionario["edad"] = 31
print("Edad modificada:", diccionario["edad"])

# Agregar una nueva clave-valor
diccionario["profesion"] = "Ingeniero"
print("Nuevo diccionario:", diccionario)

# Eliminar un elemento
del diccionario["ciudad"]
print("Después de eliminar ciudad:", diccionario)

# Obtener todas las claves
print("Claves:", list(diccionario.keys()))

# Obtener todos los valores
print("Valores:", list(diccionario.values()))

# Obtener todos los pares clave-valor
print("Items:", list(diccionario.items()))

# Recorrer el diccionario
for clave, valor in diccionario.items():
    print(f"{clave}: {valor}")

# Verificar si una clave existe
print("¿Existe 'nombre'?", "nombre" in diccionario)
print("¿Existe 'ciudad'?", "ciudad" in diccionario)

# Obtener un valor con get (sin error si no existe la clave)
print("Obtener 'nombre':", diccionario.get("nombre"))
print("Obtener 'ciudad':", diccionario.get("ciudad", "No existe"))

# Diccionarios anidados
datos_usuario = {
    "usuario1": {"nombre": "Ana", "edad": 25},
    "usuario2": {"nombre": "Luis", "edad": 28}
}
print("Diccionarios anidados:", datos_usuario)
print("Edad de usuario1:", datos_usuario["usuario1"]["edad"])

# Usar diccionarios con otros tipos de valores
diccionario_complejo = {
    "numeros": [1, 2, 3],
    "config": {"modo": "oscuro", "tamaño": 12},
    "activo": True
}
print("Diccionario complejo:", diccionario_complejo)

# Eliminar todos los elementos del diccionario
diccionario.clear()
print("Diccionario limpio:", diccionario)

# Copiar un diccionario
copia = datos_usuario.copy()
print("Copia del diccionario:", copia)
