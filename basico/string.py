# ===== STRINGS EN PYTHON =====
# Los strings son secuencias inmutables de caracteres

# === 1. Creación de Strings ===
print("=== CREACIÓN DE STRINGS ===")

# Usando comillas simples
simple = 'Hola, mundo!'
print(f"Comillas simples: {simple}")

# Usando comillas dobles
doble = "Hola, mundo!"
print(f"Comillas dobles: {doble}")

# Usando comillas triples (para strings multilínea)
multilinea = """Este es un texto
que ocupa varias
líneas."""
print(f"String multilínea:\n{multilinea}")

# Usando comillas triples con comillas simples
multilinea2 = '''Otro texto
en múltiples
líneas.'''
print(f"Otro multilínea:\n{multilinea2}")

# Caracteres de escape
escape = "Esto es un \"texto\" con \\ caracteres \n de escape."
print(f"Con caracteres de escape: {escape}")

# String vacío
vacio = ""
print(f"String vacío: '{vacio}', longitud: {len(vacio)}")
print()

# === 2. Concatenación y Repetición ===
print("=== CONCATENACIÓN Y REPETICIÓN ===")

# Concatenación con +
nombre = "Juan"
apellido = "Pérez"
nombre_completo = nombre + " " + apellido
print(f"Concatenación: {nombre} + ' ' + {apellido} = {nombre_completo}")

# Repetición con *
repetido = "Eco " * 3
print(f"Repetición: 'Eco ' * 3 = {repetido}")

# Concatenación implícita (solo funciona con literales, no con variables)
mensaje = "Esto es " "un mensaje " "concatenado."
print(f"Concatenación implícita: {mensaje}")
print()

# === 3. Acceso a Caracteres (Indexación) ===
print("=== ACCESO A CARACTERES ===")

texto = "Python"
print(f"Texto: '{texto}'")

# Índices positivos (desde el principio, empezando en 0)
print(f"Primer carácter (índice 0): {texto[0]}")
print(f"Segundo carácter (índice 1): {texto[1]}")
print(f"Último carácter (índice 5): {texto[5]}")

# Índices negativos (desde el final, empezando en -1)
print(f"Último carácter (índice -1): {texto[-1]}")
print(f"Penúltimo carácter (índice -2): {texto[-2]}")
print(f"Primer carácter (índice -6): {texto[-6]}")
print()

# === 4. Slicing (Rebanado) ===
print("=== SLICING (REBANADO) ===")

texto = "Python es genial"
print(f"Texto: '{texto}'")

# Sintaxis: string[inicio:fin:paso]
# inicio: índice donde comienza (incluido)
# fin: índice donde termina (excluido)
# paso: salto entre caracteres

# Ejemplos básicos
print(f"texto[0:6]: '{texto[0:6]}'")  # Primeros 6 caracteres
print(f"texto[7:9]: '{texto[7:9]}'")  # Caracteres del 7 al 8
print(f"texto[10:]: '{texto[10:]}'")  # Del 10 hasta el final
print(f"texto[:6]: '{texto[:6]}'")    # Desde el inicio hasta el 5

# Con paso
print(f"texto[::2]: '{texto[::2]}'")  # Cada segundo carácter
print(f"texto[1::2]: '{texto[1::2]}'")  # Cada segundo carácter, empezando por el segundo

# Con índices negativos
print(f"texto[-6:]: '{texto[-6:]}'")  # Últimos 6 caracteres
print(f"texto[:-7]: '{texto[:-7]}'")  # Todo excepto los últimos 7 caracteres

# Invertir un string
print(f"texto[::-1]: '{texto[::-1]}'")  # String invertido
print()

# === 5. Métodos de Strings ===
print("=== MÉTODOS DE STRINGS ===")

texto = "  Python es un lenguaje de programación  "
print(f"Texto original: '{texto}'")

# Métodos de caso
print(f"upper(): '{texto.upper()}'")  # Todo a mayúsculas
print(f"lower(): '{texto.lower()}'")  # Todo a minúsculas
print(f"capitalize(): '{texto.capitalize()}'")  # Primera letra en mayúscula
print(f"title(): '{texto.title()}'")  # Primera letra de cada palabra en mayúscula
print(f"swapcase(): '{texto.swapcase()}'")  # Invierte mayúsculas y minúsculas

# Métodos de búsqueda
print(f"count('a'): {texto.count('a')}")  # Cuenta ocurrencias
print(f"find('es'): {texto.find('es')}")  # Índice de la primera ocurrencia (-1 si no existe)
print(f"rfind('es'): {texto.rfind('es')}")  # Índice de la última ocurrencia
print(f"index('Python'): {texto.index('Python')}")  # Como find, pero lanza error si no existe
# print(f"index('Java'): {texto.index('Java')}")  # Esto lanzaría un ValueError
print(f"startswith('  Py'): {texto.startswith('  Py')}")  # ¿Comienza con?
print(f"endswith('  '): {texto.endswith('  ')}")  # ¿Termina con?

