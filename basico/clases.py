#clases
class persona:
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
    def mostrar(self):
        print("Nombre: ",self.nombre)
        print("Edad: ",self.edad)
        
persona1 = persona("Juan",25)
persona1.mostrar()

#excepciones
try:
    print(10/0)
except ZeroDivisionError:
    print("No se puede dividir por cero")
else:
    print("No hubo error")
finally:
    print("Fin del programa")