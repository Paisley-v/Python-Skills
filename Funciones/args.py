#UTILIZANDO EL PARAMETRO ARGS * 

def suma(nombre, *numeros):
    return f"{nombre}, la suma de tus nuemros es: {sum(numeros)}"

resultado = suma("Jhon", 2,3,4,5,6,7,9)
print (resultado)


#se puede utilizar esta forma para definir el orden dentro de una funcion

# resultado = suma( numeros = [2,3], nombre = "juan")