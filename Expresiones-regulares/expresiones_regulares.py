import re

texto = '''Hola maestro, como estas. 
Esta es la segunda linea
Esta es la tercera linea'''


# Haiendo una busqueda simple
r1 = re.findall("Esta", texto)

#\d --> Busca digitos numericos del 0 al 9
r2 = re.findall(r"\d",texto)

#\D -> busc todo menos digitos numericos del 0-9
r3 = re.findall(r"\D",texto)

#\w --> Busca caracteres alfanumericos a-z A-Z 0-9
r4 = re.findall(r"\w",texto)

#\W --> Busca todo menos caracteres alfanumericos a-z A-Z 0-9
r5 = re.findall(r"\W",texto)

#\s --> Busca espacios en blanco
r6 = re.findall(r"\s",texto)

#\S --> Busca todo menos espacios en blanco
r7 = re.findall(r"\S",texto)

#\S --> Busca todo menos saltos en linea
r8 = re.findall(r".",texto)

#\S --> Busca saltos en linea
r9 = re.findall(r"\n",texto)

print(r1, r2, r3, r4, r5, r6, r7, r8, r9)

#\Cancelar caracteres especiales, buscando puntos
r10= re.findall(r"\.", texto)

#Armando una cadena que busque un nuemro, seguido de un punto y un espacio
r11= re.findall(r"\d\.\s", texto)

#Busca el comienzo de una linea, y busca hola al principio
r12= re.findall(r"^Hola", texto)

#Activa la multilinea
r13= re.findall(r"^Hola", texto, flags=re.M)#

#Busca el final de una linea
r14= re.findall(r"$maestro", texto, flags=re.M)

#Busca n cantidad de veces el valor de la izquierda (3 numeros juntos esta vez)
r15= re.findall(r"\d{3}", texto)

#al menos n, como maximo m
r16= re.findall(r"\d{1,4}", texto)

# busca una cosa o la otra

r17= re.findall(r"\d{1,4}|Maestro", texto)

print(r10, r11, r12, r13, r14, r15, r16, r17)


