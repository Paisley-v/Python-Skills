#Creando una función que suma numeros

def sumar_dos(): 
    #Iniciando un bucle
    while True:
        #Pidiendo numeros
        a = input("numero 1: ")
        b = input("numero 2: ")
        #Intendanto converitrlos a enteros y sumas
        try:
           resultado = int(a) + int(b)
        #Si lanzo una excepcion, pedirle que reingrese los datos
        except ValueError as e:
            print(f"ERROR{e}")
        #Si todo salio bien terminamos el bucle

        else: 
            break
        finally:
            print("Esto se ejecuta siempre")
            
    #Mostrando el resultado
    return resultado
    
print(sumar_dos())