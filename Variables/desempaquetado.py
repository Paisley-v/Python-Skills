#Creando una tupla

datos = ("jhon", "titor", 10000000)
lista = ("jhon", "titor", 10000000)

#Desempaquetado (funciona en listas y tuplas)
nombre,apellido,num= datos
nombre1, apellido1,num1 = lista

print(nombre1)
print(apellido)


#Forma de crear tupla con tuple

tupla =  tuple([lista])
print(tupla)

#Creando una tupla sin parentesis 
tupla1 = "dato", "dato2"
print(tupla1)

