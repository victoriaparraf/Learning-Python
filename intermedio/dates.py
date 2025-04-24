# FECHAS EN PYTHON (Dates) - NIVEL INTERMEDIO

# 1. Importar datetime
from datetime import datetime
from datetime import time 
from datetime import date

# 2. Fecha y hora actuales
fecha_ahora = datetime.now()
print("Fecha y hora actuales:", fecha_ahora)

# 3. Solo fecha o solo hora
print("Solo la fecha:", fecha_ahora.date())
print("Solo la hora:", fecha_ahora.time())

# 4. Crear objetos datetime personalizados
cumple = datetime.datetime(2000, 5, 15, 10, 30)
print("Cumpleaños:", cumple)

# 5. Formatear fechas (strftime)
fecha = datetime.now()
print("Formato personalizado:", fecha.strftime('%d/%m/%Y %H:%M:%S'))
print(fecha.tzinfo)

# 6. Convertir string a fecha (strptime)
fecha_str = "21-04-2025 15:00"
fecha_convertida = datetime.datetime.strptime(fecha_str, "%d-%m-%Y %H:%M")
print("Fecha convertida desde string:", fecha_convertida)

# 7. Operaciones con fechas (timedelta)
mañana = fecha_ahora + datetime.timedelta(days=1)
ayer = fecha_ahora - datetime.timedelta(days=1)
print("Mañana será:", mañana)
print("Ayer fue:", ayer)

# 8. Diferencia entre fechas
fecha1 = datetime.datetime(2025, 4, 25)
fecha2 = datetime.datetime(2025, 4, 21)
diferencia = fecha1 - fecha2
print("Días de diferencia:", diferencia.days)

# 9. Comparación de fechas
if fecha1 > fecha2:
    print("fecha1 es posterior a fecha2")

# 10. Usar date (solo fechas sin hora)
hoy = datetime.date.today()
print("Fecha de hoy (sin hora):", hoy)

# 11. Crear fechas con date
fecha = datetime(2020, 12, 25)
print(fecha)

# 12. Crear una fecha con hora
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

# 13. Obtener día de la semana
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
print("Hoy es:", dias_semana[hoy.weekday()])  # weekday: lunes=0, domingo=6

# 14. Medir el tiempo que tarda un bloque de código
inicio = time.time()
for _ in range(1000000):
    pass
fin = time.time()
print("Tiempo de ejecución:", fin - inicio, "segundos")

# 14. Fecha y hora en UTC
utc_ahora = datetime.datetime.utcnow()
print("Fecha y hora UTC:", utc_ahora)

# 15. Crear zona horaria con módulo zoneinfo (Python 3.9+)
try:
    from zoneinfo import ZoneInfo

    ahora_bogota = datetime.datetime.now(ZoneInfo("America/Bogota"))
    ahora_tokyo = datetime.datetime.now(ZoneInfo("Asia/Tokyo"))

    print("Hora en Bogotá:", ahora_bogota)
    print("Hora en Tokio:", ahora_tokyo)
except ImportError:
    print("ZoneInfo no está disponible en esta versión de Python.")

# 16. Crear una hora
hora = time(10, 30, 0)
print(hora)
print(hora.hour)
print(hora.minute)
print(hora.second)
print(hora.microsecond)