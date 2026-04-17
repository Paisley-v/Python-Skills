diccionario = {
    "nombre": "juan",
    "apellido": "valencia",
    "aura": 1000000
}

#Devuelve las claves (tambien sirve para iterar), filas o columnas labels dict_item
claves = diccionario.keys()
print(claves)

#Obtener un elemento, si no encuentra nada el programa continua
gets = diccionario.get("aura")
print(gets)

#Eliminando un dato del diccionario
diccionario.pop("aura")
print(diccionario)

#Obteniendo un elemento dict_items iterable
diccionario_iterable = diccionario.items()
print(diccionario_iterable)


#Elimina todos los elementos del diccionario
diccionario.clear()
print(diccionario)