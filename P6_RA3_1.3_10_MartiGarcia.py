#Cicle: ASIX
#Autor: Martí Garcia
#Data: 08-05-2025
#Versio: 1.0
#Descripcio: 10. Email d’un usuari

class CompteUsuari:
    def __init__(self, nom, email_actual):
        self.nom = nom
        self.__email = ""
        self.get_email = email_actual

    @property
    def get_email(self):
        return self.__email
    
    @get_email.setter
    def get_email(self, email):
        if isinstance(email, str) and "@" in email and "." in email:
            self.__email = email
            print(f"L'email de {self.nom} és: {self.__email}")
        else:
            print(f"L'email {email} no és valid!")

correu_usuari = CompteUsuari("Tobias", "mgarcia2@iesjulioantonio.cat")