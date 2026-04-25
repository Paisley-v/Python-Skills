#metodo de resolución de orden
#orden en el que python busca herencia, que se ejecuta primero

class a:
    def hablar (self):
        print("Hola desde A")
        
class b(a):
    def hablar (self):
        print("Hola desde b")
        
class c(a):
    def hablar (self):
        print("Hola desde c")
       
class d(b,c):
    def hablar (self):
        print("Hola desde d")
        
        
d= d()

d.hablar()

b.hablar(d)


#Primero llama a la clase actual
#Segundo a la segunda clase que hereda
#Tercero a la tercera clase que hereda
#si no encuentra b o c, busca a
    
    
#ejecutar b desde d