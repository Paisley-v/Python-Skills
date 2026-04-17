frutas = ["banana", "manzana", "piña", "pera", "ciruela", "granada", "durazno", "naranja"]


#evitando que se coma una manzana con continue
for fruta in frutas:
    if fruta == "granada":
        continue                                   #se salta un elemento de la lista
    print(f"Me voy a comer {fruta}")
    
#Detener un bucle con break (else no se ejecuta tampoco)
for fruta in frutas:
    print(f"Me voy a comer {fruta}")
    if fruta == "pera":
        break                                       #detiene un bucle incluso tampoco si hay un else


print("bucle terminado")

#Iterar = recorrer un conjunto

#recorrer una cadena de texto
cadena = "hola jhon"

for letra in cadena:
    print({letra})
    
#for en una sola cadena agregando elementos iterados
numeros = [2,3,4,5,6]
numeros_dup = list()

numeros_dup = [x*2 for x in numeros]
print()
print(numeros_dup)