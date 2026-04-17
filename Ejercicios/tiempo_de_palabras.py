#Pedirle al usuario que diga cualquier texto real 1 segundo = 2 palabras
#Calcular cuanto tardaria en decir esa frase
#cuantas palabras dijo

texto = input("Ingresa una frase: ")
separar = texto.split(" ")
cantidad = len(separar)
tiempo= cantidad/2
print("Dijiste", cantidad, "palabras y tardaste", tiempo,  "segundos")


#Si se tarda mas de 1 minuto enviar un print
if tiempo > 5:
    print ("Te tardaste demasiado")

#Si alguien habla un 30% más rapido cuanto tardaria el en decirlo

rapido = tiempo / (0.7*2) 
print("otro lo hizo en", rapido, "segundos")