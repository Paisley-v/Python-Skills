#que cada class haga su propia forma
#que un gato haga miau y un perro guau con la variable sonido

#class Animal():
    #def sonido(self):
        #pass

class Gato():  #(Animal) polimorfismo por herencia
    def sonido(self):
        return "miau"
    
class Perro():
    def sonido(self):  #polimorfismo de clase
        return "guau"
    
def hacer_sonido(animal):   #polimorfismo de funcion
    print(animal.sonido())
    
gato = Gato()
perro = Perro()

print(perro.sonido())

hacer_sonido(gato)