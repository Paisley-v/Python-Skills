class Clase:
    def __init__(self):
        self.__atributo_privado = "valor"  #un valor que no se va a ver
        #__ define la privacidad muy privado
    def __hablar(self):  #metodo privado
        print("hola")
        
        
objeto = Clase()
#print(objeto.__atributo_privado)
#print(objeto.__hablar) #no se puede acceder de esta forma


