# Herencia
from clases_objetos import Persona

class profesor(Persona):
    # Atributos privados
    def __init__(self, nombre, edad, sexo, altura, peso, salario, materia, experiencia):
        super().__init__(nombre, edad, sexo, altura, peso)
        self.__salario = salario
        self.__materia = materia
        self.__experiencia = experiencia
    
    # Métodos
    def enseñar(self, materia):
        return materia

    def calificar(self, nota):
        return nota

    # Métodos para acceder a los atributos privados
    def get_salario(self):
        return self.__salario

    def get_materia(self):
        return self.__materia

    def get_experiencia(self):
        return self.__experiencia

profesor = profesor('Pedro', 25, 'M', 1.75, 75, 2000, 'Programacion', 5)
print(f"Nombre: {profesor.nombre} \nEdad: {profesor.edad} \nSexo: {profesor.sexo} \nAltura: {profesor.altura} \nPeso: {profesor.peso}")
print(f"Salario: {profesor.get_salario()} \nMateria: {profesor.get_materia()} \nExperiencia: {profesor.get_experiencia()}")
print(profesor.enseñar("Programacion"))
print(profesor.calificar(10))