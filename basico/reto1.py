lista = [5,7,2,7,9,4,8]

maximo = max(lista)
print(f'El valor máximo de la lista es: {maximo}')

minimo = min(lista)
print(f'El valor mínimo de la lista es: {minimo}')

def segundo_mas_grande(lista):
    lista.sort()
    return lista[-2]

print(f'El segundo valor más grande de la lista es: {segundo_mas_grande(lista)}')