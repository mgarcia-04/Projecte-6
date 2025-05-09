#Cicle: ASIX
#Autor: Martí Garcia
#Data: 08-05-2025
#Versio: 1.0
#Descripcio: 7. Temps en hores

class Rellotge:
    def __init__(self, hores_inicials):
        self.__hores = 0
        self.get_hores = hores_inicials

    @property
    def get_hores(self):
        return self.__hores

    @get_hores.setter
    def get_hores(self, nova_hora):
        if 0 <= nova_hora <= 23:
            self.__hores = nova_hora
            print(f"{nova_hora}:00")
        else:
            print("La hora indicada no es possible!")

hora_digital = Rellotge(26)
hora_digital.get_hores