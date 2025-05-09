#Cicle: ASIX
#Autor: Martí Garcia
#Data: 08-05-2025
#Versio: 1.0
#Descripcio: 8. Fes una classe Biblioteca que pugui afegir llibres (objectes Llibre) i mostrar-los tots.

class Llibre:
    def __init__(self, titol):
        self.titol = titol

    def mostrar_info(self):
        print(f"Títol: {self.titol}")

class Biblioteca:
    def __init__(self):
        self.llibres = []

    def afegir_llibre(self, llibre):
        self.llibres.append(llibre)

    def mostrar_llibres(self):
        for llibre in self.llibres:
            llibre.mostrar_info()

biblioteca = Biblioteca()

llibre1 = Llibre("El Quijote")
llibre2 = Llibre("Cien años de soledad")

biblioteca.afegir_llibre(llibre1)
biblioteca.afegir_llibre(llibre2)

biblioteca.mostrar_llibres()
