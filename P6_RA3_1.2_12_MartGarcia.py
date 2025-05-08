#Cicle: ASIX
#Autor: Martí Garcia
#Data: 06-05-2025
#Versio: 1.0
#Descripcio: 2. Crea 3 rectangles amb diferents mides. Mostra l’àrea de cadascun.

class Rectangle:
    def __init__(self, amplada, alçada):
        self.amplada = amplada
        self.alçada = alçada

    def area(self):
        return self.amplada * self.alçada

    def perimetre(self):
        return 2 * (self.amplada + self.alçada)
    
rectangle1 = Rectangle(50, 70)
rectangle2 = Rectangle(20, 60)
rectangle3 = Rectangle(60, 130)

print(f"Àrea rectangle 1: {rectangle1.area()}")
print(f"\nÀrea rectangle 1: {rectangle2.area()}")
print(f"\nÀrea rectangle 1: {rectangle3.area()}")