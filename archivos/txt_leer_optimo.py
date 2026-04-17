#USANDO witch open PARA ABRIR UN ARCHIVO

with open ("archivos\\texto.txt", encoding="UTF-8") as archivo:
    
    print(archivo.read())
    
#No es necesario cerrarlo al usar with open
    