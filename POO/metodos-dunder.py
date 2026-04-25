class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad=edad
        
    def __str__(self):  #mostrar como objeto en pantalla
        return f"Persona(nombre={self.nombre}, edad{self.edad})"
    
    def __repr__(self): #reconstruir objeto
        return f"Persona(nombre={self.nombre}, edad{self.edad})"
    
    def __add__(self, other):
        nuevo_valor = self.edad + other.edad
        return Persona(self.nombre + other.nombre, nuevo_valor)
    
persona = Persona("Camila", 21)
persona2 = Persona("Cami", 21)
repre = repr(persona)

print(persona)
print(repre)

nueva_persona = persona + persona2
print(nueva_persona.edad)