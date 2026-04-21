#Creando un contador de palabras en texto

texto = "La pizzeria de la pantera rosa tiene pizzas deliciosas"

palabras = texto.split()  #Devuelve una lista de palabras ["la", "pizzeria"..]

count = 0

for x in palabras:
    count = count + 1
    
    
print(f"La cantidad de palabras es: {count}")