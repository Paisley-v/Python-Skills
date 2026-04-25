from abc import ABC, abstractmethod

class Persona(ABC):
    
    def __init__(self, nombre, edad, sexo, actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad
        
    @abstractmethod
    def trabajar(self):
        pass
    
    def presentarse(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años")


class Estudiante(Persona):
    
    def trabajar(self):
        print(f"Estudiando: {self.actividad}")


class Trabajador(Persona):
    
    def trabajar(self):
        print(f"Trabajando en: {self.actividad}")


camila = Estudiante("Camila", 21, "F", "Python")
camilo = Trabajador("Camilo", 21, "M", "Programación")

camila.presentarse()
camila.trabajar()

camilo.presentarse()
camilo.trabajar()