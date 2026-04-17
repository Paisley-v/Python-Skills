#creando un conjunto con set y metiendo una tupla dentro de una tupla

conjunto = set(["dato1", "dato2", ("d4")])
print(conjunto)

#metiendo un conjunto dentro de otro conjunto
conjunto1 = frozenset({"d1", "d2"})
conjunto2 = ([conjunto1, "d3"])
print(conjunto2)

#Teoria de conjuntos

conjunto3 = {1,2,3,4}
conjunto4= {1,2,3}

#verificando si es un subconjunto
resultado= conjunto4.issubset(conjunto3)
#resultado = conjunto4 <= conjunto3

resultado2 = conjunto3.issuperset(conjunto4)
#resultado2 = conjunto3 >= conjunto4
print(resultado)
print(resultado2)

#verificar si hay algun nunmero en comun, es True si no hay un numero igual
resultado3 = conjunto4.isdisjoint(conjunto3)
print(resultado3)

