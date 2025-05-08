#Cicle: ASIX
#Autor: Martí Garcia
#Data: 06-05-2025
#Versio: 1.0
#Descripcio: 4. 5. Crea una classe Estudiant

class Estudiant:
    def __init__(self, nom, nota):
        self.nom = nom
        self.nota = nota

    def correccio(self):
        if self.nota >= 5:
            print("Aprovat!")
        else:
            print("Suspés!")

nota = Estudiant("Marc", 4)

nota.correccio()    
        
    