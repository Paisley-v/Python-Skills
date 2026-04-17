cadena1 = "Hola soy Juan"
cadena2 = "Bienvenido,maquina"

print(dir(cadena1))  #muestra las cosas que hacer con los datos

#Convierte a mayuscula
mayuscula = cadena1.upper()
print(mayuscula)

#Convierte a miniscula
miniscula = cadena1.lower()

#Primera letra en Mayuscula, las demás en miniscula
primer_letra_mayusc = cadena1.capitalize()

#Buscamos en una cadena en otra cadena y dice la posición, devuelve -1 cuando no encuentra un valor
busqueda_find = cadena1.find("s")
print(busqueda_find)

#Buscamos una cadena en otra cadena, si no hay coincidencias lanza una "excepcion"
busqueda_index = cadena1.index("s")

#si es numerico devuelve true, sino devolvemos false
es_numerico = cadena1.isnumeric()

#si es alfanumerico devuelve true, sino devolvemos false (Si no tiene carcateres especiales)
es_alfanumerico = cadena1.isalpha()

#Contamos una cadena dentro de otra cadena y devuelve la cantidad de veces que coindicida
contar_coincidencias = cadena1.count("a")
print(contar_coincidencias)

#Devuelve la cantidad de caracteres que tiene una cadena
contar_carcateres = len(cadena1)

#Verificamos si una cadena empieza con otra cadena dada, si es así devuelve True
empieza_con = cadena1.startswith("H")

#Verificamos si una cadena empieza con otra cadena dada, si es así devuelve True
empieza_con = cadena1.endswith("N")

#Reemplaza un pedazo de la cadena dada por otra dada
#Reemplza la por lu
cadena_nueva = cadena1.replace("la", "lu")
print(cadena_nueva)
#Una función interesante es reemplazar las , 
cadena_nueva1 = cadena2.replace(",", " ")
cadena_nueva2 = cadena_nueva1.capitalize()
print(cadena_nueva2)

#Separar cadenas por la cadena que le pasemos conviertendolas en matriz

cadena_nueva3 = cadena2.split("i")

print(cadena_nueva3)
print(cadena_nueva3[0])


