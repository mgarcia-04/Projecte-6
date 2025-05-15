#Cicle: ASIX
#Autor: Martí Garcia
#Data: 12-05-2025
#Versio: 1.0
#Descripcio: Exercici 2: Vehicles

class Vehicle:
    def __init__(self, marca):
        self.marca = marca

    def arrencar(self):
        print(f"El {self.marca} arranca!")

class Cotxe(Vehicle):
    def __init__(self, marca):
        super().__init__(marca)

    def tocar_claxon(self):
        print(f"Pip pip!")

cotxe = Cotxe("Seat")

cotxe.arrencar()
cotxe.tocar_claxon()