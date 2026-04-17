numeros = [4,5,17,16]

#Encontrando el numero mayor de una lista

numero_alto = max(numeros)
print(numero_alto)

numero_bajo = min(numeros)
print(numero_bajo)

#Redondeando a 6 decimales

numero = round(12.345,2)
print(numero)

#Retorna false ..> 0, vacio, false, ninguno
resultado = bool(None)
print(resultado)

#Retorna true si el parametro es verdadero
resultado_all = all([234, "True", [344,23]])
print(resultado_all)

#Suma total de todos los iterables
suma = sum(numeros)
print(suma)