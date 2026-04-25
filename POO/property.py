class persona:   
    def __init__(self,nombre,edad):
        self.__nombre = nombre
        self.__edad = edad
        
    @property
    def nombre(self):   #getter se convierte a propiedad con property
        return self.__nombre
    
    @nombre.setter  #setiando con nuevo nombre
    def nombre(self, new_nombre):
        self.__nombre = new_nombre

    @nombre.deleter  #eliminador de propiedades
    def nombre(self):
        del self.__nombre
    
        
camila = persona("camila",21)

#del camila.nombre

nombre = camila.nombre
print(nombre)


camila.nombre = "cami"
nombre = camila.nombre
print(nombre)



#__ muy privado
#_ privadoclass persona: