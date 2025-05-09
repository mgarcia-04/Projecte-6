#Cicle: ASIX
#Autor: Martí Garcia
#Data: 08-05-2025
#Versio: 1.0
#Descripcio: 4. Contrasenya segura

class Usuari:
    def __init__(self, nom_usuari, contrasenya_inicial):
        self.nom_usuari = nom_usuari
        self.__contrasenya = "" 
        self.canviar_contrasenya(contrasenya_inicial)

    def canviar_contrasenya(self, nova_contrasenya):
        if len(nova_contrasenya) >= 8:
            self.__contrasenya = nova_contrasenya
            print(f"Contrasenya per a l'usuari '{self.nom_usuari}' canviada amb èxit.")
            return True
        else:
            print(f"Error: La contrasenya ha de tenir almenys 8 caràcters. No s'ha canviat la contrasenya per a '{self.nom_usuari}'.")
            return False

    def verificar_contrasenya(self, clau):
        if clau == self.__contrasenya:
            print("Contrasenya verificada correctament.")
            return True
        else:
            print("Contrasenya incorrecta.")
            return False

usuari1 = Usuari("Joan", "contrasenya123")
print(f"Nom d'usuari: {usuari1.nom_usuari}")

usuari1.canviar_contrasenya("curta")
usuari1.canviar_contrasenya("llarga123")

usuari1.verificar_contrasenya("llarga123")
usuari1.verificar_contrasenya("contrasenyaerronia")