# Métodos de eliminación de espacios
print(f"strip(): '{texto.strip()}'")  # Elimina espacios al inicio y final
print(f"lstrip(): '{texto.lstrip()}'")  # Elimina espacios al inicio
print(f"rstrip(): '{texto.rstrip()}'")  # Elimina espacios al final

# Métodos de reemplazo
print(f"replace('Python', 'Java'): '{texto.replace('Python', 'Java')}'")  # Reemplaza texto

# Métodos de división
palabras = texto.split()  # Divide por espacios por defecto
print(f"split(): {palabras}")
print(f"split('a'): {texto.split('a')}")  # Divide por el carácter 'a'
print(f"join(): {'|'.join(palabras)}")  # Une con el carácter '|'

# Métodos de comprobación
texto2 = "Python123"
print(f"\nTexto2: '{texto2}'")
print(f"isalpha(): {texto2.isalpha()}")  # ¿Solo letras?
print(f"isalnum(): {texto2.isalnum()}")  # ¿Letras o números?
print(f"isdigit(): {texto2.isdigit()}")  # ¿Solo dígitos?
print(f"islower(): {texto2.islower()}")  # ¿Todo en minúsculas?
print(f"isupper(): {texto2.isupper()}")  # ¿Todo en mayúsculas?
print(f"istitle(): {texto2.istitle()}")  # ¿Formato título?
print(f"isspace(): {texto2.isspace()}")  # ¿Solo espacios?

# Alineación y relleno
print(f"\ncenter(20, '*'): '{texto2.center(20, '*')}'")  # Centra en 20 caracteres
print(f"ljust(20, '-'): '{texto2.ljust(20, '-')}'")  # Alinea a la izquierda
print(f"rjust(20, '-'): '{texto2.rjust(20, '-')}'")  # Alinea a la derecha
print(f"zfill(10): '{texto2.zfill(10)}'")  # Rellena con ceros a la izquierda
print()

# === 6. Formateo de Strings ===
print("=== FORMATEO DE STRINGS ===")

nombre = "Ana"
edad = 25
altura = 1.75

# Método 1: Operador %
formato1 = "Nombre: %s, Edad: %d, Altura: %.2f" % (nombre, edad, altura)
print(f"Usando %: {formato1}")

# Método 2: Método format()
formato2 = "Nombre: {}, Edad: {}, Altura: {:.2f}".format(nombre, edad, altura)
print(f"Usando format(): {formato2}")

# Con índices
formato3 = "Nombre: {0}, Edad: {1}, Altura: {2:.2f}".format(nombre, edad, altura)
print(f"format() con índices: {formato3}")

# Con nombres
formato4 = "Nombre: {n}, Edad: {e}, Altura: {a:.2f}".format(n=nombre, e=edad, a=altura)
print(f"format() con nombres: {formato4}")

# Método 3: f-strings (Python 3.6+)
formato5 = f"Nombre: {nombre}, Edad: {edad}, Altura: {altura:.2f}"
print(f"Usando f-string: {formato5}")

# Alineación y relleno en format y f-strings
print(f"Alineación: |{nombre:>10}|{nombre:<10}|{nombre:^10}|")  # derecha, izquierda, centro
print(f"Con relleno: |{nombre:_>10}|{nombre:_<10}|{nombre:_^10}|")  # con carácter de relleno
print()

# === 7. Inmutabilidad de Strings ===
print("=== INMUTABILIDAD DE STRINGS ===")

s = "Python"
print(f"String original: {s}")

# Los strings son inmutables, no se pueden modificar
# s[0] = "J"  # Esto daría un TypeError

# Para "modificar" un string, hay que crear uno nuevo
s_nuevo = "J" + s[1:]
print(f"Nuevo string: {s_nuevo}")

# El string original permanece sin cambios
print(f"String original (sin cambios): {s}")
print()

# === 8. Escape de Caracteres ===
print("=== ESCAPE DE CARACTERES ===")

# \n - Nueva línea
print("Primera línea\nSegunda línea")

# \t - Tabulación
print("Columna1\tColumna2\tColumna3")

# \\ - Barra invertida
print("Ruta de archivo: C:\\Users\\Usuario\\Documents")

# \' y \" - Comillas
print("Él dijo: \"Hola\" y se fue")
print('Ella respondió: \'Adiós\' y cerró la puerta')

# \r - Retorno de carro
print("Texto antes\rTexto después")  # En la mayoría de terminales, \r vuelve al inicio de la línea

# \b - Retroceso
print("Python\b es genial")  # Borra el carácter anterior (la 'n')

# Strings raw (crudos)
print(r"C:\Users\nombre\nuevo")  # La r antes de las comillas evita que se interpreten los escapes
print()

# === 9. Codificación y Decodificación ===
print("=== CODIFICACIÓN Y DECODIFICACIÓN ===")

# Codificar string a bytes
texto = "Hola, mundo!"
bytes_utf8 = texto.encode('utf-8')
print(f"String original: {texto}")
print(f"Codificado (UTF-8): {bytes_utf8}")

# Decodificar bytes a string
texto_decodificado = bytes_utf8.decode('utf-8')
print(f"Decodificado: {texto_decodificado}")

