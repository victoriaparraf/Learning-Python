from datetime import datetime
from datetime import time 
from datetime import date

fecha = datetime.now()
print(fecha)

# Formato de fecha
fecha = datetime.now()
print(fecha.strftime('%d/%m/%Y %H:%M:%S'))
print(fecha.tzinfo)

# Crear una fecha
fecha = datetime(2020, 12, 25)
print(fecha)

# Crear una fecha con hora
fecha = datetime(2020, 12, 25, 10, 30, 0)
print(fecha)

print(fecha.year)
print(fecha.month)
print(fecha.day)
print(fecha.hour)
print(fecha.minute)
print(fecha.second)
print(fecha.microsecond)
print(fecha.tzinfo)

# Crear una hora
hora = time(10, 30, 0)
print(hora)
print(hora.hour)
print(hora.minute)
print(hora.second)
print(hora.microsecond)

fecha = date(2020, 12, 25)
print(fecha)
print(fecha.year)
print(fecha.month)
print(fecha.day)

fecha = date.today()
print(fecha)