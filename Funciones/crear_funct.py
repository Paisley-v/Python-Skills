
# creando una funcion simple
def saludar():
     print("Hola jhon, como estas")

saludar() #ejecutando la funcion simple
saludar()
saludar()
saludar()

#ejecutando una funcion que tenga parametros

def bienvenido(nombre, sexo):
    
    sexo = sexo.lower() #converitr texto a miniscula
    
    if (sexo == "f"):
        adjetivo = "Maestra"
    elif (sexo == "m"):
        adjetivo = "Maestro"
    else:
        adjetivo = "Titan"
    
    print(f"Hola {nombre}, mi {adjetivo} ¿que tal?")
    
bienvenido("Camila", "F")
bienvenido("Jhon", "M")
bienvenido("thor", "X")

#Crear una funcione que retorne valores

def crear_contraseña_random(num):
    c = "abcdefghij"
    num_entero = str(num)  #el numero de entrada se convierte a entero
    num= int(num_entero[0]) #solo se queda con el primer digito del numero
    c1 = num-2
    c2 = num     #asigna una posición semialeatoria
    c3 = num -5
    contraseña = f"{c[c1]}{c[c2]}{c[c3]}"  #pone la posición de la cadena
    return (contraseña,num)  #almacena el valor sin que se muestre en consola

password,primer_numero = crear_contraseña_random(988)
frase = f"Tu contraseña nueva es: {password}"    
print(frase)
print(f"El numero utilizado fue: {primer_numero}")