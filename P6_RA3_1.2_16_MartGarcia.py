#Cicle: ASIX
#Autor: Martí Garcia
#Data: 06-05-2025
#Versio: 1.0
#Descripcio: 6. Crea dos punts i calcula la distància entre ells.

class Punts:
    def __init__(self, km):
        self.km = km

Punt1 = Punts(24.7)
Punt2 = Punts(42.3)

distancia = abs(Punt1.km - Punt2.km)

print(f"La distància és: {distancia:.2f}")


