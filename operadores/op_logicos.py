#AND       Tienen que ser ambas condiciones verdaderas

Resultado= True & True # Devolver True
Resultado2 = False & True #Devolver False
Resultado3 = True & False #Devolver False
Resultado4 = False & False #Devolver False

#OR        Algunas de las dos condicones tiene que ser verdadera

Resultado5= True | True # Devolver True
Resultado6 = False | True #Devolver True
Resultado7 = True | False #Devolver True
Resultado8 = False | False #Devolver False

#NOT  Invierte el valor de la condicion

Resultado9= not 2==2 # Devolver False
Resultado10 = not 2==2 #Devolver True

print(Resultado)