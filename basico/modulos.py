# MÓDULOS EN PYTHON

# 1. Importar un módulo completo
import math
print("Raíz cuadrada de 16:", math.sqrt(16))
print("Valor de pi:", math.pi)

# 2. Importar una función específica
from math import pow
print("2 elevado a 3:", pow(2, 3))

# 3. Importar con alias
import datetime as dt
ahora = dt.datetime.now()
print("Fecha y hora actual:", ahora)

# 4. Crear y usar un módulo propio
# Supongamos que tienes un archivo llamado "saludos.py" con este contenido:
# Lo usarías así:
from saludar import saludar
saludar("Ana")
print("Ejemplo de módulo propio: saludos.saludar('Ana')")

# 5. Listar nombres disponibles en un módulo
import random
print("Funciones disponibles en 'random':", dir(random))

# 6. Usar __name__ para definir el comportamiento al importar
def funcion_principal():
    print("Esta función se ejecuta solo si corres este archivo directamente.")

if __name__ == "__main__":
    funcion_principal()

# 7. Uso del módulo sys
import sys
print("Versión de Python:", sys.version)

# 8. Módulo os para interactuar con el sistema operativo
import os
print("Directorio actual:", os.getcwd())

# 9. Módulo json para trabajar con datos en formato JSON
import json
persona = {"nombre": "Luis", "edad": 30}
persona_json = json.dumps(persona)
print("JSON:", persona_json)

# 10. Instalación e importación de módulos externos (usando pip)
# Ejemplo (no ejecutable desde aquí, pero válido en tu entorno local):
# pip install requests
# import requests
# response = requests.get("https://api.github.com")
# print(response.status_code)
