

#importando un modulo y asignandole el nombre sal

import modulo_saludar as sal

saludo = sal.saludar("juan")
print(saludo)


print()

#segunda forma
# importando dos funciones desde un modulo
from modulo_saludar import saludar,saludar2 as s2

#variables
saludoo = saludar("Jhon")
saludo2 = s2("sofia")

print(saludo)
print(saludo2)

#para ver las propiades y variables
#print(dir(modulo_saludar))