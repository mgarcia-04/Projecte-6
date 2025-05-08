#Cicle: ASIX
#Autor: Martí Garcia
#Data: 06-05-2025
#Versio: 1.0
#Descripcio: 1. Crea dos cotxes amb la classe Cotxe i imprimeix-ne la informació.

class Cotxe:
    def __init__(self, marca, model):
        self.marca = marca
        self.model = model

    def descriure(self):
        print(f"Cotxe: {self.marca} {self.model}")

cotxe1 = Cotxe("Seat", "León")

cotxe2 = Cotxe("Ford", "Focus")

print("Informació del primer cotxe:")
cotxe1.descriure()

print("\nInformació del segon cotxe:")
cotxe2.descriure()
