#Cicle: ASIX
#Autor: Martí Garcia
#Data: 06-05-2025
#Versio: 1.0
#Descripcio: 4. Crea una classe Producte

class Producte:
    def __init__(self, nom, preu):
        self.nom = nom
        self.preu = preu

    def descompte_deu_percent(self):
        preu_descomptat = self.preu - ((self.preu * 10) / 100)
        print(f"El preu original del {self.nom} és {self.preu}€\nEl preu descomptat per un 10% és {preu_descomptat}€")
    
monitor = Producte("monitor", 200)

monitor.descompte_deu_percent()