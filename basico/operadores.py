# ===== OPERADORES EN PYTHON =====

# === 1. Operadores Aritméticos ===
print("=== OPERADORES ARITMÉTICOS ===")
a, b = 10, 3

# Suma (+)
suma = a + b
print(f"{a} + {b} = {suma}")

# Resta (-)
resta = a - b
print(f"{a} - {b} = {resta}")

# Multiplicación (*)
multiplicacion = a * b
print(f"{a} * {b} = {multiplicacion}")

# División (/)
division = a / b  # Siempre devuelve un float
print(f"{a} / {b} = {division}")

# División entera (//)
division_entera = a // b  # Devuelve solo la parte entera
print(f"{a} // {b} = {division_entera}")

# Módulo (%)
modulo = a % b  # Devuelve el resto de la división
print(f"{a} % {b} = {modulo}")

# Exponente (**)
exponente = a ** b  # a elevado a b
print(f"{a} ** {b} = {exponente}")

# Negación (-)
negacion = -a
print(f"Negación de {a} = {negacion}")
print()

# === 2. Operadores de Asignación ===
print("=== OPERADORES DE ASIGNACIÓN ===")
x = 5
print(f"Valor inicial de x: {x}")

# Asignación simple (=)
x = 10
print(f"x = 10: {x}")

# Asignación con suma (+=)
x += 3  # Equivalente a x = x + 3
print(f"x += 3: {x}")

# Asignación con resta (-=)
x -= 2  # Equivalente a x = x - 2
print(f"x -= 2: {x}")

# Asignación con multiplicación (*=)
x *= 2  # Equivalente a x = x * 2
print(f"x *= 2: {x}")

# Asignación con división (/=)
x /= 4  # Equivalente a x = x / 4
print(f"x /= 4: {x}")

# Asignación con división entera (//=)
x = 10
x //= 3  # Equivalente a x = x // 3
print(f"x //= 3: {x}")

# Asignación con módulo (%=)
x %= 2  # Equivalente a x = x % 2
print(f"x %= 2: {x}")

# Asignación con exponente (**=)
x = 2
x **= 3  # Equivalente a x = x ** 3
print(f"x **= 3: {x}")
print()

# === 3. Operadores de Comparación ===
print("=== OPERADORES DE COMPARACIÓN ===")
a, b = 5, 10
c = 5

# Igual a (==)
print(f"{a} == {b}: {a == b}")
print(f"{a} == {c}: {a == c}")

# Diferente de (!=)
print(f"{a} != {b}: {a != b}")
print(f"{a} != {c}: {a != c}")

# Mayor que (>)
print(f"{a} > {b}: {a > b}")
print(f"{b} > {a}: {b > a}")

# Menor que (<)
print(f"{a} < {b}: {a < b}")
print(f"{b} < {a}: {b < a}")

# Mayor o igual que (>=)
print(f"{a} >= {c}: {a >= c}")
print(f"{a} >= {b}: {a >= b}")

# Menor o igual que (<=)
print(f"{a} <= {c}: {a <= c}")
print(f"{b} <= {a}: {b <= a}")
print()

# === 4. Operadores Lógicos ===
print("=== OPERADORES LÓGICOS ===")
p, q = True, False

# AND lógico (and)
print(f"True and True: {True and True}")
print(f"True and False: {True and False}")
print(f"False and True: {False and True}")
print(f"False and False: {False and False}")

# OR lógico (or)
print(f"True or True: {True or True}")
print(f"True or False: {True or False}")
print(f"False or True: {False or True}")
print(f"False or False: {False or False}")

# NOT lógico (not)
print(f"not True: {not True}")
print(f"not False: {not False}")

# Ejemplo práctico
edad = 25
tiene_licencia = True
puede_conducir = edad >= 18 and tiene_licencia
print(f"Edad: {edad}, Tiene licencia: {tiene_licencia}")
print(f"¿Puede conducir?: {puede_conducir}")
print()

# === 5. Operadores de Identidad ===
print("=== OPERADORES DE IDENTIDAD ===")
# is: Devuelve True si ambas variables son el mismo objeto
# is not: Devuelve True si no son el mismo objeto

