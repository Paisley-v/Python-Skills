#Crear una clase estudiante que tenga atributos nombre edad y grado
#metodos estudiar , el estudiante nombre esta estudiando
#crear un objeto estudiante y usar el metodo estudiar
#se debe interactuar con el usuario y este debe brindar los atributos
#al escribir estudiar utilizar el metodo estudiar

class estudiante:
    def __init__(self,nombre,edad,grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
        
    def estudiar(self):
        print("Estudiando ..")
        
nombre = input("Ingrese nombre: ")
edad = input("Ingrese edad: ")
grado = input("Ingrese grado: ")
        
estudiante = estudiante(nombre, edad, grado)

print(f"Nombre {nombre}, edad {edad}, grado {grado}")

while True:
    estudiar = input()
    if (estudiar.lower() == "estudiar"):
        estudiante.estudiar()