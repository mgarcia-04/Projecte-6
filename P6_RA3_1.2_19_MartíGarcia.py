#Cicle: ASIX
#Autor: Martí Garcia
#Data: 08-05-2025
#Versio: 1.0
#Descripcio: 9. Crea un llistat de cercles i mostra quins tenen àrea superior a 50.

import math

class Cercle:
    def __init__(self, nom, radi):
        self.nom = nom
        self.radi = radi

    def calcular_area(self):
        return math.pi * (self.radi ** 2)

cercles = [
    Cercle("Cercle 1", 5),
    Cercle("Cercle 2", 13),
    Cercle("Cercle 3", 2),
    Cercle("Cercle 4", 3),
    Cercle("Cercle 5", 6)
]

print("Cercles amb àrea superior o igual a 50:")
for cercle in cercles:
    area = cercle.calcular_area()
    if area >= 50:
        print(f"{cercle.nom}: {area:.2f}")


    
    
   