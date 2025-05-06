#Cicle: ASIX
#Autor: Martí Garcia
#Data: 06-05-2025
#Versio: 1.0
#Descripcio: 3. Crea una classe Persona

class Persona:
    def __init__(self, nom, edat):
        self.nom = nom
        self.edat = edat

    def presentar_se(self):
        print(f"Hola, soc {jo.nom} i tinc {jo.edat} anys")
    
jo = Persona("Martí", 20)

jo.presentar_se()