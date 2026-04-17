numeros = [1,2,3,4,5,6,7,8,9,10]

#lambda es un funcion solo funciona con una condicion
#crear una funcion lamba que multiple por 2 

mult_num = lambda x: x*2
print (mult_num(5))


#Creando funcion comun que diga si es par o no par

#def es_par(num:)
#    if (num%2==1)
#        return True
#usando filter con una fuuncion comun
#pares= filter(es_par, numeros)    


#Creando lo mismo pero con lambda

numeros_pares = filter(lambda nume: nume%2 == 0, numeros)
print(list(numeros_pares))