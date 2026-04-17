#creando una lista con list
lista = list(["Hola", "Juan", 21, 22, 25, True])

#Devuelve la cantidad de elementos de la lista
resultado = len(lista)
print(lista)

#Agregando elementos con append
lista.append("KKKKK")
print(lista)

#Agregando un elemento a la lista con un indice en especifico
lista.insert(2, "Pigeon")
print(lista)

#Agregando varios elementos a la lista con una lista
lista.extend([False, 2030])
print(lista)

#Eliminando un elemento de la lista por su indice
lista.pop(0)
lista.pop(-1) #elimina el ultimo de la lista truco (-2)
print(lista)

#Removiendo un elemento de la lista pro su valor
lista.remove(False)
print(lista)

# Ordena la lista
lista1 = list([2, 21, 22, 25, True])
lista1.sort()
print(lista1)
lista1.sort(reverse=True)  #Ordena del mayor al menor

#Invirtiendo los elementos en una lista
lista.reverse()
print(lista)

#Eliminando todos los elementos de la lista
lista.clear()
print(lista)

#Al usar el directorio
# __X__ no se puede hacer,   x se puede hacer


