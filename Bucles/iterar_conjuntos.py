#Iterar repite el bloque continuamente hasta que finaliza (iterar)

animales = {"gato", "perro", "cocodrilo", "loro"}

#recorre la conjunto animales y crea una variable
for animal in animales:
    print(f"Ahora la variable animal es : {animal}")


numeros = [12,4,77,30]

for numero in enumerate(numeros):
    indice = numero[0]
    valor = numero[1]
    print(f"{indice}, {valor}")
    
    
#usando for/else

for numero in numeros:
    print(f"ejecutando bucle {numero}")
else:
    print("el bucle termino")