#Cicle: ASIX
#Autor: Martí Garcia
#Data: 08-05-2025
#Versio: 1.0
#Descripcio: 2. Estudiant amb nota protegida

class Estudiant:
    def __init__(self, nom, _nota):
        self.nom = nom
        self._nota = _nota

    def llegir_nota(self):
        print(f"La nota actual de l'alumne {self.nom} és {self._nota}")

    def modificar_nota(self, nova_nota):
        if 0 <= self._nota <= 10:
            self._nota = nova_nota
            print(f"La nota de {self.nom} s'ha actualitzat a {nova_nota}")
        else:
            print("Error, la nota a de ser entre 0 i 10")

estudiant1 = Estudiant("Tobias", 7)

estudiant1.llegir_nota()

estudiant1.modificar_nota(9)