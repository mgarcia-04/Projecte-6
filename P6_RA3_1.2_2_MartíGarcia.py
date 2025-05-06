#Cicle: ASIX
#Autor: Martí Garcia
#Data: 06-05-2025
#Versio: 1.0
#Descripcio: 1. Crea una classe Cotxe

class Rectangle:
    def __init__(self, amplada, alçada):
        self.amplada = amplada
        self.alçada = alçada

    def area(self):
        return self.amplada * self.alçada

    def perimetre(self):
        return 2 * (self.amplada + self.alçada)
    
rectangle = Rectangle(50, 70)

print(f"Àrea rectangle: {rectangle.area()}\nPerímetre rectangle: {rectangle.perimetre()}")

