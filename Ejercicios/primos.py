#creando una funcipn que nos devuelva los numeros primos 
#entre 0 y el argumento que pasamos


#creando una funcion que verifique si un numero es primo
def es_primo(num):
    #verificamos que el numero pasado no pueda dividirse
    #por ningun numero entre 2 y ese mismo numero -1
    for i in range(2, num-1):
        #si es divisible por alguno retornamos false y termina en bucle
        if num%i==0: return False    
    #si termina el bucle, significa que no fue divisible neotnces es primo
    return True
               
               
#creando funciones que retorneo una lista con todos los primos
def primos_hast(num):
    primos = []
    for i in range(num):
        resultado = es_primo(i) #verificamos si el valor es primo
        if resultado == True: primos.append(i) # si es, se agrega a la lista
    return primos  #devolvemos la lista
        
               
#desempaquetado        
resultado = es_primo(98)
resultado2 = primos_hast(98)
print(resultado)
print()
print(resultado2)