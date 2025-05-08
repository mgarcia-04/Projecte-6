#Cicle: ASIX
#Autor: Martí Garcia
#Data: 06-05-2025
#Versio: 1.0
#Descripcio: 4. 7. Crea una classe Cercle

import math

class Cercle:
    def __init__(self, radi):
        self.radi = radi

    def Calculs(self):
        area_cercle = ((self.radi ** 2) * math.pi)
        perimetre_cercle = ((self.radi * 2) * math.pi)
        print(f"L'àrea del cercle de {self.radi}cm de radi és: {area_cercle} cm²")
        print(f"El perímetre del cercle de {self.radi} és: {perimetre_cercle} cm²")

mesures = Cercle(20)

mesures.Calculs()