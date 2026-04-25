class animal:
    def comer(self):
        print("animal comiendo")
        
class ave(animal):
    def volar(self):
        print("el animal esta volando")
        
class mamifero(animal):
    def amamantar(self):
        print("el mamifero esta amamantando")
        
class Murcielago(mamifero,ave):
    pass

murcielago = Murcielago()

murcielago.comer()
murcielago.amamantar()
murcielago.volar()

print(Murcielago.mro())