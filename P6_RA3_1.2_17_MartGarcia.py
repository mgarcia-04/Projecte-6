#Cicle: ASIX
#Autor: Martí Garcia
#Data: 06-05-2025
#Versio: 1.0
#Descripcio: 7. Crea una classe Gos que hereti d’Animal i sobreescrigui fer_soroll() per dir “Bup bup!”.

class Animal:
    def __init__(self, nom, especie):
        self.nom = nom
        self.especie = especie

    def fer_soroll(self):
        print(f"{self.nom}, el qual és un {self.especie} fa un soroll")

class Gos(Animal):
    def __init__(self, nom):
        super().__init__(nom, "labrador")

    def fer_soroll(self):
        print(f"{self.nom} fa: Bup bup!")

meu_gos = Gos("Buddy")

meu_gos.fer_soroll()

print(f"Nom del gos: {meu_gos.nom}")
print(f"Espècie de gos: {meu_gos.especie}")