# Leer archivo

archivo = open("archivos\\texto.txt", encoding = "UTF-8")

n = archivo.read()

print(n)

archivo.close()


#leer linea x lineas

archivo = open("archivos\\texto.txt", encoding = "UTF-8")

lineas = archivo.readlines()

print(lineas)

archivo.close()

#leer una sola linea
archivo = open("archivos\\texto.txt", encoding = "UTF-8")

linea = archivo.readline(100)  #cantidad de caracteres por linea () para completo
print(linea)

archivo.close()