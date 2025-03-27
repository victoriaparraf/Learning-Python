#CLASES Y OBJETOS

#Clase
class Persona:
    #Atributos
    nombre = "Juan"
    edad = 18
    sexo = "M"
    altura = 1.70
    peso = 70
    
    def __init__(self, nombre, edad, sexo, altura, peso):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.altura = altura
        self.peso = peso

    #Metodos
    def hablar(self, mensaje):
        return mensaje

    def caminar(self, pasos):
        return pasos
    
class Coche:
    #Atributos
    marca = "Toyota"
    modelo = "Corolla"
    color = "Rojo"
    cilindraje = 1.8
    precio = 20000
    
    def __init__(self, marca, modelo, color, cilindraje, precio):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.cilindraje = cilindraje
        self.precio = precio

    #Metodos
    def acelerar(self, velocidad):
        return velocidad

    def frenar(self, velocidad):
        return velocidad    
    
#Objeto
persona = Persona("Pedro", 25, "M", 1.75, 75)
print(f"Nombre: {persona.nombre} \nEdad: {persona.edad} \nSexo: {persona.sexo} \nAltura: {persona.altura} \nPeso: {persona.peso}")
print(persona.hablar("Hola, estoy hablando"))
print(persona.caminar(10))

coche = Coche("Nissan", "Sentra", "Blanco", 1.6, 15000)
print(f"Marca: {coche.marca} \nModelo: {coche.modelo} \nColor: {coche.color} \nCilindraje: {coche.cilindraje} \nPrecio: {coche.precio}")
print(coche.acelerar(100))
print(coche.frenar(50))
