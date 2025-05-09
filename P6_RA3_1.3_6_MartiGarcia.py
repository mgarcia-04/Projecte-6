#Cicle: ASIX
#Autor: Martí Garcia
#Data: 08-05-2025
#Versio: 1.0
#Descripcio: 6. Producte amb preu controlat

class Producte:
    def __init__(self, nom, __preu):
        self.nom = nom
        self.__preu = __preu
    
    def obtenir_preu(self):
        return self.__preu
    
    def modificar_preu(self, nou_preu):
        if nou_preu > 0:
            self.__preu = nou_preu
        else:
            print(f"El preu ha de ser major a 0€")

producte1 = Producte("Piña", 2)
print(f"Preu Original:\n{producte1.nom}: {producte1.obtenir_preu()}€")


producte1.modificar_preu(3)
print(f"Preu Actualitzat:\n{producte1.nom}: {producte1.obtenir_preu()}€")