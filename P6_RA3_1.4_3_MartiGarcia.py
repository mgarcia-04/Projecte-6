#Cicle: ASIX
#Autor: Martí Garcia
#Data: 08-05-2025
#Versio: 1.0
#Descripcio: 3. Refés el codi perquè la lògica de descompte no estigui codificada dins CarretCompra.

class Descompte20:
    def aplicar(self, total):
        return total * 0.2  # 20% de descompte

class CarretCompra:
    def __init__(self, total, estrategia_descompte):
        self.total = total
        self.estrategia_descompte = estrategia_descompte  # Injectem l'estratègia de descompte

    def calcular_total_amb_descompte(self):
        descompte = self.estrategia_descompte.aplicar(self.total)
        return self.total - descompte