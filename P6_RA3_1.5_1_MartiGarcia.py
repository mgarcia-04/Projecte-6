#Cicle: ASIX
#Autor: Martí Garcia
#Data: 12-05-2025
#Versio: 1.0
#Descripcio: Exercici 1: Animals

class Animal:
    def parlar(self):
        pass

class Gos(Animal):
    def parlar(self):
        print("Bup bup!")

class Gat(Animal):
    def parlar(self):
        print("Miau!")

gos = Gos()
gat = Gat()

gos.parlar()
gat.parlar()