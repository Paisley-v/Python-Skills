diccionario = {
    "nombre": "Jhon",   # Key, datos
    "apellido": "Titor",
    "Edad"   : 200
}

#recorriendo disccionario con items() para obetener claves y datos
for datos in diccionario.items():
    key = datos[0] 
    value = datos[1]
    print(f"key:{key}, value{datos}")
    
