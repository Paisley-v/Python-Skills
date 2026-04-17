#Creando mi propia excepcion personalizada

class MiExcepcion(Exception):
    def __init__(self,err):
        print(f"cometiste el error: {err}")
  
  
  
  
#Lanzando propia excepcion
try:      
    raise ZeroDivisionError("Dividisste por 0")

except: 
    print("xxx")