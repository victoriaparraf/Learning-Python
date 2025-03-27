def convertir_a_milisegundos(tiempo):
    dias, horas, minutos, segundos = tiempo
    milisegundos = (
        (dias * 24 * 60 * 60 * 1000) +
        (horas * 60 * 60 * 1000) +
        (minutos * 60 * 1000) +
        (segundos * 1000)
    )
    return milisegundos

tiempo = [1, 1, 1, 1]
print(f'El tiempo en milisegundos es: {convertir_a_milisegundos(tiempo)}')