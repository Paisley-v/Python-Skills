#Iterar repite el bloque continuamente hasta que finaliza (iterar)

animales = ["gato", "perro", "cocodrilo", "loro"]

#recorre la lista animales y crea una variable
for animal in animales:
    print(f"Ahora la variable animal es : {animal}")


numeros = [12,4,77,30]

#recorriendo y multiplicando la lista numeros
for numero in numeros:
    resultado = numero * 10
    print(f"resultado: {resultado}")
    
#recorriendo dos listas del mismo tamaño al mismo tiempo

for numero,animal in zip(animales, numeros):
    print(f"recoriendo lista 1: {animal}")
    print(f"recorriendo lista 2: {numero}")
    
#recorriendo numeros del 5 al 10
for num in range(5,10):
    print(num)
    
#recorriendo una lista por el indice

for numero in enumerate(numeros):
    indice = numero[0]
    valor = numero[1]
    print(f"{indice}, {valor}")
    
    
#usando for/else

for numero in numeros:
    print(f"ejecutando bucle {numero}")
else:
    print("el bucle termino")
    
#IGUAL PARA TUPLAS Y LISTAS