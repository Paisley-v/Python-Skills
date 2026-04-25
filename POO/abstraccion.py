class auto():
    def __init__(self):
        self._estado = "apagado"
        
    def encender(self):
        self._estado = "encendido"
    print("El auto esta encendido")
    
    def conducir(self):
        if self._estado == "apagado":  #abstraccion
            self.encender()
        print("Conduciendo auto")
        
mi_auto = auto()
mi_auto.conducir()


#hacer un sistema con una interfaz sencilla para el usuario
#el usuario al conducir solo tiene que ver que conducir
#no tiene que ver otros mecanismos
#abstraccion es un concepto