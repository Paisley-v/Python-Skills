
#si el modulo estuviera en la misma ruta
import funciones_buenas.saludar as m_saludar

print(m_saludar.saludar("Kurisu"))


#######


#si el modulo estuviera en una ruta afuer
import sys 

sys.path.append("C\\Users\\... funciones buenas") #muestra las rutas de los archivos


#import saludar 

print(m_saludar.salduar("Milena"))