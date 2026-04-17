#LISTA
lista = ["Juan Valencia", "Soy Valencia", True, 1.65]
print(lista[0])

# Esto es valido
# lista[3] = "maquinola"

# En las listas el indice 0 es la posicón 1, el  indice 1 es la posición 2..

#TUPLAS

tupla = ("Juan Valencia", "Soy Valencia", True, 1.65)
print(tupla[1])

#Esto no es valido
# tupla[3]= "Maquinola"

# La diferencia es que la tupla no se modifica
# una vez compilado guarda los datos en la memoria y no cambian

#CONJUNTO (set)
conjunto = {"Juan Valencia", "Soy Valencia", True, 1.65}
print(conjunto)

# Los conjuntos no tienen un orden
# No tienen indice para llamar
# No permite repetir datos

#DICCIONARIO (dic)
diccionario = {
    "nombre" : "Juan Valencia",
    "lenguaje" : "Python",
    "esta:programando": True,
    "altura" : 1.65,
    "dato_duplicado" : "Soy valencia"
}

print(diccionario["altura"] + 7)

# Es similar a una lista, e vez de tener un indice, tiene una key que se puede definir