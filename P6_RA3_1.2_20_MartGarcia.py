#Cicle: ASIX
#Autor: Martí Garcia
#Data: 08-05-2025
#Versio: 1.0
#Descripcio: 10. Fes una funció que rebi una llista de persones i imprimeixi només les que tenen més de 30 anys.

class Persona:
    def __init__(self, nom, edat):
        self.nom = nom
        self.edat = edat

    def presentar_se(self):
        print(f"Hola, soc {self.nom} i tinc {self.edat} anys")

def imprimir_majors_de_30(llista_persones):
    print("Persones majors de 30 anys:")
    for persona in llista_persones:
        if persona.edat > 30:
            persona.presentar_se()
            print("-" * 20)

persones = [
    Persona("Anna", 35),
    Persona("Pere", 28),
    Persona("Carla", 42),
    Persona("Joan", 30),
    Persona("Marta", 51),
    Persona("Lluís", 25)
]

imprimir_majors_de_30(persones)
