#Hereda todo lo de una clase padre a una clase hija 
#ej: galleta base (padre) --> galleta chocolate padre + detalle

class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
        
    def hablar(self):
        print("Hablando ..")
        
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
        
#HERENCIA SIMPLE
        
class Empleado(Persona):  #Herencia
    def __init__(self,nombre, edad, nacionalidad, trabajo, salario):
        super().__init__(nombre,edad,nacionalidad)
        self.trabajo = trabajo
        self.salario = salario
        
    def hablar(self):
        print("no ..")
    #pass  // para poder dejar vacio una clase
    
humano1 = Empleado("Camila", 23, "argentina", "programadora", "1000000")

print(humano1.nacionalidad)
humano1.hablar()

#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
    
#HERENCIA MULTIPLE
        
class Artista:
    def __init__(self, habilidad):
        self.habilidad = habilidad 
    
    def show_skill(self):
        return f"Mi habilidad es: {self.habilidad}"
        
class EmpleadoArtista (Persona, Artista):
    def __init__(self, nombre, edad, nacionalidad, habilidad, salario, empresa):
        Persona.__init__(self,nombre,edad,nacionalidad)
        Artista.__init__(self,habilidad)
        self.salario = salario
        self.empresa = empresa
        
    def presentarse(self):
        print (f"Hola soy {self.nombre}, {super().show_skill()}")
        
humano2 = EmpleadoArtista("Camila", 23, "argentina", "cantar","1000000", "Google")

humano2.presentarse()

#Para ver si es una herencia
herencia = issubclass(EmpleadoArtista,Persona)
instancia = isinstance(humano2, Artista)
print(herencia, instancia)
