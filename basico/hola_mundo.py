#hola como estas
print('hola mundo')

#tipos de datos
print(type('hola mundo'))
print(type(100))
print(type(100.5))
print(type(True))
print(type(False))
print(type([1,2,3]))
print(type((1,2,3)))
print(type({'nombre':'juan','apellido':'perez'}))

#variables
nombre = 'juan'
print(nombre)
print(type(nombre))

mi_texto = 'Mi numero favorito es: '
mi_numero = 7
print(mi_texto + str(mi_numero))
print(mi_texto, mi_numero)
print(mi_texto, 7)

#operadores aritmeticos
numero1 = 10
numero2 = 5
suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2
division_entera = numero1 // numero2
modulo = numero1 % numero2
potencia = numero1 ** numero2
print(suma)
print(resta)
print(multiplicacion)
print(division)
print(division_entera)
print(modulo)
print(potencia)

#operadores de comparacion
numero1 = 10
numero2 = 5
print(numero1 == numero2)
print(numero1 != numero2)
print(numero1 > numero2)
print(numero1 < numero2)
print(numero1 >= numero2)
print(numero1 <= numero2)

#operadores logicos
numero1 = 10
numero2 = 5
numero3 = 7
print(numero1 > numero2 and numero1 < numero3)
print(numero1 > numero2 or numero1 < numero3)
print(not(numero1 > numero2))

#strings
mi_primer_string = "Este es un string con comillas dobles"
mi_segundo_string = 'Este es un string con comillas simples'
mi_string_multilinea = """Este es un string
multilinea"""
print(mi_primer_string)
print(mi_segundo_string)
print(mi_string_multilinea)
print(f'Este es un string con f-string {mi_primer_string}')
mi_string = 'hola'
a,b,c,d = mi_string
print(a)
print(b)
print(c)
print(d)

print(mi_primer_string.upper())
print(mi_primer_string.lower())
print(mi_primer_string.capitalize())
print(mi_primer_string.title())
print(mi_primer_string.replace('string','texto'))
print(mi_primer_string.split(' ')) 
print(' '.join(['Este','es','un','string','unido','por','espacios']))
print(''.join(['Este','es','un','string','unido','sin','espacios']))
print(mi_primer_string.find('string'))
print(mi_primer_string.find('texto'))
print(mi_primer_string.count('string'))
print(mi_primer_string.isalnum()) 
print(mi_primer_string.isalpha())
print(mi_primer_string.isdigit())
print(mi_primer_string.islower())
print(mi_primer_string.isupper())
print(mi_primer_string.istitle())
print(mi_primer_string.isnumeric())
print(mi_primer_string.isdecimal())
print(mi_primer_string.isprintable())
print(mi_primer_string.isspace())
print(mi_primer_string.isidentifier())
print(mi_primer_string.isascii())
print(mi_primer_string.startswith('Este'))
print(mi_primer_string.endswith('doble'))
print('string' in mi_primer_string)
print('texto' not in mi_primer_string)
print(len(mi_primer_string))
