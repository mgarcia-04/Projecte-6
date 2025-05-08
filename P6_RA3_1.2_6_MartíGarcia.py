#Cicle: ASIX
#Autor: Martí Garcia
#Data: 06-05-2025
#Versio: 1.0
#Descripcio: 4. 6. Crea una classe CompteBancari

class CompteBancari:
    def __init__(self, saldo):
        self.saldo = saldo

    def Moviments(self):
        print(f"Saldo disponible: {self.saldo}")
        ingres = int(input("Introdueix la quantitat que vols ingressar: "))
        saldo_ingressat = self.saldo + ingres
        retirada = int(input("Ara la quantitat que dessitges retirar: "))
        saldo_retirat = saldo_ingressat - retirada

        print(f"El saldo final al compte és de {saldo_retirat}€")

diners = CompteBancari(500)

diners.Moviments()

    