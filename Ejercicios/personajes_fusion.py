class Personaje:
    def __init__(self, nombre, fuerza, velocidad):
        self.nombre = nombre 
        self.fuerza = fuerza
        self.velocidad = velocidad
        
    def __repr__(self):
        return f"{self.nombre}, fuerza: {self.fuerza}, velocidad: {self.velocidad}"
    
    def __add__(self,other):
        nuevo_nombre = self.nombre + "-" + other.nombre
        nueva_fuerza = round(((self.fuerza + other.fuerza)/2)**1.3)
        nueva_velocidad = round(((self.velocidad + other.velocidad)/2)**1.3)
        return Personaje(nuevo_nombre, nueva_fuerza, nueva_velocidad)
    
goku = Personaje("Goku", 100, 100)
vegetta = Personaje ("Vegetta", 99, 99)
jiren = Personaje("Jiren", 130, 140)

print(goku, vegetta, jiren)

gogeta = goku + vegetta
jireta = gogeta + jiren

print(gogeta)
print(jireta)

