#Cicle: ASIX
#Autor: Martí Garcia
#Data: 06-05-2025
#Versio: 1.0
#Descripcio: 1. Crea una classe Cotxe


class Cotxe:
    def __init__(self, marca, model):
        self.marca = marca
        self.model = model

    def descriure(self):
        print(f"Cotxe: {self.marca} {self.model}")

cotxe1 = Cotxe("Toyota", "Corolla")

cotxe1.descriure()