#Cicle: ASIX
#Autor: Martí Garcia
#Data: 06-05-2025
#Versio: 1.0
#Descripcio: 5. Fes una funció que rebi una llista de productes i n’apliqui un descompte del 10% a tots.

class Producte:
    def __init__(self, nom, preu):
        self.nom = nom
        self.preu = preu

    def descompte(self, percentatge):
            descompte = (self.preu * percentatge) / 100
            self.preu -= descompte

productes = [
    Producte("Monitor", 200),
    Producte("Portàtil", 560),
    Producte("Cadira", 130),
    Producte("Mouse", 40)
]

print(f"Preus originals:")
for producte in productes:
    print(f"{producte.nom}: {producte.preu:}€")

for producte in productes:
    producte.descompte(10)

print(f"\nPreus descomptats:")
for producte in productes:
    print(f"{producte.nom}: {producte.preu:.2f}€")
