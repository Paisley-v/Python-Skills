def decorador(funcion):
    def funcion_modificada():
        print("Antes de llamar a la función")
        funcion()
        #print("Despues de llamar a la función")
    return funcion_modificada

# def saludo():
#     print("Hola")
    
# saludo_modificado = decorador(saludo)
# saludo_modificado()

#ctrl k c

@decorador  #ejecuta una funcion y agrega otra funcion
def saludo():
    print("Hola como andas")
    
    
saludo()