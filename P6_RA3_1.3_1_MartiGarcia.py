#Cicle: ASIX
#Autor: Martí Garcia
#Data: 08-05-2025
#Versio: 1.0
#Descripcio: 1. Compte Bancari Simple

class CompteBancari:
    def __init__(self, saldo_inicial):
        self.__saldo = saldo_inicial

    def ingressar(self, quantitat):
        if quantitat >= 0:
            self.__saldo += quantitat
            print(f"S'han ingressat {quantitat}€. Nou saldo: {self.consultar_saldo()}€")
        else:
            print("La quantitat a ingressar no pot ser negativa.")

    def retirar(self, quantitat):
        if quantitat > 0:
            if quantitat <= self.__saldo:
                self.__saldo -= quantitat
                print(f"S'han retirat {quantitat}€. Nou saldo: {self.consultar_saldo()}€")
            else:
                print(f"No hi ha suficient saldo per retirar {quantitat}€. Saldo actual: {self.consultar_saldo()}€")
        else:
            print("La quantitat a retirar ha de ser positiva.")

    def consultar_saldo(self):
        return self.__saldo

compte = CompteBancari(100)

compte.ingressar(50)
compte.ingressar(-20)
compte.retirar(30)
compte.retirar(200)

print(f"Saldo final: {compte.consultar_saldo()}€")