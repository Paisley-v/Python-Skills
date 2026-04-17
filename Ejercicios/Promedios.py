# Diferencia en porcentaje entre el curso menor y 
# el más rapido
# el más lento
# el promedio

#Promedios de duración
lento = 7
rapido = 2.5
promedio = 4
actual = 1.5

#Duración de crudos
crudo_promedio = 5
crudo_actual = 3.5

curso_actual = 100 - actual * 100
dif_rap =  100 - actual / rapido * 100
dif_len =  100 - actual / lento * 100
dif_pro =  100 - actual / promedio * 100

print("Dura un ", dif_rap, "% menos que el más rapido")
print("Dura un ", round(dif_len, 1), "% menos que el más rapido")
print("Dura un ", dif_pro, "% menos que el más rapido")
print()
#Porcentaje de material inservible
# Promedio de los cursos
#Promedio actual

tiempo_vacio_pro =  100 - promedio / crudo_promedio * 100
print("Se muestra un tiempo vacio promedio de en otros cursos", round(tiempo_vacio_pro, 1), "% menos que el promedio")

tiempo_vacio_pro =  100 - actual / crudo_actual * 100
print("Se muestra un tiempo vacio promedio de en otros cursos", round(tiempo_vacio_pro, 1), "% menos que el promedio")
print()
#En 10 horas de otros cursos a cuantas de otros cursos equivale y al reves

k =  promedio / actual *10
print("Ver 10 horas de este curso equivale a ver ", round(k, 1), "horas de otros cursos" )

m =  actual *10 / promedio
print("Ver 10 horas de otros cursos equivale a ver ", round(m, 1), "horas de otros cursos" )