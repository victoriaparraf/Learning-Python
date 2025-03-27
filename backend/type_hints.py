#type hints
from typing import Optional

mi_variable: str = "Hola Mundo"
otra_variable: int = 10
print(mi_variable)
print(otra_variable)

def saludo(nombre: str) -> str:
    return f"Hola {nombre}"

def suma(a: int, b: int) -> int:
    return a + b

def frase(nombre: str, edad: int, mensaje: Optional[str]) -> str:
    # Optional significa que el argumento es opcional
    if mensaje:
        return f"{nombre} tiene {edad} años y dice {mensaje}"
    else:
        return f"{nombre} tiene {edad} años"

