#listas
mi_lista = ['1', 23, True, 'Hola Mundo', 5]
print(mi_lista)
print(type(mi_lista))

mi_lista.append(6)
print(mi_lista)

mi_lista.insert(1, 'Hola')
print(mi_lista)

mi_lista.remove(23)
print(mi_lista)

mi_lista.pop(2)
print(mi_lista)

mi_lista.pop()
print(mi_lista)

mi_lista.reverse()
print(mi_lista)

mi_lista.clear()
print(mi_lista)

#tuplas
mi_tupla = ('1', 23, True, 'Hola Mundo', 5)
print(mi_tupla)
print(type(mi_tupla))
print(mi_tupla.count('1'))
print(mi_tupla.index(23))

#diccionarios
mi_diccionario = {'clave1': 1, 'clave2': 2, 'clave3': 3}
print(mi_diccionario)
mi_diccionario['clave4'] = 4
print(mi_diccionario)
mi_diccionario.pop('clave1')
print(mi_diccionario)
print(mi_diccionario.keys())
print(mi_diccionario.values())
mi_diccionario.clear()
print(mi_diccionario)

#sets
mi_set = {1, 2, 3, 4, 5}
print(mi_set)
mi_set.add(6)
print(mi_set)
mi_set.remove(1)
print(mi_set)
mi_set.clear()
print(mi_set)