# Otros encodings
bytes_latin1 = texto.encode('latin-1')
print(f"Codificado (Latin-1): {bytes_latin1}")
print(f"Decodificado: {bytes_latin1.decode('latin-1')}")
print()

# === 10. Operaciones Avanzadas ===
print("=== OPERACIONES AVANZADAS ===")

# Traducción de caracteres
tabla_traduccion = str.maketrans("aeiou", "12345")
texto = "murcielago"
traducido = texto.translate(tabla_traduccion)
print(f"Original: {texto}")
print(f"Traducido: {traducido}")

# Partición
texto = "nombre:apellido:edad"
print(f"partition(':') -> {texto.partition(':')}")  # Divide en 3 partes por la primera ocurrencia
print(f"rpartition(':') -> {texto.rpartition(':')}")  # Divide en 3 partes por la última ocurrencia

# Justificación con formato
numero = 42
print(f"Número justificado: |{numero:5d}|")  # Justificado a 5 espacios
print(f"Número con ceros: |{numero:05d}|")  # Relleno con ceros

# Formato de números
pi = 3.14159265359
print(f"Pi con 2 decimales: {pi:.2f}")
print(f"Pi en notación científica: {pi:e}")
print(f"Pi en formato porcentaje: {pi:.2%}")  # Multiplica por 100 y añade %

# Formato con separador de miles
numero_grande = 1234567890
print(f"Con separador de miles: {numero_grande:,}")
print()

# === 11. Comparación de Strings ===
print("=== COMPARACIÓN DE STRINGS ===")

a = "abc"
b = "abd"
c = "ABC"
d = "abc"

print(f"a = '{a}', b = '{b}', c = '{c}', d = '{d}'")
print(f"a == d: {a == d}")  # Igualdad (mismo contenido)
print(f"a == c: {a == c}")  # Sensible a mayúsculas/minúsculas
print(f"a.lower() == c.lower(): {a.lower() == c.lower()}")  # Insensible a mayúsculas/minúsculas
print(f"a != b: {a != b}")  # Desigualdad
print(f"a < b: {a < b}")  # Comparación lexicográfica
print(f"a > c: {a > c}")  # En ASCII/Unicode, las minúsculas tienen valores mayores
print()

# === 12. Strings y Bytes ===
print("=== STRINGS Y BYTES ===")

# String normal (Unicode)
s = "Hola, mundo! 😊"
print(f"String: {s}")
print(f"Tipo: {type(s)}")

# Convertir a bytes
b = s.encode('utf-8')
print(f"Bytes: {b}")
print(f"Tipo: {type(b)}")

# Convertir bytes a string
s2 = b.decode('utf-8')
print(f"String de nuevo: {s2}")

# Bytes literales
b2 = b'Hola'  # Solo puede contener ASCII
print(f"Bytes literal: {b2}")

# Bytes y caracteres no ASCII
# b3 = b'😊'  # Esto daría error, los bytes literales solo aceptan ASCII
b3 = '😊'.encode('utf-8')
print(f"Emoji en bytes: {b3}")
print()

# === 13. Strings y Memoria ===
print("=== STRINGS Y MEMORIA ===")

# Interning (optimización interna de Python)
a = "hola"
b = "hola"
print(f"a = '{a}', b = '{b}'")
print(f"a is b: {a is b}")  # True, Python reutiliza strings idénticos

# Pero no siempre funciona
c = "hola mundo"
d = "hola mundo"
print(f"c = '{c}', d = '{d}'")
print(f"c is d: {c is d}")  # Puede ser True o False dependiendo de la implementación

# Longitud y memoria
print(f"Longitud de '{a}': {len(a)}")
print(f"Tamaño en memoria: {a.__sizeof__()} bytes")
print()

# === 14. Ejemplos Prácticos ===
print("=== EJEMPLOS PRÁCTICOS ===")

# Ejemplo 1: Validar una dirección de correo electrónico (simplificado)
def validar_email(email):
    return '@' in email and '.' in email.split('@')[1]

email1 = "usuario@dominio.com"
email2 = "usuariodominio.com"
print(f"¿'{email1}' es un email válido? {validar_email(email1)}")
print(f"¿'{email2}' es un email válido? {validar_email(email2)}")

# Ejemplo 2: Extraer nombre de usuario de un email
def extraer_usuario(email):
    return email.split('@')[0] if '@' in email else None

print(f"Usuario de '{email1}': {extraer_usuario(email1)}")

# Ejemplo 3: Contar palabras en un texto
def contar_palabras(texto):
    return len(texto.split())

texto = "Python es un lenguaje de programación interpretado"
print(f"Palabras en '{texto}': {contar_palabras(texto)}")

# Ejemplo 4: Censurar palabras
def censurar(texto, palabra):
    return texto.replace(palabra, '*' * len(palabra))

texto = "Python es genial y Python es fácil"
print(f"Texto censurado: {censurar(texto, 'Python')}")

# Ejemplo 5: Formatear un número de teléfono
def formatear_telefono(numero):
    if len(numero) != 10:
        return "Número inválido"
    return f"({numero[:3]}) {numero[3:6]}-{numero[6:]}"

telefono = "1234567890"
print(f"Teléfono formateado: {formatear_telefono(telefono)}")