lista1 = [1, 2, 3]
lista2 = [1, 2, 3]
lista3 = lista1

print(f"lista1: {lista1}")
print(f"lista2: {lista2}")
print(f"lista3: {lista3}")

print(f"lista1 == lista2: {lista1 == lista2}")  # Compara valores
print(f"lista1 is lista2: {lista1 is lista2}")  # Compara identidad (referencia)
print(f"lista1 is lista3: {lista1 is lista3}")  # Misma referencia
print(f"lista1 is not lista2: {lista1 is not lista2}")
print()

# === 6. Operadores de Pertenencia ===
print("=== OPERADORES DE PERTENENCIA ===")
# in: Devuelve True si un valor está en la secuencia
# not in: Devuelve True si un valor no está en la secuencia

frutas = ["manzana", "banana", "cereza"]
print(f"Lista de frutas: {frutas}")

print(f"'manzana' in frutas: {'manzana' in frutas}")
print(f"'pera' in frutas: {'pera' in frutas}")
print(f"'pera' not in frutas: {'pera' not in frutas}")

texto = "Python es genial"
print(f"Texto: '{texto}'")
print(f"'Python' in texto: {'Python' in texto}")
print(f"'Java' in texto: {'Java' in texto}")
print()

# === 7. Operadores Bit a Bit (Bitwise) ===
print("=== OPERADORES BIT A BIT ===")
x, y = 10, 7  # En binario: 1010 y 0111

# AND bit a bit (&)
print(f"{x} & {y} = {x & y}")  # 1010 & 0111 = 0010 (2 en decimal)

# OR bit a bit (|)
print(f"{x} | {y} = {x | y}")  # 1010 | 0111 = 1111 (15 en decimal)

# XOR bit a bit (^)
print(f"{x} ^ {y} = {x ^ y}")  # 1010 ^ 0111 = 1101 (13 en decimal)

# NOT bit a bit (~)
print(f"~{x} = {~x}")  # ~1010 = -1011 (-11 en decimal)

# Desplazamiento a la izquierda (<<)
print(f"{x} << 1 = {x << 1}")  # 1010 << 1 = 10100 (20 en decimal)

# Desplazamiento a la derecha (>>)
print(f"{x} >> 1 = {x >> 1}")  # 1010 >> 1 = 0101 (5 en decimal)
print()

# === 8. Precedencia de Operadores ===
print("=== PRECEDENCIA DE OPERADORES ===")
# La precedencia determina el orden en que se evalúan las operaciones

resultado = 5 + 3 * 2
print(f"5 + 3 * 2 = {resultado}")  # La multiplicación tiene mayor precedencia

resultado = (5 + 3) * 2
print(f"(5 + 3) * 2 = {resultado}")  # Los paréntesis tienen la mayor precedencia

# Orden de precedencia (de mayor a menor):
# 1. Paréntesis ()
# 2. Exponentes **
# 3. Unarios +, -, ~
# 4. Multiplicativos *, /, //, %
# 5. Aditivos +, -
# 6. Desplazamientos <<, >>
# 7. AND bit a bit &
# 8. XOR bit a bit ^
# 9. OR bit a bit |
# 10. Comparaciones ==, !=, >, >=, <, <=, is, is not, in, not in
# 11. NOT lógico not
# 12. AND lógico and
# 13. OR lógico or

expresion_compleja = 2 ** 3 * 4 + 5 * 2 // 3
# Se evalúa como: ((2 ** 3) * 4) + ((5 * 2) // 3)
# = (8 * 4) + (10 // 3)
# = 32 + 3
# = 35
print(f"2 ** 3 * 4 + 5 * 2 // 3 = {expresion_compleja}")

# Usando paréntesis para cambiar la precedencia
expresion_con_parentesis = 2 ** (3 * 4) + 5 * (2 // 3)
# = 2 ** 12 + 5 * 0
# = 4096 + 0
# = 4096
print(f"2 ** (3 * 4) + 5 * (2 // 3) = {expresion_con_parentesis}")