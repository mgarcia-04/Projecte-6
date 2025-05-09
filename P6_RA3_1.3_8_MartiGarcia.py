#Cicle: ASIX
#Autor: Martí Garcia
#Data: 08-05-2025
#Versio: 1.0
#Descripcio: 8. Alumne amb edat controlada

class Alumne:
    def __init__(self, nom, edat_actual):
        self.nom = nom
        self.__edat = 0
        self.get_edat = edat_actual

    @property
    def get_edat(self):
        return self.__edat
    
    @get_edat.setter
    def get_edat(self, edat_alumne):
        if edat_alumne > 0:
            self.__edat = edat_alumne
            print(f"Nom: {self.nom}\nEdat: {self.__edat}")
        else:
            print("L'edat no pot ser negativa ni zero!")

anys = Alumne("Tobias", 13)

anys.get_edat


