#Objeto y clase fijos
class Celular():
    marca = "samsung"
    modelo = "S23"
    camara = "48MP"
    
celular1 = Celular()  #instancia de clase
celular2 = Celular()
celular3 = Celular()
celular4 = Celular()

print(celular1.marca)


#Atributos y constructor

class Phone:
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.model = modelo
        self.camara = camara
        
    def llamar(self):                      #las funciones dentro de la clase se llaman metodos
        print(f"Estas llamando desde un: {self.model}")
        
    def colgar(self):
        print(f"Colgaste desde un: {self.model}")
        
phone1 = Phone("Samsung", "S23", "48MP")
phone2 = Phone("Apple", "Iphone X Pro", "96MP")

print(phone2.marca)

phone2.llamar()