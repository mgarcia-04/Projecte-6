#Cicle: ASIX
#Autor: Martí Garcia
#Data: 06-05-2025
#Versio: 1.0
#Descripcio: 3. Crea una llista d’estudiants. Mostra només els que han aprovat.

class Estudiant:
    def __init__(self, nom, nota):
        self.nom = nom
        self.nota = nota

    def correccio(self):
        if self.nota >= 5:
            print(f"Enhorabona {self.nom}, has tret un {self.nota}")

estudiants = [
    Estudiant("Anna", 8),
    Estudiant("Tobias", 4),
    Estudiant("Marta", 5),
    Estudiant("Joan", 2),
    Estudiant("Marc", 7)
]

for estudiant in estudiants:
    if estudiant.nota >= 5:
        estudiant.correccio()