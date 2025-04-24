# Condicionales en Python

# if simple
edad = 18
if edad >= 18:
    print("Eres mayor de edad")

# if-else
nota = 6
if nota >= 5:
    print("Aprobado")
else:
    print("Reprobado")

# if-elif-else
calificacion = 8
if calificacion >= 9:
    print("Excelente")
elif calificacion >= 7:
    print("Bueno")
elif calificacion >= 5:
    print("Regular")
else:
    print("Insuficiente")

# Condicionales anidados
numero = 15
if numero > 0:
    if numero % 2 == 0:
        print("Número positivo y par")
    else:
        print("Número positivo e impar")
else:
    print("Número no positivo")

# Uso de operadores lógicos
usuario = "admin"
contrasena = "1234"
if usuario == "admin" and contrasena == "1234":
    print("Acceso concedido")
else:
    print("Acceso denegado")

# Uso de 'or'
edad = 65
if edad < 18 or edad >= 60:
    print("Tienes descuento")
else:
    print("Precio completo")

# Uso de 'not'
está_lloviendo = False
if not está_lloviendo:
    print("Puedes salir sin paraguas")

# Operador ternario
numero = 7
par_o_impar = "Par" if numero % 2 == 0 else "Impar"
print(f"El número es {par_o_impar}")

# Comparación de múltiples valores
color = "rojo"
if color in ["rojo", "azul", "verde"]:
    print("Color permitido")
else:
    print("Color no permitido")
