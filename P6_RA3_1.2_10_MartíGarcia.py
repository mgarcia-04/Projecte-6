#Cicle: ASIX
#Autor: Martí Garcia
#Data: 06-05-2025
#Versio: 1.0
#Descripcio: 4. 10. Crea una classe Punt

class Punt:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def distancia_entre_punts(self):
        distancia = self.x - self.y
        print(f"La distancia entre el punt X i el punt Y és de {abs(distancia)} km")

metres = Punt(37.7, 39.2)
metres.distancia_entre_punts()