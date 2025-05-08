#Cicle: ASIX
#Autor: Martí Garcia
#Data: 06-05-2025
#Versio: 1.0
#Descripcio: 4. 8. Crea una classe Animal

class Animal:
    def __init__(self, nom, especie):
        self.nom = nom
        self.especie = especie

    def fer_soroll(self):
        print(f"{self.nom}, el qual és una {self.especie} fa un soroll")
    
soroll = Animal("Tobias", "Guineu")
soroll.fer_soroll()