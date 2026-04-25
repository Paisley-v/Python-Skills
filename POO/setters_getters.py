class persona:   
    def __init__(self,nombre,edad):
        self._nombre = nombre
        self._edad = edad
        
    def get_nombre(self):   #getter
        return self._nombre
    
    def set_nombre(self,new_nombre):  #setter, setea nuevo nombre
        self._nombre = new_nombre
        
camila = persona("camila",21)

nombre = camila.get_nombre()
print(nombre)

camila.set_nombre("Cami")

nombre = camila.get_nombre()
print(nombre)


#__ muy privado
#_ privadoclass persona:
 