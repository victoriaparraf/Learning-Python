# 1. Clase simple
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")

persona1 = Persona("Carlos", 30)
persona1.saludar()

# 2. Atributos de clase y de instancia
class Coche:
    ruedas = 4  # Atributo de clase

    def __init__(self, marca, modelo):
        self.marca = marca  # Atributo de instancia
        self.modelo = modelo

coche1 = Coche("Toyota", "Corolla")
print(f"{coche1.marca} {coche1.modelo} tiene {Coche.ruedas} ruedas.")

# 3. Herencia
class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)
        self.carrera = carrera

    def estudiar(self):
        print(f"{self.nombre} está estudiando {self.carrera}.")

estudiante1 = Estudiante("Laura", 22, "Ingeniería")
estudiante1.saludar()
estudiante1.estudiar()

# 4. Métodos especiales (__str__)
class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def __str__(self):
        return f"'{self.titulo}' de {self.autor}"

libro1 = Libro("1984", "George Orwell")
print(libro1)

# 5. Encapsulamiento
class CuentaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo  # Atributo privado

    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad

    def obtener_saldo(self):
        return self.__saldo

cuenta = CuentaBancaria(1000)
cuenta.depositar(500)
print("Saldo actual:", cuenta.obtener_saldo())

# 6. Clase con método estático
class Utilidades:
    @staticmethod
    def es_par(numero):
        return numero % 2 == 0

print("¿4 es par?", Utilidades.es_par(4))

# 7. Clase con método de clase
class Animal:
    especie = "Desconocida"

    @classmethod
    def cambiar_especie(cls, nueva_especie):
        cls.especie = nueva_especie

Animal.cambiar_especie("Mamífero")
print("Nueva especie:", Animal.especie)

# 8. Getters y Setters
class Robot:
    def __init(self, name= None):
        self.name = name
        
    def decir_hola(self):
        if self.name:
            print("Hola, yo soy" + self.name)
        else:
            print("Hola, soy un robot sin nombre")
            
    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name

# 9. Propiedades
class P:
    def __init__(self, x):
        self.x = x
        
    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, x):
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x