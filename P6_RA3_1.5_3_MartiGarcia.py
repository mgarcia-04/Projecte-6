#Cicle: ASIX
#Autor: Martí Garcia
#Data: 12-05-2025
#Versio: 1.0
#Descripcio: Exercici 3: Persones i treballadors

class Persona:
    def __init__(self, nom, edat):
        self.nom = nom
        self.edat = edat

    def saludar(self):
        print(f"Hola, soc {self.nom}")

class Treballador(Persona):
    def __init__(self, nom, edat, feina):
        self.feina = feina

    def mostrar_feina(self):
        print(f"Treballo com a {self.feina}")

treball = Treballador("Jaume""fuster")

treball.saludar()
treball.mostrar_feina()