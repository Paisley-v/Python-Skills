#falto el profesor y los alumnos arman la clase


#función para obtener al asistente y al profesor según la edad
def obtener_comp(cantidad):
    
    #creando lista con los compañeros
    compañeros = []
    
    #ejecutando for para pedir info de cada compañero
    for i in range(cantidad):
        nombre = input ("nombre: ")
        edad = int(input("ingrese edad"))
        compañero =  (nombre,edad)
        
        #agregando la información a la lista
        compañeros.append(compañero)   
        
    #ordenando de menor a mayor según edad
    compañeros.sort(key= lambda x:x[1])
    
    #compañeros[x] devuelve una tupla con (nombre,edad) y despues accedemos al nombre
    #para definir al asistente y al profesor
    asistente = compañeros[0][0]
    profesor = compañeros[-1][0]
    
    #retorna una tupla
    return asistente,profesor

#depempaquetado
asistente,profesor = obtener_comp(5)

print(f"profesor: {profesor} , asistente: {asistente}")