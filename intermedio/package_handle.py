# MANEJO DE PAQUETES EN PYTHON

# --------------------------------------
# 1. IMPORTAR PAQUETES ESTÁNDAR
import math
print("Raíz cuadrada de 16:", math.sqrt(16))

# --------------------------------------
# 2. INSTALAR PAQUETES CON PIP
# (Esto se hace por terminal, no en el código)
# pip install requests

import requests
respuesta = requests.get("https://httpbin.org/get")
print("Status code con requests:", respuesta.status_code)

# --------------------------------------
# 3. CREAR TU PROPIO PAQUETE

# Supongamos esta estructura:
# mi_paquete/
# ├── __init__.py
# ├── operaciones.py
# └── herramientas/
#     ├── __init__.py
#     └── saludos.py

# Contenido de operaciones.py
# def suma(a, b): return a + b

# Contenido de saludos.py
# def saludar(nombre): return f"Hola, {nombre}"

# Y ahora lo importamos:

# from mi_paquete.operaciones import suma
# from mi_paquete.herramientas.saludos import saludar

# print(suma(2, 3))
# print(saludar("Juan"))

# --------------------------------------
# 4. USAR ALIAS AL IMPORTAR
import math as m
print("Coseno de 0:", m.cos(0))

# --------------------------------------
# 5. IMPORTAR SOLO UNA FUNCIÓN
from math import sqrt
print("Raíz cuadrada:", sqrt(25))

# --------------------------------------
# 6. USAR __init__.py
# Este archivo puede estar vacío o contener código que se ejecuta al importar el paquete.
# También puedes definir qué se exporta:
# __init__.py:
# __all__ = ['modulo1', 'modulo2']

# --------------------------------------
# 7. PAQUETES EXTERNOS COMUNES
# pip install numpy
# pip install pandas
# pip install matplotlib

# Ejemplo:
# import numpy as np
# arreglo = np.array([1, 2, 3])
# print("Numpy array:", arreglo)

# --------------------------------------
# 8. VER PAQUETES INSTALADOS
# Desde terminal:
# pip list

# --------------------------------------
# 9. VER DETALLES DE UN PAQUETE
# pip show nombre_del_paquete
# Ejemplo:
# pip show requests

# --------------------------------------
# 10. INSTALAR UNA VERSIÓN ESPECÍFICA
# pip install paquete==versión
# pip install numpy==1.23.0

# --------------------------------------
# 11. CREAR requirements.txt
# Este archivo lista los paquetes necesarios para un proyecto

# requests==2.31.0
# numpy>=1.23

# Para instalar todos:
# pip install -r requirements.txt

# --------------------------------------
# 12. INSTALACIÓN LOCAL DE UN PAQUETE
# Si tienes una carpeta con un paquete local:
# pip install ./mi_paquete

# --------------------------------------
# 13. PAQUETES VS MÓDULOS
# Un módulo es un solo archivo `.py`
# Un paquete es una carpeta con `__init__.py` y módulos dentro

# --------------------------------------
# 14. INSTALACIÓN GLOBAL VS VIRTUAL ENV
# Recomendado: trabajar en un entorno virtual
# python -m venv venv
# source venv/bin/activate (Linux/mac) o venv\Scripts\activate (Windows)

# --------------------------------------
# 15. DESINSTALAR PAQUETES
# pip uninstall nombre_del_paquete
